import turtle
from setup import setup_screen, setup_game
from splash import splash_screen
from game_loop import game_loop
from gameover import show_game_over

setup_screen()
game_objects = setup_game()

# Show splash, then start game when Enter is pressed
splash_screen(lambda: game_loop(*game_objects))

turtle.mainloop()