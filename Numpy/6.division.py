# -*- coding:utf-8 -*-

import numpy as np

a = np.arange(12).reshape((2, 6))
print(a)

#############################
#   split 分割 axis=0横向分割 axis=1纵向分割 注意：只能等分！不等分会报错
#############################
print(np.split(a, 2, axis=0))   # 横向分割
print(np.split(a, 2, axis=1))   # 纵向分割

#############################
#   array_split 数据不等量分割
#############################
print(np.array_split(a, 4, axis=1))

############################
# vsplit hsplit
############################
print(np.vsplit(a, 2))      # 等于np.split(a, 2, asix=0)  横向分割
print(np.hsplit(a, 2))      # 等于np.split(a, 2, asix=1)   纵向分割




