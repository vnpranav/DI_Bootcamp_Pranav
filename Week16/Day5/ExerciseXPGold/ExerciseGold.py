import numpy as np
cube = np.random.random((3,3,3))
# print(cube)

grid = np.random.randint(1,1000, (10,10))
# print(grid.max())
# print(grid.min())

arr = np.ones((4,5))
arr[1:-1, 1:-1] = 0
# print(arr)

matrix = np.ones((3,3))
matrix = np.pad(matrix, 1)
# print(matrix)

nums = np.array([1,2,3,4,5,6])
nums[nums % 2 != 0] = -1
# print(nums)

square = np.diag([1,2,3,4,7])
print(square)