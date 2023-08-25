import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for i in range(max_iter):
        if abs(z) > 2.0:
            return i
        z = z * z + c
    return max_iter

def create_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    mandelbrot_set = np.zeros((width, height))
    
    for i in range(width):
        for j in range(height):
            mandelbrot_set[i, j] = mandelbrot(x[i] + 1j * y[j], max_iter)
    
    return mandelbrot_set

def plot_mandelbrot(mandelbrot_set, x_min, x_max, y_min, y_max):
    plt.imshow(mandelbrot_set, extent=(x_min, x_max, y_min, y_max))
    plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.xlabel("Real")
    plt.ylabel("Imaginary")
    plt.show()

def main():
    width = 800
    height = 800
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.5, 1.5
    max_iter = 1000
    
    mandelbrot_set = create_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)
    plot_mandelbrot(mandelbrot_set, x_min, x_max, y_min, y_max)

if __name__ == "__main__":
    main()
