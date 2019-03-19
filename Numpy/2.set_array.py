# -*- coding:utf-8 -*-
import numpy as np
# 1、正常创建
a = np.array([1, 2, 3])
print(a)
# [1 2 3]

# 2、指定数据类型
a = np.array([1, 2, 3], dtype=np.int)       # int int32 float float32
print(a.dtype)
# int32

# 3、创建全零矩阵
a = np.zeros((3, 4))  # 3行4列的全零数组
print(a)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]


# 4、创建全一矩阵，同时也能指定这些数据的类型：
a = np.ones((3, 4), dtype=np.int)
print(a)
# [[1 1 1 1]
#  [1 1 1 1]
#  [1 1 1 1]]

# 5、创建全空数组，其实每个值都是接近于零的：
a = np.empty((3, 4))    # 数据为empty，三行四列
print(a)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# 6、用arange创建连续数组：
a = np.arange(10, 20, 2)    # 从10到19的数据，2步长
print(a)
# [10,12,14,16,18]

# 7、用reshape改变数据形状:
a = np.arange(0, 20).reshape(4, 5)   # 把本来一行数据变成四行五列
print(a)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]]

# 8、用linspace创建线段型的数据
a = np.linspace(1, 10, 20).reshape(4, 5)  # 在1到10中间随机产生20个数据
print(a)

# [[ 1.          1.47368421  1.94736842  2.42105263  2.89473684]
#  [ 3.36842105  3.84210526  4.31578947  4.78947368  5.26315789]
#  [ 5.73684211  6.21052632  6.68421053  7.15789474  7.63157895]
#  [ 8.10526316  8.57894737  9.05263158  9.52631579 10.        ]]