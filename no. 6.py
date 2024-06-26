import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
x = x[x !=0]

y = np.sin(x) / (3*x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$y =\\frac{{\\sin(x)}}{{3x}}$', color='g', linewidth=2)
plt.axhline(y=0, color='y')
plt.ayhline(y=0, color='y')
plt.title('Plot of $y =\\frac{{\\sin(x)}}{{3x}}$')
plt.xlabel('x', color='y')
plt.ylabel('y', color='g')
plt.grid(True)
plt.legend()
plt.show()
