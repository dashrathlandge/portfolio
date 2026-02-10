# import numpy as np
# import matplotlib.pyplot as plt
# img = np.zeros((300, 300, 3), dtype=np.uint8)
# print(img.shape)
# img[150:200,150:200] = [250,250,250]
# img[90:200,90:200] = [0,255,0]

# plt.figure(figsize=(5,5))
# plt.imshow(img)
# plt.axis('off')
# plt.show() 
# # import numpy as np
# import matplotlib.pyplot as plt

# count =int(input("enter pixle size x:")) #200
# constant_coeff =int(input("enter constat vale c:"))
# square_size = int(input("enter square size:"))
# arr= np.full((count,count),constant_coeff)
# print(arr)
# center =count//2
# half = square_size//2
# start= center - half
# end = center + half
# arr[start:end,start:end]=0
# plt.imshow(arr,cmap='hot')
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# fig, ax = plt.subplots(figsize=(6,6))
# ax.set_xlim(-250, 250)
# ax.set_ylim(-250, 250)
# ax.set_aspect('equal')
# ax.axis('off')

# # Square corner points
# square_x = [-200, 1, 1, -1, -1]
# square_y = [-1, -1, 1, 1, -1]

# line, = ax.plot([], [], linewidth=3)

# def update(frame):
#     # Draw square gradually
#     line.set_data(square_x[:frame], square_y[:frame])
#     return line,

# ani = FuncAnimation(
#     fig,
#     update,
#     frames=len(square_x) + 1,
#     interval=500,
#     repeat=False
# )

# plt.show()
# a=np.random.rand(3,3)
# b=np.random.rand(3,3)

# print("a:",a)
# print("b",b)

# result =np.einsum('ij,jk-.ik',a,b)
# print("result:", result)
# #dot product
# #

# a[i] [j]
#ivmp
import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0, 1,500)
print(t)
signal=np.sin(2*np.pi*5*t) + np.sin(2*np.pi*20*t)*0.5
fft= np.fft.fft(signal) #time base
freq =np.fft.fftfreq(len(signal),t[1]-t[0])

plt.plot(freq,np.abs(fft))
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import animation

size=21
center=size//2
fig, ax=plt.subplots()

ax.set_xlim(0,size)
ax.set_ylim(0,size)
ax.set_xticke([])
ax.set_xticke([])

img =ax.show(np.zero((size, size)),animated=True)
def update(frame):
    row,cols=np.indices(size,size)