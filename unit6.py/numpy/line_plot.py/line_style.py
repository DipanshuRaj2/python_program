#<<<<<<<linestyle in phython>>>>>>>>>>>>>>
#linestyle ='dashed'
#          =  'dotted'
#          = 'solid'
#show multiple lines in matplot>>>>>>>>>>>>>>>.
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0,1,2,3,4,5])
y1 = np.array([2,4,6,8,10,12])
x2 = np.array([3,4,5,6,7,8,9])
y2 = np.array([6,7,8,9,10,11,12])
plt.plot(x1,y1)                     #plt.plot(x1,y1,x2,y2)
plt.plot(x2,y2)
plt.show()