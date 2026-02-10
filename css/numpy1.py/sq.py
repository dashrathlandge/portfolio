import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def square(x, y):
    # implicit square formula
    return np.maximum(np.abs(x), np.abs(y)) - 1

fig, ax = plt.subplots(figsize=(6,6))
ax.set_ylim(1.5, 1.5)
ax.set_xlim(1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

ys = np.linspace(-1.3, 1.3, 500)

line=[]

def update(i):
    y = ys[i]
    x = np.linspace(-1.5, 1.5, 800)

    mask = square(x, y) <= 0

    ax.clear()
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    line, = ax.plot(x[mask], np.full(np.sum(mask), y), linewidth=3)
    return line,

ani = FuncAnimation(
    fig,
    update,
    frames=len(ys),
    interval=2
)

plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # Grid
# x = np.linspace(-1.5, 1.5, 600)
# y = np.linspace(-1.5, 1.5, 600)
# X, Y = np.meshgrid(x, y)

# def square(X, Y):
#     return np.maximum(np.abs(X), np.abs(Y)) - 1

# fig, ax = plt.subplots(figsize=(6,6))
# ax.set_xlim(-1.5, 1.5)
# ax.set_ylim(-1.5, 1.5)
# ax.set_aspect('equal')
# ax.axis('off')

# def update(frame):
#     ax.clear()
#     ax.set_xlim(-1.5, 1.5)
#     ax.set_ylim(-1.5, 1.5)
#     ax.set_aspect('equal')
#     ax.axis('off')

#     scale = frame / 100   # grow animation
#     Z = np.maximum(np.abs(X), np.abs(Y)) - scale
#     ax.contour(X, Y, Z, levels=[0], colors='black', linewidths=3)

# ani = FuncAnimation(fig, update, frames=100, interval=30)

# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# x=np.arange(0,2 * np.pi, 0.1)

# y=np.cos(x)

# plt.plot(x,y)
# plt.xlabel("x,axis")
# plt.xlabel("y,axis")
# plt.show()

# x=np.arange(0,4 * np.pi, 0.1)

# y=np.sin(x)

# plt.plot(x,y)
# plt.xlabel("x,axis")
# plt.xlabel("y,axis")
# plt.show()

# x=np.arange(0,4 * np.pi, 0.1) 

# y=np.tan(x)

# plt.plot(x,y)
# plt.xlabel("x,axis")
# plt.xlabel("y,axis")
# plt.show()