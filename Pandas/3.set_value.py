# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)

##################################
# 1.根据位置设置loc和iloc
##################################
df.iloc[2, 2] = 1111
df.loc['20130101', 'b'] = 2222      # 给出索引并赋值
print(df)


##################################
# 2.根据条件设置
##################################
df.b[df.a > 4] = 0  # b这一列中a中大于4的行全部清零
print(df)


#################################
# 3.按行或按列设置
################################
df['f'] = np.nan
print(df)

################################
# 4.添加数据
################################

df['e'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130101', periods=6))
print(df)




