# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

##############################
# 1、series 索引在左边，值在右边
##############################

s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)

###############################
# 2、dataframe 是一个表格型的数据结构，它既有行索引， 又有列索引
###############################
dates = pd.date_range("20160101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)

print(df['b'])  # 按列索引

df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(df1)

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)              #
print(df2.dtypes)   # 查看每一列的数据类型
print(df2.index)     # 查看序号
print(df2.columns)  # 查看每种
print(df2.values)   # 查看所有值
df2.describe()         # 数据总结
print(df2.T)            # 转置
print(df2.sort_index(axis=1, ascending=False))  # 对index排序
print(df2.sort_values(by='B'))  # 按b的值排序











