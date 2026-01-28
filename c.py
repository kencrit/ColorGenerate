import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 1. Function to interpolate between two RGB colors
def gradient_2colors(c1, c2, n):
    c1 = np.array(c1)
    c2 = np.array(c2)
    steps = np.linspace(0, 1, n)
    gradient = [tuple((c1 * (1 - s) + c2 * s).astype(int)) for s in steps]
    return gradient

# 2. Make a horizontal gradient image with PIL
def make_gradient_image(width, height, c1, c2):
    img = Image.new("RGB", (width, height))
    pixels = img.load()
    for x in range(width):
        mix = x / (width - 1) if width > 1 else 0
        r = int(c1[0] * (1 - mix) + c2[0] * mix)
        g = int(c1[1] * (1 - mix) + c2[1] * mix)
        b = int(c1[2] * (1 - mix) + c2[2] * mix)
        for y in range(height):
            pixels[x, y] = (r, g, b)
    return img

# 3. Example usage

# Define colors (RGB)
red = (255, 0, 0)
blue = (0, 0, 255)

# Generate gradient list (10 steps, for debugging)
grad_list = gradient_2colors(red, blue, 10)
print("Gradient RGB list (10 steps):")
for i, rgb in enumerate(grad_list):
    print(f"  {i}: {rgb}")

# Create and show a gradient image
width, height = 400, 100
img = make_gradient_image(width, height, red, blue)
img.show()  # Opens in default image viewer
# Optional: save to file
# img.save("gradient.png")

# 4. Gradient colormap in matplotlib (optional plot)
from matplotlib.colors import LinearSegmentedColormap

colors = ["red", "blue"]
n_bins = 256
cmap = LinearSegmentedColormap.from_list("red_blue", colors, N=n_bins)

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(8, 4))
plt.scatter(x, y, c=x, cmap=cmap, s=50)
plt.colorbar(label="X value")
plt.title("Color gradient using colormap")
plt.show()
