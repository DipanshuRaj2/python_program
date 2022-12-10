import numpy as np
import matplotlib as plt


clr = np.array(['Red','Blue', 'Yellow', 'Pink','Black', 'Orange','Green'])
x1 = np.array([0,1,5,7,810,12])
y1 = np.array([2,6,8,5,2,12,18])

x2 = np.array([1,4,6,8,10,12,15])
y2 = np.array([0,5,10,4,8,6,12])

plt.scatter(x2,y2, color ='yellow' , marker ='*')
plt.scatter(x1,y1,color =clr)





