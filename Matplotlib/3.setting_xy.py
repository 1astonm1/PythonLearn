# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)

y = 3*x**3 + 1
y1 = 2*x+2

#生成表格
plt.figure()
plt.plot(x, y)      # 生成表格
plt.plot(x, y1, color='red', linestyle='--')

#设置x坐标轴
plt.xlim(-1, 3)     # 设置x，y轴范围
plt.ylim(-1, 2)
plt.xlabel("i am x")    # 设置x,y轴名字
plt.ylabel("i am y")


#调整边框
ax = plt.gca()
ax.spines['right'].set_color("none")    # 清除右边的边框
ax.spines['top'].set_color("none")      # 清除顶部的边框


# 调整坐标轴位置
# 方法1：直接设置
ax.xaxis.set_ticks_position('default')   # 所有位置：top，bottom，both，default，none
#方法2：通过set_position来设置
ax.spines['bottom'].set_position(('data', 0))    # （位置所有属性：outward，axes，data）
ax.spines['left'].set_position(('data',0))


plt.show()      # 显示表格
