#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 12:48:02 2017

@author: chientung
"""

import pandas as pd
import tushare as ts
import os
import glob
#import talib as ta
#from matplotlib import rc
#import glob

os.getcwd()

data_path = os.getcwd().decode('utf-8')  
os.chdir(data_path)

csvfile = glob.glob('*.csv')

dat = pd.read_csv(csvfile[0], encoding = 'gbk')

#tmp_dat = ts.get_k_data('000022', start='2005-01-01', end='2017-04-18', \
#                   ktype = 'M', autype='qfq')

subk = pd.DataFrame()
for i in range(dat.shape[0]):
    stri = str(dat['code'][i])
    if len(stri) < 6:
        stri = '0'*(6-len(stri)) + stri
    subk_tmp = ts.get_k_data(stri, start='2007-01-01', end='2017-06-30', \
                  ktype = 'M', autype='qfq')
    subk = [subk, subk_tmp]
    subk = pd.concat(subk)
    print(i)
    
#subk = subk.sort_values('date')
#date_list = subk['date']

date_group = subk.groupby('date')  

date_group.size()