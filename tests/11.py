# Creating a Random Pattern Generator for Wallpapers/Textures

# The idea is to create various geometric shapes and patterns with random colors

# Steps:

# 1. Set up PIL for image creation

# 2. Create functions for different patterns (circles, lines, squares)

# 3. Generate random colors

# 4. Combine patterns with random positioning

# 5. Save the final image








def random_color():

    """Generate a random RGB color"""
    
    return (random.randint(0, 255), 
            
            random.randint(0, 255), 

            random.randint(0, 255))



def draw_circles(draw, width, height):

    """Draw random circles on the image"""
    
    for _ in range(random.randint(10, 30)):

        x = random.randint(0, width)

        y = random.randint(0, height)

        radius = random.randint(20, 100)

        draw.ellipse([x-radius, y-radius, x+radius, y+radius], 
                     
                     fill=random_color(), 

                     outline=random_color())



def draw_lines(draw, width, height):

    """Draw random lines on the image"""
    
    for _ in range(random.randint(10, 30)):

        start_x = random.randint(0, width)

        start_y = random.randint(0, height)

        end_x = random.randint(0, width)

        end_y = random.randint(0, height)

        width_line = random.randint(1, 5)

        draw.line([start_x, start_y, end_x, end_y], 
                  
                 fill=random_color(), 

                 width=width_line)



def draw_squares(draw, width, height):

    """Draw random squares on the image"""
    
    for _ in range(random.randint(10, 30)):

        x = random.randint(0, width)

        y = random.randint(0, height)

        size = random.randint(20, 100)

        draw.rectangle([x, y, x+size, y+size], 
                       
                      fill=random_color(), 

                      outline=random_color())



def create_pattern(width=1920, height=1080):

    """Create a random pattern with the specified dimensions"""
    
    # Create a new image with white background

    image = Image.new('RGB', (width, height), 'white')

    draw = ImageDraw.Draw(image)

    

    # Draw different patterns

    pattern_funcs = [draw_circles, draw_lines, draw_squares]

    for func in pattern_funcs:

        if random.random() > 0.3:  # 70% chance to include each pattern

            func(draw, width, height)

    

    


# Generate and save the pattern

if __name__ == "__main__":

    pattern = create_pattern()

    pattern.save("random_pattern.png")

    print("Pattern generated and saved as 'random_pattern.png'")



# This code creates a random pattern generator that:

# - Creates patterns at 1920x1080 resolution (default)

# - Uses random circles, lines, and squares

# - Generates random colors for each shape

# - Has a 70% chance to include each type of pattern

# - Saves the result as a PNG file

# You can modify the dimensions by calling create_pattern(width, height)