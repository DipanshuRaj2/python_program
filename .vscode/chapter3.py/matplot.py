import numpy as np 
from matplotlib import pyplot as plt
foodd={
    "apple":74,
    "hsb":39,
    "hbe":34
}

key1 = list(foodd.keys())
value1=list(foodd.values())


plt.pie(value1 , labels=key1)
plt.show()