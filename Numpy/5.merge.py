# -*- coding:utf-8 -*-

# numpy array 合并

import numpy as np

#######################
# 1.vstack 上下合并
#######################
a = np.array([1, 1, 1])
b = np.array([2, 2, 2])

print(np.vstack((a, b)))
# [[1,1,1]
# [2,2,2]]


######################
# 2.hstack 横向合并
######################
print(np.hstack((a, b)))    # 横向合并
# [1, 1, 1, 2, 2, 2]

#####################
# 3.newaxis() 转置
#####################
a = np.array([1, 1, 1])[:, np.newaxis]
b = np.array([2, 2, 2])[:, np.newaxis]

print(a)
print(b)

#####################
# 4.concatenate 多个矩阵合并
#####################
c = np.concatenate((a, b, b, a), axis=0)
print(c)
# array([[1],       纵向排列
#       [1],
#       [1],
#       [2],
#       [2],
#       [2],
#       [2],
#       [2],
#       [2],
#       [1],
#       [1],
#       [1]])

d = np.concatenate((a, b, b, a), axis=1)
print(d)

# array([[1, 2, 2, 1],      横向排列
#        [1, 2, 2, 1],
#        [1, 2, 2, 1]])
