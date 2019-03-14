# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, -1, 50)

y1 = 2*x+10
y2 = x**2+10

plt.figure(num=1)
plt.plot(x, y1)
plt.show()


plt.figure(num = i)
plt.plot(x, y2, color='blue')
plt.plot(x, y1, color='red', linestyle='--')
plt.show()
