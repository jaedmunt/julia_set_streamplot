import numpy as np
import matplotlib.pyplot as plt
import imageio

def generate_vector_field(x, y, phase):
    """
    Generate a vector field that has a swirling pattern (eddies).
    The phase allows the pattern to change over time.
    """
    u = np.sin(np.pi * x) * np.cos(np.pi * y + phase)
    v = -np.cos(np.pi * x) * np.sin(np.pi * y + phase)
    return u, v

def generate_frames(width, height, num_frames=30):
    x = np.linspace(-3, 3, width)
    y = np.linspace(-3, 3, height)
    X, Y = np.meshgrid(x, y)
    frames = []
    for i in range(num_frames):
        phase = 2 * np.pi * i / num_frames  # Phase changes with each frame to animate the field
        u, v = generate_vector_field(X, Y, phase)

        fig, ax = plt.subplots()
        strm = ax.streamplot(X, Y, u, v, color='b', linewidth=1.5, density=2)
        ax.set_aspect('equal')
        ax.axis('off')

        fig.canvas.draw()
        image = np.frombuffer(fig.canvas.buffer_rgba(), dtype='uint8')
        image = image.reshape(fig.canvas.get_width_height()[::-1] + (4,))
        frames.append(image[..., :3])  # Convert RGBA to RGB
        plt.close(fig)

    return frames

width, height = 400, 400
num_frames = 60  # More frames for a smoother animation
frames = generate_frames(width, height, num_frames)
imageio.mimsave('currents_eddies.gif', frames, fps=20)
print('Done! Image saved successfully.')
