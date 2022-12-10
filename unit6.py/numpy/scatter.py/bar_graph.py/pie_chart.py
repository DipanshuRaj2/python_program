import numpy as np
from matplotlib import pyplot as plt

x1 = np.array([35,25,40,15])

plt.pie(x1)

# plt.show()

# colors
clr = np.array(['Pink', 'Yellow', 'Black','Purple'])
plt.pie(x1,colors =clr)

# plt.show()

#startangle
plt.pie(x1 ,startangle =90)

plt.pie(x1 , startangle =90)

#explode
exp =[0.2 ,0,0,0]
plt.pie(x1 , explode =exp)

#plt.show()

#labels  

lbl =['Apple' , 'Mango' , 'Litchi', 'Cherry']

plt.pie (x1, labels = lbl)
#plt.show()

#shadow

plt.pie(x1, shadow ='True')

#legend 
plt.legend(title='Fruits')
plt.show()

