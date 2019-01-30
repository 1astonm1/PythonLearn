# -*- coding:utf-8 -*-
import numpy as np


a = np.array([10, 20, 30, 40])  # 10, 20, 30, 40
b = np.arange(0, 4)     # 0, 1, 2, 3

# 1.基本运算加减乘 直接对应操作
c = a-b
print(c)

c = a+b
print(c)

c = a*b
print(c)

c = b**2    # 平方
print(c)

# 2、对数组进行三角函数计算
c = 10*np.sin(a)
print(c)

# 3、dot 矩阵乘法
a = np.array([[1, 2], [3, 4]])
b = np.arange(4).reshape((2, 2))

c = np.dot(a, b)     # method1
c = a.dot(b)     # method2
print(a, b)
print(c)

# 4、sum min max
a = np.random.random((2, 4))
print(a)
# sum全部元素相加、min全部元素中的最小值、max全部元素中的最大值
print(np.sum(a), np.min(a), np.max(a))
# axis=0时以列为单元查找，axis=0时以行为单元查找
print(np.min(a, axis=0), np.min(a, axis=1))

# 5、








