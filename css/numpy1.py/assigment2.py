#1. Create a NumPy array
# Create a NumPy array containing numbers from 1 to 10.
#import numpy as np
# arr1=np.arange(1,10)
# print(arr1)
#2. Array shape
# Create a 3×3 matrix with values from 1 to 9.
#import numpy as np
# matrix=np.arange(1,10).reshape(3,3)
# print(matrix)
# print(arr)
#3.Zeros array
# Create a NumPy array of zeros with shape (4,4)
#import numpy as np
# arr1=np.zeros((4,4))
# print(arr1)
# 4.Ones array
# Create a NumPy array of ones with shape (3,5).
#import numpy as np
# arr1=np.ones((3,5))
# print(arr1)
# 4.Range array
# Create an array containing numbers from 10 to 50.
#import numpy as np
# arr1=np.arange(10,50)
# print(arr1)
# 6.Even numbers
# Create an array of even numbers from 10 to 50.
# import numpy as np
# arr1=np.arange(10,50)
# arr=even_number=arr1[arr1%2==0]
# print(arr)
# 7.Identity matrix
# Create a 4×4 identity matrix.
#import numpy as np
# matrix=np.arange(1,17).reshape(4,4)
#print(matrix)
#8. Random numbers
# Generate 5 random numbers between 0 and 1.
import numpy as np
# arr=np.random.rand(5)
# print(arr)
#9 Array indexing
# Given array [10,20,30,40,50], extract the element 30.
import numpy as np
# arr=np.array([10,20,30,40,50])
# print(arr[2])
# 10. Array slicing
# From [1,2,3,4,5,6,7], extract [3,4,5]
import numpy as np
# arr=np.array([1,2,3,4,5,6,7])
# print(arr[2:5])
# 11. Reshape array
# Convert the array [1,2,3,4,5,6] into a 2 × 3 matrix.
import numpy as np
# arr=np.arange(1,7).reshape(2,3)
# print(arr)
# 12. Matrix multiplication

# Multiply the matrices:

# A = [[1,2],
#      [3,4]]

# B = [[5,6],
#      [7,8]]

import numpy as np
# a=[[1,2],[3,4]]
# b=[[5,6],[7,8]]
# print(np.dot(a,b))
# 13. Find maximum value
# Find the maximum value in [4,8,1,9,3].
import numpy as np
# arr=np.array([4,8,1,9,3])
# arr1=np.max(arr)
# print(arr1)
# 14. Find minimum value
# Find the minimum value in [4,8,1,9,3].
# import numpy as np
# arr=np.array([4,8,1,9,3])
# arr1=np.min(arr)
# print(arr1)
# 15. Calculate mean
# Find the average of [10,20,30,40].
# import numpy as np
# arr=np.array([10,20,30,40])
# arr1=np.mean(arr)
# print(arr1)
# 16. Sum of elements
# Find the sum of all elements in [2,4,6,8,10].
# import numpy as np
# arr=np.array([2,4,6,8,10])
# arr1=np.sum(arr)
# print(arr1)
# 17. Transpose matrix
# Transpose:
# import numpy as np
# matrix=np.array([[1,2,3],
#                  [4,5,6]])
# print(np.transpose(matrix))
# 18. Element-wise addition
# Add arrays:
# import numpy as np
# a=[[1,2,3]]
# b=[[4,5,6]]
# print(a+b)
# 19. Boolean indexing
# Extract numbers greater than 15 from [5,10,15,20,25].
# import numpy as np
# ar=np.array([5,10,15,20,25])