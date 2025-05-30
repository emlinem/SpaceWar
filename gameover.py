import turtle

def show_game_over(score):
    gameover_turtle = turtle.Turtle()
    gameover_turtle.hideturtle()
    gameover_turtle.penup()
    gameover_turtle.color("white")

    # Draw the title
    gameover_turtle.goto(0, 100)
    gameover_turtle.write("Game Over", align="center", font=("Arial", 36, "bold"))

    # Show the final score
    gameover_turtle.goto(0, 50)
    gameover_turtle.write(f"Final Score: {score}", align="center", font=("Arial", 24, "normal"))

    # Optionally, instructions to restart or quit
    gameover_turtle.goto(0, 0)
    gameover_turtle.write("Press 'Escape' to Quit", align="center", font=("Arial", 18, "normal"))

    # Add at the end of show_game_over
def quit_game():
    turtle.bye()

    turtle.listen()
    turtle.onkey(quit_game, "Escape")