# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 50)

y1 = x*2 +1
#y2 = x**2

plt.figure()

plt.plot(x, y1, color='red', label='linear line')
plt.legend(loc='best')

ax = plt.gca()
ax.spines['top'].set_color("none")
ax.spines['right'].set_color("none")
ax.spines['bottom'].set_position(("data", 0))
ax.spines['left'].set_position(("data", 0))

plt.xlim(-3, 3)
plt.ylim(-6, 6)
# 画点和虚线
x0 = 1
y0 = 2*x0 + 1
plt.scatter(x0, y0, s=50, color='black')
plt.plot([x0, x0], [y0, 0], color='black', linestyle='--', lw=2.5)
# annotate使用说明 做标注
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
                    textcoords='offset points', fontsize=16,
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2'))



plt.show()
