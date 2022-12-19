import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5.0, 0.1)
y1 = np.exp(x)
y2 = 25*x-5
y3=x**3+x**2
plt.plot(x,y1,'bs-',x,y2,'g^-', x,y3,'r8-')
plt.legend(['exponencial', 'linear', 'terceiro grau'], loc='best')
plt.grid(True)
plt.show()