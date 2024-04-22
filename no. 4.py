import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)

y = x**4 + x**3 + x**2 + x + 1

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$y = x^4 +x^3 + x^2 + x + 1$', color='b', linewidth=2)
plt.title('Plot of $y = x^4 +x^3 + x^2 + x + 1$')
plt.xlabel('x', color='y')
plt.ylabel('y', color='g')
plt.grid(True)
plt.legend()
plt.show()
