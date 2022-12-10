#plt.grid() show grid on the graph
import matplotlib.pyplot as plt
import numpy as np
x1 = np.array([0,1,2,3,4,5])
y1 = np.array([2,4,6,8,10,12])
plt.plot(x1)
plt.plot(y1)
# plt.plot(x2,y2)
# plt.grid(axis='x')
# plt.grid(axis='y')
plt.grid(axis='x')

plt.title('Data about XYZ Company')
plt.xlabel('This is X-axis')
plt.ylabel('This is Y-Axis')
plt.show()
