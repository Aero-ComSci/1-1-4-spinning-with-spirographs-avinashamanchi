# 1.1.4 Spinning with Spirographs

# Project 1: Compare and contrast zero-iteration conditions and infinite loops.

# Project 2: A link to your code where you solve the following problem. Take the screen size of 800px. Create code or algorithm that always places the object(s), up to 5, in the center an equal distance from one another and from the edges of the screen.

# Project 3: Concentric Squares -- Add a screenshot of your result and the code to create it on your repo. Objective: Write a Python program using the turtle module to draw a pattern of concentric squares. The pattern should be created using nested loops.

This Python script uses the `turtle` module to draw concentric squares with different colors. The colors are defined using RGB tuples and converted to hexadecimal format for Turtle graphics.

## Code

```python
import turtle

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

def draw_square(turtle_obj, size):
    for _ in range(4):
        turtle_obj.forward(size)
        turtle_obj.right(90)

def draw_concentric_squares_with_colors(num_squares, colors):
    screen = turtle.Screen()
    screen.setup(width=800, height=800)  
    screen.bgcolor("white") 
    
    turtle_obj = turtle.Turtle()
    turtle_obj.speed(0) 
    turtle_obj.hideturtle()
    
    turtle_obj.width(5) 
    
    size = 20 
    num_colors = len(colors)
    
    for i in range(num_squares):
        turtle_obj.penup()
        turtle_obj.goto(-size / 2, size / 2)
        turtle_obj.pendown()
        
        color = rgb_to_hex(colors[i % num_colors])
        turtle_obj.color(color)
        
        draw_square(turtle_obj, size)
        
        size += 20  

    screen.mainloop()  

colors = [
    (255, 0, 0),   
    (0, 255, 0),    
    (0, 0, 255),    
    (0, 255, 255),  
    (255, 0, 255),  
    (255, 255, 0),  
    (255, 165, 0),  
    (128, 0, 128),  
    (0, 128, 128),  
    (128, 128, 128) 
]

draw_concentric_squares_with_colors(10, colors)

draw_concentric_squares_with_colors(10, colors)
```
## What the Code Does

1. **Setup the Drawing Environment**:
   - Creates a window of 800x800 pixels.
   - Sets the background color to white.
   - Initializes a `Turtle` module for drawing.

2. **Drawing Concentric Squares**:
   - Draws multiple squares, each larger than the previous one.
   - Centers each square on the screen by positioning the turtle before drawing.
   - Colors each square differently from a defined list of colors which they all cycle through these colors for each square.

3. **Customization**:
   - Uses a thick pen width to draw the squares.
   - Increases the size of each successive square by 20 pixels.
   - Colors are specified in RGB format and converted to hexadecimal.

This script showcases how to use the `turtle` module for creating colorful, concentric patterns and is a great example of programmatic drawing in Python.




