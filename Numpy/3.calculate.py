# -*- coding:utf-8 -*-
import numpy as np


a = np.array([10, 20, 30, 40])  # 10, 20, 30, 40
b = np.arange(0, 4)     # 0, 1, 2, 3

##########################
# 1.基本运算加减乘 直接对应操作
##########################
c = a-b
print(c)

c = a+b
print(c)

c = a*b
print(c)

c = b**2    # 平方
print(c)

#########################
# 2、对数组进行三角函数计算
#########################
c = 10*np.sin(a)
print(c)

#########################
# 3、dot 矩阵乘法
#########################
a = np.array([[1, 2], [3, 4]])
b = np.arange(4).reshape((2, 2))

c = np.dot(a, b)     # method1
c = a.dot(b)     # method2
print(a, b)
print(c)

##########################
# 4、sum min max
##########################
a = np.random.random((2, 4))
print(a)
# sum全部元素相加、min全部元素中的最小值、max全部元素中的最大值
print(np.sum(a), np.min(a), np.max(a))
# axis=0时以列为单元查找，axis=0时以行为单元查找
print(np.min(a, axis=0), np.min(a, axis=1))

##########################
# 5、argmin 和 argmax、mean、average、median
##########################
a = np.arange(2, 14).reshape((3, 4))

print(np.argmin(a))     # 0 最小值的索引
print(np.argmax(a))     # 11 最大值的索引
print(np.mean(a))       # 求均值
print(np.median(a))     # 求中位值
print(np.average(a))    # 求均值

#############################
# 6、累加，累差
#############################
a = np.arange(2, 14).reshape((3, 4))

print(np.cumsum(a))     # 将每一个元素进行累加
print(np.diff(a))       # 将每一个元素进行累差

##############################
# 7、转置和排序
##############################
a = np.arange(14, 2, -1).reshape((3, 4))
print(np.sort(a))   # 从大到小排序

# 转置的两种方法
print(np.transpose(a))
print(a.T)

##############################
# 8、clip(Array,Array_min,Array_max)函数
##############################
# 给定范围，矩阵中比他大的值用最大值代替， 比他小的值用最小值代替
a = np.arange(14, 2, -1).reshape((3, 4))
print(np.clip(a, 5, 9))     # 选取5和9之间的值，范围外用最大最小值替代









