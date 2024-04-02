import numpy as np
import matplotlib.pyplot as plt
import imageio

def julia_set(width, height, x_min, x_max, y_min, y_max, c, max_iter=256):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    final_iter = np.zeros(Z.shape)
    for i in range(max_iter):
        Z = np.where(np.abs(Z) > 2, Z, Z**2 + c)  # Keep Z unchanged if it escapes
        final_iter[np.abs(Z) < 2] = i
    return final_iter

def generate_frames(data, width, height, num_frames=30):
    X, Y = np.meshgrid(np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height))
    frames = []
    for i in range(num_frames):
        fig, ax = plt.subplots()
        ax.imshow(data, extent=[x_min, x_max, y_min, y_max], origin='lower', cmap='twilight')
        ax.axis('off')

        fig.canvas.draw()
        image = np.frombuffer(fig.canvas.buffer_rgba(), dtype='uint8')
        image = image.reshape(fig.canvas.get_width_height()[::-1] + (4,))  # RGBA has 4 channels
        frames.append(image[..., :3])  # Convert RGBA to RGB by dropping the alpha channel
        plt.close(fig)

    return frames

width, height = 800, 600
x_min, x_max = -2, 2
y_min, y_max = -1.5, 1.5
c = complex(-0.7, 0.27015)
data = julia_set(width, height, x_min, x_max, y_min, y_max, c)
frames = generate_frames(data, width, height)
imageio.mimsave('julia_set.gif', frames, fps=10)
print('Done! Image saved successfully.')
