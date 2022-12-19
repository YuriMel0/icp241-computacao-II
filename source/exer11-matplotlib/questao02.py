import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,5.0,0.1)
func1 = np.exp(-x/2) * np.sin(2 * np.pi * x)
func2 = np.cos(x/2)
plt.subplot(211)
plt.plot(x,func1,x,func2,'ro-')
plt.grid(True)

dif_func = func2 - func1
plt.subplot(212)
plt.bar(np.arange(len(dif_func)), dif_func, 0.5, color='r')
plt.show()