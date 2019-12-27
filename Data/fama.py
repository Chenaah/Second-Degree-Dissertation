import pandas as pd
import numpy as np
x = pd.read_csv("all.csv")
y = pd.read_csv("fama_lite.csv")
z = pd.merge(x, y, on='日期_Date',how='left')
#z['市场溢酬因子__流通市值加权_Rmrf_tmv'] = np.where(x.日期_Date == y.日期_Date, y.市场溢酬因子__流通市值加权_Rmrf_tmv)
#z['市值因子__流通市值加权_Smb_tmv'] = np.where
#z['账面市值比因子__流通市值加权_Hml_tmv'] = 
z.to_csv("test.csv",encoding='UTF-8',index=False,float_format='%f')

#y.市场溢酬因子__流通市值加权_Rmrf_tmv[y['日期_Date'] == x['日期_Date']]  y[y.日期_Date == '2016-10-19']