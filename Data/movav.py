from __future__ import division
import pandas as pd
import numpy as np
import sys, time
from progressbar import *


x = pd.read_csv("test.csv")
x["movav"] = 0
pbar = ProgressBar().start()
for i in range(27,417207,27):
	x.loc[i-1,"movav"] = np.mean(x.账面市值比因子__流通市值加权_Hml_tmv[i-27:i])
	pbar.update(int((i / (417206)) * 100))
x = x["movav"]
x.to_csv("hml_movav.csv",encoding='UTF-8',index=False,float_format='%f')
pbar.finish()

x = pd.read_csv("test.csv")
x["movav"] = 0
pbar = ProgressBar().start()
for i in range(27,417207,27):
	x.loc[i-1,"movav"] = np.mean(x.市值因子__流通市值加权_Smb_tmv[i-27:i])
	pbar.update(int((i / (417206)) * 100))
x = x["movav"]
x.to_csv("smb_movav.csv",encoding='UTF-8',index=False,float_format='%f')
pbar.finish()

x = pd.read_csv("test.csv")
x["movav"] = 0
pbar = ProgressBar().start()
for i in range(27,417207,27):
	x.loc[i-1,"movav"] = np.mean(x.流通市值加权平均市场日收益率_Drettmv[i-27:i])
	pbar.update(int((i / (417206)) * 100))
x = x["movav"]
x.to_csv("r_m_movav.csv",encoding='UTF-8',index=False,float_format='%f')
pbar.finish()

x = pd.read_csv("test.csv")
x["movav"] = 0
pbar = ProgressBar().start()
for i in range(27,417207,27):
	x.loc[i-1,"movav"] = np.mean(x.日无风险收益率_DRfRet[i-27:i])
	pbar.update(int((i / (417206)) * 100))
x = x["movav"]
x.to_csv("r_f_movav.csv",encoding='UTF-8',index=False,float_format='%f')
pbar.finish()