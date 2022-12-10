# Draw a line from (1,3) to (2,8) then to (6,1) and finding to (8,10)
import matplotlib.pyplot as plt
import numpy as  np

xpts = np.array([1,2,6,8])
ypts =np.array([3,8,1,10])
plt.plot(xpts , ypts)
plt.show()
