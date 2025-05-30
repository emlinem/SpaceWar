import turtle
import time
import os
import random
from gameover import show_game_over

def game_loop(game, player, missile, enemies, allies, particles):
    # Keyboard bindings
    turtle.onkey(lambda: player.turn_left(), "Left")
    turtle.onkey(lambda: player.turn_right(), "Right")
    turtle.onkey(lambda: player.accelerate(), "Up")
    turtle.onkey(lambda: player.decelerate(), "Down")
    turtle.onkey(lambda: missile.fire(player), "space")
    turtle.listen()

    while True:
        turtle.update()
        time.sleep(0.02)

        player.move()
        missile.move()

        for enemy in enemies:
            enemy.move()
            if player.is_collision(enemy):
                os.system("afplay assets/crash.mp3&")
                enemy.goto(random.randint(-250, 250), random.randint(-250, 250))
                game.lives -= 1
                game.show_status()
            if missile.is_collision(enemy):
                os.system("afplay assets/explosion.mp3&")
                enemy.goto(random.randint(-250, 250), random.randint(-250, 250))
                missile.status = "ready"
                game.score += 100
                game.show_status()
                for particle in particles:
                    particle.explode(missile.xcor(), missile.ycor())
                missile.goto(-1000, -1000)

        for ally in allies:
            ally.move()
            if player.is_collision(ally):
                os.system("afplay assets/crash.mp3&")
                ally.goto(random.randint(-250, 250), random.randint(-250, 250))
                game.lives -= 1
                game.show_status()
            if missile.is_collision(ally):
                os.system("afplay assets/explosion.mp3&")
                ally.goto(random.randint(-250, 250), random.randint(-250, 250))
                missile.status = "ready"
                game.score -= 100
                game.show_status()
                for particle in particles:
                    particle.explode(missile.xcor(), missile.ycor())
                missile.goto(-1000, -1000)

        for particle in particles:
            particle.move()

        if game.lives <= 0:
            turtle.clear()
            show_game_over(game.score)
            break