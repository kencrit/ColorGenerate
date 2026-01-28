# Color Gradient Generator

This small Python project lets you generate **color gradients** between two RGB colors and visualize them either as an image or as a colormap in a plot.

***

## Features

- Interpolate between two RGB colors over a given number of steps.
- Generate a **horizontal gradient image** (left → right).
- Use the gradient as a **colormap** in a `matplotlib` scatter plot.

***

## Requirements

Make sure you have Python 3 installed, then install the required packages:

```bash
pip install matplotlib pillow
```

***

## How to Use

1. **Clone or create the script**

   Save the code below into a file, for example `gradient.py`:

   ```python
   import numpy as np
   import matplotlib.pyplot as plt
   from PIL import Image
   from matplotlib.colors import LinearSegmentedColormap

   def gradient_2colors(c1, c2, n):
       c1 = np.array(c1)
       c2 = np.array(c2)
       steps = np.linspace(0, 1, n)
       gradient = [tuple((c1 * (1 - s) + c2 * s).astype(int)) for s in steps]
       return gradient

   def make_gradient_image(width, height, c1, c2):
       img = Image.new("RGB", (width, height))
       pixels = img.load()
       for x in range(width):
           mix = x / (width - 1) if width > 1 else 0
           r = int(c1 * (1 - mix) + c2 * mix)
           g = int(c1 * (1 - mix) + c2 * mix)
           b = int(c1 * (1 - mix) + c2 * mix)
           for y in range(height):
               pixels[x, y] = (r, g, b)
       return img

   # Example colors (RGB)
   red = (255, 0, 0)
   blue = (0, 0, 255)

   # Print gradient RGB list (10 steps)
   grad_list = gradient_2colors(red, blue, 10)
   print("Gradient RGB list (10 steps):")
   for i, rgb in enumerate(grad_list):
       print(f"  {i}: {rgb}")

   # Create and show gradient image
   width, height = 400, 100
   img = make_gradient_image(width, height, red, blue)
   img.show()
   # Optional: save image
   # img.save("gradient.png")

   # Gradient colormap in matplotlib
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
   ```

2. **Run the script**

   In your terminal:

   ```bash
   python gradient.py
   ```

   - A window will show the **gradient RGB values** in the console.
   - An image viewer will open with a **horizontal red → blue gradient**.
   - A `matplotlib` window will show a **scatter plot** using the gradient colormap.

***

## Customizing the Gradient

- Change the start and end colors:

  ```python
  c1 = (255, 0, 0)   # red
  c2 = (0, 0, 255)   # blue
  ```

- Adjust the image size:

  ```python
  width, height = 600, 80
  ```

- Change the number of steps in the gradient list:

  ```python
  grad_list = gradient_2colors(red, blue, 20)
  ```

***

## License

You can use, modify, and distribute this code freely in your own projects.
