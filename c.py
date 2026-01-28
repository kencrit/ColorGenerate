import numpy as np

def gradient_2colors(c1, c2, n):
    """Interpolate between two RGB tuples over n steps."""
    c1 = np.array(c1)
    c2 = np.array(c2)
    steps = np.linspace(0, 1, n)
    gradient = [tuple((c1 * (1 - s) + c2 * s).astype(int)) for s in steps]
    return gradient

# Example: red → blue gradient, 10 steps
red = (255, 0, 0)
blue = (0, 0, 255)
grad = gradient_2colors(red, blue, 10)

print(grad)
