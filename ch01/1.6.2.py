import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 그래프 그래기
plt.plot(x, y1, label='sin')
plt.plot(x, y2, label='cos')

plt.xlabel('x')
plt.ylabel('y')
plt.title('sin & cos')

plt.legend()
plt.show()

