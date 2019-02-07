# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

# 创建一个含有nan的矩阵
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['a', 'b', 'c', 'd'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df)

# 以下函数会返回处理过的矩阵，但是不会改变原矩阵。必须赋值使用
####################################
# dropna 直接去掉含有nan的列或行
####################################

df1 = df.dropna(axis=0, how='any')
print(df1)

####################################
# fillna() 将nan用其他值代替
####################################

df2 = df.fillna(value=0)
print(df2)

####################################
# isnull 检测是否有数据缺失，若存在就返回True
####################################

def checknan(input):
    true_flag = False
    inputx = input.shape[0]
    inputy = input.shape[1]
    temp = input.isnull()
    for i in range(inputx):
        for j in range(inputy):
            if temp.iloc[i, j] == True:
                true_flag = True
    if true_flag:
        print("lossdata")
        processing_flag = 1
    else:
         print("good")
         processing_flag = 0


checknan(df)




