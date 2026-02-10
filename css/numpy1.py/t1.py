# import numpy as np
# import matplotlib.pyplot as plt

# count=int(input("Enter pixle size:"))
# constant_coeff=int(input("Enter constant value c:"))
# diamond_size=int(input("Enter diamod size:"))
# arr=np.full((count,count),constant_coeff)
# print(arr)

# center =count//2
# half=diamond_size//2

# for i in range(count):
#     for j in range(count):
#         if(i-center)+ (j-count) <=half:
#             arr[i,j]=0

# plt.imshow(arr, cmap='hot')
# plt.show()

# from matplotlib.transforms import interval_contains
# from matplotlib.animation import adjusted_figsize
# import numpy as np 
# import matplotlib.pyplot as plt 
# from matplotlib.animation import FuncAnimation

# arr = np.linspace(0,2*np.pi,1800)

# x = 16*np.sin(arr)
# y = 13*np.cos(arr)-5*np.cos(2*arr)-2*np.cos(3*arr)-np.cos(4*arr)

# fig, ax = plt.subplots(figsize=(6,6))

# ax.set_xlim(-20,20)
# ax.set_ylim(-20,20)

# ax.set_aspect('equal')
# ax.axis('off')

# line, = ax.plot([],[],linewidth=3)

# def update(i):
#     line.set_data(x[:i],y[:i])
#     return line

# ani = FuncAnimation(
#     fig,
#     update,
#     frames=len(x),
#     interval= 2
# ) 
# plt.show()

# arr =np.array ([2,4,5,3,7,8])
# mean=np.mean(arr)
# print("mean",mean)
# min=np.min(arr)
# print("min",min)
# max=np.max(arr)
# print("max",max)
# sum=np.sum(arr)
# print("sum",sum)
# median=np.median(arr)
# print("median",median)
# std=np.std(arr)
# print("std",std)
# var=np.var(arr)
# print("var",var)
# prod=np.prod(arr)
# print("prod",prod)
# arr1=[1,2,3,4,5,6]
# counts=[0]*6
# roll= []
# fig,ax =plt.subplots()
# bar =ax.bar(arr1,counts)
# ax.set_xticks(arr1)
# ax.set_ylim(0,40)
# def update(frame):
#     roll=np.random.choice(arr1)
#     roll.append(roll)
#     counts[roll-1]+=1
#     for bar, counts in zip(bars,counts):
#         bar.set_hight(counts)
#     return bars
# ani=FuncAnimation(fig,update,frames=200,interval=100,repeat=False)
# arr =np.random.choice(arr1,size=1)
# #plt.imshow()
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# arr1=[1,2,3,4,5,6]
# print(arr1)
# counts = [0]*6
# print(counts)
# roll = []
# fig, ax = plt.subplots()
# bars = ax.bar(arr1,counts)
# ax.set_xticks(arr1)
# ax.set_ylim(0,40)

# def update(frame):
#     roll = np.random.choice(arr1)
#     print(roll)
#     print(arr1.index)
#     counts[arr1.index(roll)] +=1
#     print(counts)


#     for bar, count in zip(bars, counts):
#         bar.set_height(count)
#     return bars
# ani = FuncAnimation(fig, update,frames=200,interval=100,repeat=False)
# plt.show()

# arr=[0,1]
# print(arr)
# counts=[0]*2
# print(counts)
# roll=[]
# fig, ax=plt.subplots()
# bars = ax.bar()
# import numpy as np 
# import matplotlib.pyplot as plt 

# no_of_points = int(input("enter no of points:"))

# theta = np.linspace(0,4*np.pi,no_of_points)
# print(theta)

# r = theta

# print(np.cos(theta))
# x = r*np.cos(theta)

# print(np.sin(theta))
# y = r*np.sin(theta)

# noise = np.random.normal(0,0.5,no_of_points)
# print(noise)
# x = x+noise
# y = y+noise

# colors = np.sqrt(x**2 + y**2)
# print(colors)


# plt.scatter(x,y,c=colors)
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# t = np.linspace(0,2*np.pi,1500)
# arr_x = 16*np.sin(t)**3
# arr_y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)

# fig, ax  = plt.subplots(figsize=(6,6))
# ax.set_ylim(-20,20)
# ax.set_xlim(-20,20)

# ax.set_aspect('equal')
# ax.axis('off')

# line, = ax.plot([],[],linewidth=3)

# glow_lines = [
#     ax.plot([],[],linewidth=3,alpha=0.08)[0]
#     for w in range(8,1,-2)
# ]

# def update(frame):
#     scale = 1+0.15*np.sin(frame*0.15)

#     x=arr_x*scale
#     y=arr_y*scale

#     theta = frame*0.03
#     xr= x*np.cos(theta)-y*np.sin(theta)
#     yr= x*np.sin(theta)+y*np.cos(theta)

#     for g in glow_lines:
#         g.set_data(xr,yr)

#     line.set_data(xr,yr)

#     return [line]+glow_lines

# ani = FuncAnimation(
#     fig,update,frames=600,interval=25
# )
# plt.show()

# import numpy as np 
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# def heart(x,y):
#     # implicit heart formula
#     return (x**2+y**2-1)**3-x**2*y**3
#     # return ax.set_ylim(-1.5,1.5)  
# #ax.set_xlim(-1.5,1.5),
# fig, ax = plt.subplots(figsize=(6,6))
# ax.set_ylim(-1.0,50)  
# ax.set_xlim(-1.0,50)
# ax.set_aspect('equal')
# ax.axis('off')

# ys = np.linspace(-1.0,1.0,500)

# line=[]

# def update(i):
#     y = ys[i]
#     x = np.linspace(-2,2,800)

#     mask =heart(x,y)<=0

#     line, =ax.plot(x[mask],np.full(np.sum(mask),y),linewidth=3)

#     return line
# ani = FuncAnimation(
#     fig,
#     update,
#     frames=len(ys),
#     interval=20
# )

# plt.show()

