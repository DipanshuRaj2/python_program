# #access array in phython
# #use index to access
# import numpy as np

# arr = np.array([1,2,3,4,5])
# print(arr[0]) #1st element
# print(arr[-1]) #last element
# sum=(arr[1]+arr[3])
# print(("Sum of array elements: "),sum)

# access array in 2d
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1][3])
print(arr[0][4])
#access in 3D array
import numpy as np
arr =np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(arr[0,1,2])