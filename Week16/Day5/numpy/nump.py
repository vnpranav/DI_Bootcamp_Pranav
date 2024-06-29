import numpy as np
# data ==> raw input

arr = np.array(range(10,21))
print(arr)
print(arr[3])
print("dimensions: ",arr.ndim)
print("shape: ",arr.shape)
print("size: ",arr.size)
print("data type: ",arr.dtype)

print('--------------------------------------------------')

arr_float = arr.astype('float64')
print(arr_float)
print("data type: ", arr_float.dtype)

print('--------------------------------------------------')

double = arr * 2

print(double)

print('--------------------------------------------------')