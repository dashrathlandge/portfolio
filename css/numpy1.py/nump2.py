# import time
# import random
# import numpy as np
# #normal python list
# start_time =time.time()  
# for i in range(random.randint(1,100000)):
#     list=[]
#     list.append(i)
#     end_time =time.time()
   
#     print(f"Time take create using list: {end_time -start_time} seconds")
#     break

# start_time =time.time()
# arr = np.arange(1,100000)
# end_time = time.time()
# print(f"time take to create using numpy array: {end_time - start_time} seconds") 

# import  numpy as np
import matplotlib.pyplot as pit

# arr =np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[15,16],[17,18],[19,20]])
# print(arr[4:6],arr[8:10])

# import numpy as np
# arr=np.arange(1,50,4)

# print(arr)
# import numpy as np
# import matplotlib.pyplot as plt

# count = int(input("enter pixel size x: "))
# constant_coeff = int(input("enter constant value c: "))
# diamond_size = int(input("enter diamond size: "))

# arr = np.full((count, count), constant_coeff)

# center = count // 2
# radius = diamond_size // 2

# # Create coordinate grid
# y, x = np.ogrid[:count, :count]

# # Manhattan distance mask (diamond shape)
# mask = np.abs(x - center) + np.abs(y - center) <= radius

# # Apply mask
# arr[mask] = 0

# plt.imshow(arr, cmap='hot')
# plt.colorbar()
# plt.show()

# import numpy as np

# arr= np.array([[10,20,30,40],[50,60,70,80],[90,100,102,103]])
# #print(arr[0,2])
# print(np.shape(arr))
# print(np.size(arr))#rows colums
# print(np.ndim(arr))
# print(type(arr))#type of element
# print(arr.dtype)#datatype of variable
# print(len(arr)) #number of nested values
# print(arr.astype(int))#conversion of datatype

#concatenate
# import numpy as np
# arr1= np.array([[30,40],[10,50]])
# arr2= np.array([[50,10],[5,3]])
# print(np.concatenate([arr1,arr2]))
# print(np.concatenate([arr1,arr2],axis=1))
# print(np.hstack([arr1,arr2]))#horizontal concatenation

# import numpy as np 
# import matplotlib.pyplot as plt
# a= np.array([[12,10],[12,13]])
# print(np.append(a,[10,20]))
# print(np.insert(a,[1,2],[100], axis =0))#array index value
# print(np.delete(a,1))
# lst =[100,200,300,400,600]
# print(lst)
# arr= np.array(lst)

# print(arr.reshape(5))# it reshape

# arr=np.
#2d array---------------------------------------
# points= np.random.randint(1,10,10)
# print(points)
# lst=list(range(10_000_000))
# arr=np.array([[1,2],[3,4],[5,6],[6,7]])

# print(arr[1:4],arr[:4])

# plt.scatter(arr[:4],arr[:4])
# plt.show()
# arr =np.array([[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1,11],[1,12],[1,13],[1,14],[1,15],[1,16],[1,17],[1,18],[1,19],[1,20]])
# print(arr[6:8]*arr[15:16])

# arr1=np.arange(1,21)
# print(arr1)

# arr2=np.ones(20)
# print(arr2)

# final_arr=np.column_stack(arr1,arr2)
# print(final_arr)

# print(final_arr[1:8],final_arr[11:19])

# import numpy as np
#  n=int(input("Enter dim of matrix:"))
# matrix=np.random.randint(1,100,n)
# print(matrix)

# m=np.diag(matrix)
# print("main diagonal",m)
# m=np.fliplr(matrix).diagonal()
# print("secondary diagonal",m)
# m=np.diag(matrix)
# print("sum of main diagonal",m )

# import numpy as np
# n=int(input(":"))

# arr=np.random.randint(1,10,(n,n))
# print(arr)
# print("n"*60)
# primar_diagonal= arr[np.arange(n),np.arange(n)]
# print(primar_diagonal)
# print("n"*60)
# secondray_diagonal=arr[np.arange(n),np.arange(n-1,-1,-1)]
# print(secondray_diagonal)
#one d array user input based element
# import numpy as np
# n=input("Enter element of array:")

# arr=np.array(n.split(","),dtype=int)
# print(arr[1])
# n=int(input("how many elements:"))
# arr=np.empty(n,dtype=int)
# for i in range(n):
#     arr=int(input(f"Enter element{i+1}"))
#     print(arr)
# #2nd array using the user input based element insertion
# n=int(input("enter matrix size:"))
# arr=np.array([list(map(int,input("enter element  for rows:").split(","))) for _ in range(n)])
# print(arr)
#lines space #farctes of data
# arr=np.linspace(1,2,500)
# print(arr)
# import numpy as py
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# x=np.linspace(0,2*np.pi,500)

# fig, axl =plt.subplots()
# line,=axl.plot(x,np.sin(x))

# def update_wave(frame):
#     y=np.sin(x + frame/10)
#     line.set_ydata(y)
#     return line
# ani=FuncAnimation(fig,update_wave,frames=200)
# plt.show()
# import numpy as py
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# x=np.linspace(0,4*np.pi,500)

# fig, axl =plt.subplots()
# line,=axl.plot(x,np.cos(x))

# def update_wave(frame):
#     y=np.sin(x + frame/10)
#     line.set_ydata(y)
#     return line
# ani=FuncAnimation(fig,update_wave,frames=200)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# theta = np.linspace(0,2*np.pi,200)
# square = np.array([
#     [-1,-1],
#     [1,-1],
#     [1,1],
#     [-1,1],
#     [-1,-1]
# ])

# fig, ax = plt.subplots()
# line, = ax.plot(square[:,0],square[:,1])
# ax.set_xlim(-2,2)
# ax.set_ylim(-2,2)

# def update_rotation(frame):
#     angle = frame/20
#     rotation_matrix = np.array([
#         [np.cos(angle),-np.sin(angle)], 
#         [np.sin(angle),np.cos(angle)]
#         ])
#     rotated = square @ rotation_matrix
#     line.set_data(rotated[:,0],rotated[:,1])
#     return line
# ani = FuncAnimation(fig, update_rotation, frames=200, interval=30)
# plt.show()
# x= np.linspace(-5,5,400)
# y= np.linspace(-5,5,400)

# x,y=np.meshgrid(x,y)

# r=np.sqrt(x**2,y**2)

# fig, ax=plt.subplots()
# wave = ax.imshow(np.sin(r),extent=[-5,5,-5,5],origin='lower')

# def update(frame):
#     z =np.sin(r-frame*0.1)
#     wave.set_array(z)
#     return wave

# ani=FuncAnimation(fig,update,frames=300,interval=40)
# plt.show()
 
# points =np.array([
#     [1,2],
#     [3,4],
#     [5,6]
# ])
# print(points)
# print(points)
# diff= points[:,np.newaxis,:] -points[np.newaxis,:,:]
# sq_diff=diff**2

# sum_sq=np.sum(sq_diff,axis=2)
# distance_matrix =np.sqrt(sum_sq)
# print(distance_matrix)
import numpy as np
n=int(input("Enter number of point: "))
point_list=[]

for i in range(n):
    x=int(input(f"Enter x cordinate of point  {i+1}"))
    y=int(input(f"Enter y cordinate of point  {i+1}"))
    point_list.append([x,y])
print(point_list)
point_list=np.array(point_list)
#print(points)
diff= point_list[:,np.newaxis,:] -point_list[np.newaxis,:,:]
sq_diff=diff**2

sum_sq=np.sum(sq_diff,axis=2)
distance_matrix =np.sqrt(sum_sq)
print(distance_matrix)