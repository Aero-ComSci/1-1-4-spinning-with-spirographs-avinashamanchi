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
