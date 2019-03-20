# -*- coding:utf-8 -*-

# python base

# ********************************************类型和运算*************************************************#

# 测试类型的三种方法  推荐第三种
L = [1, 2, 3]
if type(L) == type([]):
    print("L is list")
if type(L) == list:
    print("L is list")
if isinstance(L,list):
    print("L is list")

# python中的数据类型：
1234, -1234, 0, 9999999                        # 整数
1.23, 1., 3.14e-10,                                  # 浮点数
0o177, 0x9ff, 0X9FF, 0b101010              # 八进制、十六进制、二进制数字
3 + 4j, 3.0 + 4.0j, 3J                             # 复数常量，也可以用complex(real, image)来创建
hex(10), oct(10), bin(10)                       # 将十进制数转化为十六进制、八进制、二进制表示的“字符串”
# int(string, base)                                   # 将字符串转化为整数，base为进制数
float('inf'), float('-inf'), float('nan')       # 无穷大, 无穷小, 非数

a = 255
print(a.bit_length())

s1 = set([3, 5, 7, 9])
s2 = set([1, 3, 5, 7, 9])
output = s1.difference(s2)
print(output)
