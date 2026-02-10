
# import numpy as np 
# import pandas as pd
# import matplotlib as plot

# aarr = np.array([2,32,43,231,2332,54])
# print(aarr)
# add = aarr +10
# print(add)

# data ={
#     "name":["suresh","dasarth"],
#     "age":[21,21],
#     "salary":[15000,21000]
# }
# print(data)
# df = pd.DataFrame(data)
# print(df["name"])


# # df = pd.DataFrame(data)
# print("hello world...")

# user_name = input("enter your name = ")
# print("my name is ",user_name)
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Sample data
# data = [1, 2, 3, 4, 5]

# # Simple plot with matplotlib
# plt.plot(data)
# plt.title("Matplotlib Test")
#plt.show()

# Simple plot with seaborn
# sns.histplot(data)
# plt.title("Seaborn Test")
# plt.show()


# list=[1,2,3,4,5]
# print(list[1])
#  



import numpy as np
import matplotlib.pyplot as plt

# 1. Create a 200x200 zero matrix
size = 200
matrix = np.zeros((size, size))

# 2. Draw a diagonal line (top-left to bottom-right)
for i in range(size):
    matrix[i, i] = 1

# 3. Draw a square in the center
square_size = 50  # size of the square
start = (size - square_size) // 2
end = start + square_size
matrix[start:end, start:end] = 1

# 4. Draw a circular mask
center = size // 2
radius = 60
y, x = np.ogrid[:size, :size]
mask = (x - center)**2 + (y - center)**2 <= radius**2
matrix[mask] = 1

# 5. Visualize the result
plt.imshow(matrix, cmap='gray')
plt.title("Custom Pattern: Diagonal, Square, Circle")
plt.axis('off')
plt.show()