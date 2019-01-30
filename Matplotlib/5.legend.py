# -*- coding:utf-8 -*-
# 给图加说明标签
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 50)

y1 = 2*x + 1
y2 = x**2

plt.figure()
# 加标签
plt.plot(x, y1, color='blue', label='square line')
plt.plot(x, y2, color='red', linestyle='--', label='linear line')
plt.legend(loc='best')   # upper right      upper left	   lower left	   lower right
                                    # right	center   left	  center right	    lower center	   upper center	   center
                                    # best自动分配最好的位置

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xlabel("this is x")
plt.ylabel("this is y")

# 设置坐标轴
ax = plt.gca()
ax.spines['right'].set_color("none")
ax.spines['top'].set_color("none")
ax.spines['bottom'].set_position(("data", 0))
ax.spines['left'].set_position(('data', 0))

plt.show()

