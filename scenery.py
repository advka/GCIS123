import turtle

def cake():
    # Setup turtle screen
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    # Setup turtle
    pen = turtle.Turtle()
    pen.speed(3)

    # Function to draw a rectangle
    def draw_rectangle(width, height, color):
        pen.fillcolor(color)
        pen.begin_fill()
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
        pen.end_fill()

    # Draw the table (top)
    pen.penup()
    pen.goto(-150, -150)
    pen.pendown()
    draw_rectangle(300, 20, "brown")
    
    # Draw the table legs
    # First leg
    pen.penup()
    pen.goto(-140, -150)
    pen.pendown()
    draw_rectangle(20, -100, "brown")

    # Second leg
    pen.penup()
    pen.goto(120, -150)
    pen.pendown()
    draw_rectangle(20, -100, "brown")

    # Draw the first tier of the cake (bottom)
    pen.penup()
    pen.goto(-100, -130)
    pen.pendown()
    draw_rectangle(200, 80, "pink")
    
    # Draw the second tier of the cake (middle)
    pen.penup()
    pen.goto(-70, -50)
    pen.pendown()
    draw_rectangle(140, 60, "lightblue")
    
    # Draw the third tier of the cake (top)
    pen.penup()
    pen.goto(-40, 10)
    pen.pendown()
    draw_rectangle(80, 40, "lightgreen")
    
    # Draw the first candle on the top tier
    pen.penup()
    pen.goto(-25, 50)
    pen.pendown()
    draw_rectangle(10, 40, "yellow")
    
    # Draw the second candle on the top tier
    pen.penup()
    pen.goto(5, 50)
    pen.pendown()
    draw_rectangle(10, 40, "orange")

    
    # Draw candle flames
    pen.penup()
    pen.goto(-20, 90)
    pen.pendown()
    pen.fillcolor("red")
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()

    pen.penup()
    pen.goto(10, 90)
    pen.pendown()
    pen.fillcolor("red")
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()


    # Hide the turtle
    pen.hideturtle()

# Run the function to draw the cake with candles
cake()

# Keep the window open until clicked
turtle.done()
