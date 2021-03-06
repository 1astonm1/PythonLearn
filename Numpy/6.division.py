# -*- coding:utf-8 -*-

import numpy as np

a = np.arange(12).reshape((2, 6))
print(a)
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]]


#############################
#   split 分割 axis=0横向分割 axis=1纵向分割 注意：只能等分！不等分会报错
#############################
print(np.split(a, 2, axis=0))   # 横向分割
print(np.split(a, 2, axis=1))   # 纵向分割
# [array([[0, 1, 2, 3, 4, 5]]), array([[ 6,  7,  8,  9, 10, 11]])]

# [array([[0, 1, 2],
#        [6, 7, 8]]), array([[ 3,  4,  5],
#        [ 9, 10, 11]])]
#############################
#   array_split 数据不等量分割
#############################
print(np.array_split(a, 4, axis=1))
# [array([[0, 1],[6, 7]]),
#
#  array([[2, 3],[8, 9]]),
#
#  array([[ 4],[10]]),
#  array([[ 5],[11]])]
#
############################
# vsplit hsplit
############################
print(np.vsplit(a, 2))      # 等于np.split(a, 2, asix=0)  横向分割
print(np.hsplit(a, 2))      # 等于np.split(a, 2, asix=1)   纵向分割

# [array([[0, 1, 2, 3, 4, 5]]), array([[ 6,  7,  8,  9, 10, 11]])]
# [array([[0, 1, 2],
#        [6, 7, 8]]), array([[ 3,  4,  5],
#        [ 9, 10, 11]])]



