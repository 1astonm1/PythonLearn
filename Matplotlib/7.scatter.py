import numpy as np
import matplotlib.pyplot as plt

size = 1024  # 总数

X = np.random.normal(0, 1, size) # random.normal 具有标准正态分布的随机数
Y = np.random.normal(0, 1, size)
T = np.arctan2(Y, X)

# 画散点图
plt.scatter(X, Y, s=50, c=T, alpha=0.5) # c：颜色 s：点的大小 alpha：透明度（0,1）之间
# 限制范围
plt.xlim(-1.5, 1.5)
plt.xticks()
plt.ylim(-1.5, 1.5)
plt.yticks()
# 显示
plt.show()
