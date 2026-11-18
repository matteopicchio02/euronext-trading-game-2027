import numpy as np, pandas as pd
from scipy.optimize import minimize
from pathlib import Path
P=Path('/mnt/data')
df=pd.read_csv(P/'ALPHA_daily_returns.csv',parse_dates=['Date']).set_index('Date').sort_index()
p=pd.read_csv(P/'portfolio_actual_2026-11-18.csv').set_index('ticker').loc[df.columns]
nav=50164.75
w=p.market_value_eur.to_numpy()/nav
n=len(w)
paris=np.array([x.endswith('.PA') for x in df.columns])
sector=p.sector.to_numpy()
sectors=[np.where(sector==s)[0] for s in sorted(set(sector))]
rets=df.to_numpy(dtype=float)
assert np.isfinite(rets).all() and len(df)==517

def cov_est(data):
  raw=np.cov(data,rowvar=False)*252
  # mild diagonal shrinkage to improve stability; no future info
  return .8*raw+.2*np.diag(np.diag(raw))

def optimize(cov,turnover=.24):
  from scipy.optimize import linprog, LinearConstraint
  A=[]; lo=[]; hi=[]
  def add(row,lower=-np.inf,upper=np.inf):A.append(row);lo.append(lower);hi.append(upper)
  for i in range(n):
    r=np.zeros(2*n);r[i]=1;r[n+i]=-1;add(r,upper=w[i])
    r=np.zeros(2*n);r[i]=-1;r[n+i]=-1;add(r,upper=-w[i])
  r=np.zeros(2*n);r[:n]=paris.astype(float);add(r,upper=.35)
  for inds in sectors:
    r=np.zeros(2*n);r[inds]=1;add(r,upper=.18)
  r=np.r_[np.ones(n),np.zeros(n)];add(r,lower=w.sum(),upper=w.sum())
  r=np.r_[np.zeros(n),np.ones(n)];add(r,upper=turnover)
  A=np.array(A);lo=np.array(lo);hi=np.array(hi)
  bounds=[(max(.005,wi-.018),min(.05,wi+.018)) for wi in w]+[(0,None)]*n
  e=np.isclose(lo,hi); u=np.isfinite(hi)&(~e);l=np.isfinite(lo)&(~e)
  A_ub=np.vstack([A[u],-A[l]]) if l.any() else A[u]
  b_ub=np.r_[hi[u],-lo[l]] if l.any() else hi[u]
  lp=linprog(np.r_[np.zeros(n),np.ones(n)],A_ub=A_ub,b_ub=b_ub,A_eq=A[e],b_eq=lo[e],bounds=bounds,method='highs')
  if not lp.success:raise RuntimeError('Infeasible: '+lp.message)
  def f(z):return 1000*z[:n]@cov@z[:n]+.04*np.sum((z[:n]-w)**2)
  def j(z):return np.r_[2000*cov@z[:n]+.08*(z[:n]-w),np.zeros(n)]
  res=minimize(f,lp.x,jac=j,method='SLSQP',constraints=[LinearConstraint(A,lo,hi)],bounds=bounds,options={'maxiter':1600,'ftol':1e-10})
  x=res.x[:n]
  if x[paris].sum()>.35001 or abs(x.sum()-w.sum())>1e-5 or np.abs(x-w).sum()>turnover+.0001 or max(x)>.05001:
    raise RuntimeError('Optimization constraints violated '+res.message)
  return x

def evaluate(x,data):
  # constant-weight daily rebalanced portfolio, zero transaction charges assumption
  r=data@x
  compound=np.prod(1+r)-1
  vol=np.std(r,ddof=1)*np.sqrt(252)
  annualret=(1+compound)**(252/len(r))-1 if 1+compound>0 else np.nan
  navs=np.cumprod(1+r)
  dd=np.min(navs/np.maximum.accumulate(np.r_[1.,navs])[1:]-1)
  sharpe=np.mean(r)/np.std(r,ddof=1)*np.sqrt(252)
  return dict(daily_n=len(r),period_return_pct=100*compound,ann_return_pct=100*annualret,ann_vol_pct=100*vol,max_drawdown_pct=100*dd,sharpe_zero_rf=sharpe)

# Single honest chronological 60/40 holdout
split=320
train,test=rets[:split],rets[split:]
models={'Attuale':w,'OOS_minvar_turnover24':optimize(cov_est(train),.24),'OOS_minvar_turnover16':optimize(cov_est(train),.16)}
rows=[]
for name,x in models.items():
  e=evaluate(x,test);e.update(scenario=name,train_last_date=str(df.index[split-1].date()),test_first_date=str(df.index[split].date()),test_last_date=str(df.index[-1].date()),gross_turnover_pct=100*np.abs(x-w).sum(),paris_pct=100*x[paris].sum(),ex_ante_train_vol_pct=100*np.sqrt(x@cov_est(train)@x))
  rows.append(e)
result=pd.DataFrame(rows).set_index('scenario')
result.to_csv(P/'ALPHA_oos_holdout_results.csv',float_format='%.6f')

# Walk forward: 252 lookback / 63 forward, no optimization using future returns
wf=[]
for st in range(252,len(df),63):
  end=min(st+63,len(df));a=rets[st-252:st];b=rets[st:end]
  baseline=evaluate(w,b)
  for label,x in [('Attuale',w),('Ottimizzato24',optimize(cov_est(a),.24)),('Ottimizzato16',optimize(cov_est(a),.16))]:
    e=evaluate(x,b); e.update(model=label,fold_from=str(df.index[st].date()),fold_to=str(df.index[end-1].date()),train_to=str(df.index[st-1].date()),gross_turnover_pct=100*sum(abs(x-w)))
    wf.append(e)
walk=pd.DataFrame(wf)
walk.to_csv(P/'ALPHA_oos_walkforward_folds.csv',index=False,float_format='%.6f')
# concatenate fold returns to correctly aggregate (different lengths)
whole={name:[] for name in ['Attuale','Ottimizzato24','Ottimizzato16']}
for st in range(252,len(df),63):
  end=min(st+63,len(df));a=rets[st-252:st];b=rets[st:end]
  for name,x in [('Attuale',w),('Ottimizzato24',optimize(cov_est(a),.24)),('Ottimizzato16',optimize(cov_est(a),.16))]:whole[name].extend(b@x)
agg=pd.DataFrame([dict(model=k,**evaluate(np.array([1.]),np.array(v).reshape(-1,1))) for k,v in whole.items()]).set_index('model')
agg.to_csv(P/'ALPHA_oos_walkforward_aggregate.csv',float_format='%.6f')
weights=pd.DataFrame({'ticker':df.columns,'name':p.name.values,'current_weight_pct':100*w})
for label,x in models.items():
 if label!='Attuale':weights[label+'_target_pct']=100*x;weights[label+'_delta_eur']=(x-w)*nav
weights.to_csv(P/'ALPHA_oos_weights_diagnostic.csv',index=False,float_format='%.6f')
print('HOLDOUT',result.round(3).to_string())
print('WALK FWD',agg.round(3).to_string())
print('FOLDS',walk[['model','fold_from','period_return_pct','ann_vol_pct','max_drawdown_pct']].round(3).to_string(index=False))
print('WEIGHTS',weights[['ticker','current_weight_pct','OOS_minvar_turnover16_target_pct','OOS_minvar_turnover16_delta_eur']].round(2).to_string(index=False))
