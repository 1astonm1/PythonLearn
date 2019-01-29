# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 50)
y = 2*x*x + 5*x + 10
plt.plot(x, y)
plt.show()
