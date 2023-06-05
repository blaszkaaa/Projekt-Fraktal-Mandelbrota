import numpy as np
import matplotlib.pyplot as plt

def generate_fractal(height, width, max_iter):
    # Inicjalizacja tablicy pikseli jako czarnych
    image = np.zeros((height, width))

    # Utworzenie siatki punktów w płaszczyźnie zespolonej
    y, x = np.ogrid[-2:2:height*1j, -2.5:1.5:width*1j]

    # Inicjalizacja tablicy zespolonej dla każdego piksela na siatce
    c = x + y * 1j

    # Inicjalizacja tablicy iteracji
    z = np.zeros_like(c)

    for i in range(max_iter):
        # Obliczanie kolejnych iteracji wzoru z = z^2 + c
        z = z**2 + c

        # Warunek stopu: wartość bezwzględna z większa niż 2
        mask = np.abs(z) < 2

        # Aktualizacja tablicy obrazu tylko dla pikseli, które nie spełniają warunku stopu
        image += mask

    return image

def plot_fractal(image):
    plt.figure(figsize=(10, 10))
    plt.imshow(image, cmap='hot', extent=[-2.5, 1.5, -2, 2])
    plt.colorbar(label='Iterations')
    plt.title('Mandelbrot Fractal')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.show()

def main():
    height = 800
    width = 800
    max_iter = 100

    fractal_image = generate_fractal(height, width, max_iter)
    plot_fractal(fractal_image)

if __name__ == "__main__":
    main()
