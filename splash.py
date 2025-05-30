import turtle

def splash_screen(on_start):
    splash_turtle = turtle.Turtle()
    splash_turtle.hideturtle()
    splash_turtle.penup()
    splash_turtle.color("white")

    # Draw the title
    splash_turtle.goto(0, 100)
    splash_turtle.write("Space War", align="center", font=("Arial", 36, "bold"))

    # Draw the instructions
    splash_turtle.goto(0, 50)
    splash_turtle.write("Press 'Enter' to Start", align="center", font=("Arial", 24, "normal"))

    # Define what happens when Enter is pressed
    def start_game():
        splash_turtle.clear()
        on_start()

    turtle.listen()
    turtle.onkey(start_game, "Return")