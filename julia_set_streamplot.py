#python3
import numpy as np
import matplotlib.pyplot as plt
import imageio

def julia_set(width, height, x_min, x_max, y_min, y_max, c, max_iter=256):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    for i in range(max_iter):
        Z = Z**2 + c
    return Z

def generate_frames(Z, width, height, num_frames=30):
    frames = []
    for i in range(num_frames):
        fig, ax = plt.subplots()
        ax.streamplot(X, Y, np.real(Z), np.imag(Z))
        ax.set_aspect('equal')
        plt.axis('off')

        fig.canvas.draw()
        image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
        image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        frames.append(image)
        plt.close(fig)

    return frames

width, height = 800, 600
x_min, x_max = -2, 2
y_min, y_max = -1.5, 1.5
c = complex(-0.7, 0.27015)
Z = julia_set(width, height, x_min, x_max, y_min, y_max, c)
frames = generate_frames(Z, width, height)
imageio.mimsave('julia_set.gif', frames, fps=10)
