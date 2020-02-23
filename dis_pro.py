import numpy as np
import matplotlib.pyplot as plt
from math import gamma

X = np.arange(0, 2, 1)

print(X)

p=1/2

# 計算式
Y=[p**x*(1-p)**(1-x) for x in X]

# 横軸の変数。縦軸の変数。
plt.bar(X,Y, width=0.08)

# 描画実行
plt.show()

result=np.random.choice(X,size=10,p=Y)

re=[list(result).count(0), list(result).count(1)]

# 横軸の変数。縦軸の変数。
plt.bar(X,re, width=0.08)

# 描画実行
plt.show()

#ベータ分布

a=10
b=5

p_x=[i / 50 for i in range(1, 50, 1)]

Beta= [gamma(a+b)/(gamma(a)*gamma(b))*p**(a-1)*(1-p)**(b-1) for p in p_x]

# 横軸の変数。縦軸の変数。
plt.plot(p_x,Beta)

# 描画実行
plt.show()
