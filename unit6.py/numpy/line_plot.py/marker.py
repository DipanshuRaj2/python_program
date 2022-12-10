#marker in matplot
import matplotlib.pyplot as plt
import numpy as np

ypts = np.array([3,8,6,15])
plt.plot(ypts, marker='*',ms = 10 , mec ='Yellow')#mec=marker edge colour
plt.show()