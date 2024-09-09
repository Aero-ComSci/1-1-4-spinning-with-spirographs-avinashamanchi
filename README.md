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
    
    size_increment = 800 / num_squares
    initial_size = size_increment
    
    num_colors = len(colors)
    
    for i in range(num_squares):
        turtle_obj.penup()
        turtle_obj.goto(-initial_size / 2, initial_size / 2)
        turtle_obj.pendown()
        
        color = rgb_to_hex(colors[i % num_colors])
        turtle_obj.color(color)
        
        draw_square(turtle_obj, initial_size)
        
        initial_size += size_increment

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

draw_concentric_squares_with_colors(20, colors)

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

# Project 4: Clever PLTW activities

## Complete the steps 17, 18 and 19

```python
import turtle as trtl

painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()

while True:
    # Original pattern
    x = -200
    y = 0
    move_x = 1
    move_y = 1

    while (x < 200):
        while (y < 100):
            x = x + move_x
            y = y + move_y
            painter.goto(x, y)
        move_y = -1

        while (y > 0):
            x = x + move_x
            y = y + move_y
            painter.goto(x, y)
        move_y = 1

    # Reset position for the opposite pattern
    painter.penup()
    painter.goto(-200, 0)
    painter.pendown()

    # Opposite pattern
    x = -200
    y = 0
    move_x = 1
    move_y = 1

    while (x < 200):
        while (y > -100):  # Move downwards for the opposite pattern
            x = x + move_x
            y = y + move_y
            painter.goto(x, y)
        move_y = 1

        while (y < 0):  # Move upwards for the opposite pattern
            x = x + move_x
            y = y + move_y
            painter.goto(x, y)
        move_y = -1
        
        while (x < 200):
          while (y > -100):  # Move downwards for the opposite pattern
            x = x + move_x
            y = y + move_y
            painter.goto(x, y)
        move_y = 1
        
        while (y < 0):  # Move upwards for the opposite pattern
            x = x + move_x
            y = y + move_y
            painter.goto(x, y)
        move_y = -1


wn = trtl.Screen()
wn.mainloop()
```
## Project 5: Answer to 21

## Project 6: Insert a screenshot or picture of the algorith you used for your tokenizer on the previous activity.

## Project 7: Give an example of an undecidable problem, attach code.

### Overview

The Halting Problem is a classic example of an undecidable problem. It involves determining whether a given computer program will eventually halt (finish executing) or continue to run forever when provided with a specific input. Alan Turing proved that this problem is undecidable, meaning there is no general algorithm that can solve it for all possible programs and inputs.

### Why It Is Undecidable

The Halting Problem is undecidable because a hypothetical solution to it can lead to contradictions. Specifically, if we had a perfect algorithm to determine whether any given program halts, we could construct a paradoxical program that contradicts itself, demonstrating the impossibility of such an algorithm.

### Example Code

Below is an example code snippet that illustrates the Halting Problem. This code does not solve the Halting Problem but demonstrates why it is undecidable.

```python
def halting_problem_simulator(program, input):
    """
    This function simulates a decision problem for the Halting Problem.
    It is meant to illustrate the problem and does not actually solve it.
    """
    try:
        exec(program)  # Execute the given program code
    except Exception as e:
        print("The program threw an exception, which means it might be in an infinite loop.")

# Example usage
program_code = """
def run():
    while True:
        pass  # Infinite loop

run()
"""

input_data = ""  # Not used in this example

halting_problem_simulator(program_code, input_data)
```
# Why This Example Demonstrates Undecidability
## Undecidability: The provided code does not truly solve the Halting Problem. It merely illustrates that you cannot always determine if a given program (represented as a string) will halt or run forever.

## Practical Example: In real-world scenarios, analyzing the behavior of arbitrary code to decide if it halts is not feasible due to the undecidability of the problem. No universal algorithm can decide halting for all possible programs and inputs.


