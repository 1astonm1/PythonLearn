# -*- coding:utf-8 -*-

import numpy as np

# 列表转化为矩阵
array = np.array([[1, 2, 3], [2, 3, 4]])
print(array)

# [[1 2 3]
#  [2 3 4]]

# 基本特征
print(array.ndim)   # 维度
print(array.shape)  # 行数和列数
print(array.shape[0])   # 只输出行数
print(array.shape[1])   # 只输出列数
print(array.size)   # 元素个数

# 2
# (2, 3)
# 2
# 3
# 6

for i in range(0, 2, 1):
    for j in range(0, 3, 1):
        print(("第"+str(i+1)+"行，第"+str(j+1)+"列的数值是：")+str(array[i][j]))  # 可以像二维数组一样调用array中的值

#
# 第1行，第1列的数值是：1
# 第1行，第2列的数值是：2
# 第1行，第3列的数值是：3
# 第2行，第1列的数值是：2
# 第2行，第2列的数值是：3
# 第2行，第3列的数值是：4

########################################################
# 修改其中某一个的值
########################################################
array[0][1] = 10
print(array)


# [[ 1 10  3]
#  [ 2  3  4]]
