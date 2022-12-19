import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2, 0.01)
func1 = np.sin((25*x)/2)
func2 = np.sin(63*x/10)
plt.subplot(221)
plt.plot(x,func1,'g-',x,func2,'r')
plt.grid(True)

plt.subplot(222)
plt.fill_between(x,func1,func2,where=func1>func2,color='g')
plt.fill_between(x,func1,func2,where=func2>func1,color='r')
plt.show()
