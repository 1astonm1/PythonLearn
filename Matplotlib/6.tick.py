# -*- coding:utf-8 -*-
# 修改图层顺序，防止遮住坐标
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 50)
y = 0.1*x

plt.figure()
plt.plot(x, y, linewidth=2, zorder=1)
plt.ylim(-2, 2)
plt.xlim(-2, 2)

ax = plt.gca()
ax.spines['top'].set_color("none")
ax.spines['right'].set_color("none")
ax.spines['bottom'].set_position(("data", 0))
ax.spines['left'].set_position(("data", 0))
# 此时图像遮住了坐标轴
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    # 在 plt 2.0.2 或更高的版本中, 设置 zorder 给 plot 在 z 轴方向排序
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7, zorder=2))

plt.show()
