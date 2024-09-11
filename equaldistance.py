import turtle

def draw_object(turtle_obj, x, y):
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.begin_fill()
    turtle_obj.circle(20)  
    turtle_obj.end_fill()

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)  
    screen.title("Centered Objects")

    my_turtle = turtle.Turtle()
    my_turtle.color("blue")

    while True:
        try:
            num_objects = int(screen.textinput("Number of Objects", "Enter the number of objects you would like to draw (1-5):"))
            if 1 <= num_objects <= 5:
                break
            else:
                screen.textinput("Invalid Input", "Please enter a number between 1 and 5.")
        except ValueError:
            screen.textinput("Invalid Input", "Please enter a valid integer.")

    total_width = 800  
    object_diameter = 40  
    space_between = (total_width - (num_objects * object_diameter)) / (num_objects + 1)

    for i in range(num_objects):
        x = -400 + space_between * (i + 1) + object_diameter * i
        y = 0 
        draw_object(my_turtle, x, y)

   
    my_turtle.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
