# Creating a Fractal Generator for Mandelbrot and Julia Sets

# Steps:

# 1. Import required libraries for numerical computations and visualization

# 2. Create functions to generate both Mandelbrot and Julia sets

# 3. Use numpy for efficient array operations

# 4. Implement colorization using matplotlib

# 5. Add user interaction to choose between sets and parameters

# 6. Create a visualization window with proper scaling



import numpy as np

import matplotlib.pyplot as plt



def mandelbrot(h, w, max_iter):

    y, x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]

    c = x + y*1j

    
    divtime = max_iter + np.zeros(z.shape, dtype=int)

    

    for i in range(max_iter):

        
        diverge = z*np.conj(z) > 2**2

        div_now = diverge & (divtime == max_iter)

        
        z[diverge] = 2

    

    


def julia(h, w, c, max_iter):

    y, x = np.ogrid[-1.5:1.5:h*1j, -1.5:1.5:w*1j]

    z = x + y*1j

    divtime = max_iter + np.zeros(z.shape, dtype=int)

    

    for i in range(max_iter):

        
        diverge = z*np.conj(z) > 2**2

        div_now = diverge & (divtime == max_iter)

        
        z[diverge] = 2

    

    


def main():

    print("Fractal Generator")

    print("1. Mandelbrot Set")

    print("2. Julia Set")

    choice = input("Choose fractal type (1 or 2): ")

    

    height, width = 1000, 1500

    max_iterations = 100

    

    if choice == "1":

        fractal = mandelbrot(height, width, max_iterations)

        title = "Mandelbrot Set"

    else:

        c = complex(-0.4, 0.6)  # Default Julia set parameter

        fractal = julia(height, width, c, max_iterations)

        title = f"Julia Set (c = {c})"

    

    plt.figure(figsize=(12, 8))

    plt.imshow(fractal, cmap='hot', extent=[-2, 0.8, -1.4, 1.4])

    plt.title(title)

    plt.colorbar(label='Iteration count')

    plt.xlabel('Re(c)')

    plt.ylabel('Im(c)')

    plt.show()



if __name__ == "__main__":

    main()



# This code creates a fractal generator that can produce both Mandelbrot and Julia sets

# The Mandelbrot set is generated for points c where the sequence z_(n+1) = z_n^2 + c remains bounded

# The Julia set is generated for a fixed c value, showing points z where the same sequence remains bounded

# The visualization uses a heat map coloring scheme where different colors represent how quickly points escape

# Users can choose between the two types of fractals through command line input

# The resolution can be adjusted by modifying height and width variables

# The maximum iteration count affects both detail level and computation time