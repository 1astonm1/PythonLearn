# -*- coding:utf-8 -*-

import numpy as np

a = np.arange(4)

b = a
c = a
d = b

a[0] = 11
print(a)

print(b is a)
print(c is a)
print(d is a)

d[1:3] = [22, 33]
print(a)
print(b)
print(c)

b = a.copy()
print(b)
a[3] = 44
print(a)
print(b)
