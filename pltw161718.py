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
