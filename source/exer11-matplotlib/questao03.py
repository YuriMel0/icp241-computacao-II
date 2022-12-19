import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2, 0.05)
func1 = np.sin(25*x/2) - np.sin(63*x/10)
func2 = ((-13*x+15)/10)

plt.subplot(221)
plt.plot(x,func1,'g^-',x,func2,'b.')
plt.grid(True)

plt.subplot(222)
plt.fill_between(x,func1,func2,color='y')
plt.show()