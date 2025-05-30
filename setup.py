import turtle

def setup_screen():
    turtle.fd(0)
    turtle.speed(0)
    turtle.bgcolor("black")
    turtle.title("Space War")
    turtle.bgpic("assets/starfield.gif")
    turtle.ht()
    turtle.setundobuffer(1)
    turtle.tracer(0)

import random
from classes import Player, Missile, Enemy, Ally, Particle, Game

def setup_game():
    game = Game()
    game.draw_border()
    game.show_status()

    player = Player("triangle", "white", 0, 0)
    missile = Missile("triangle", "yellow", 0, 0)

    enemies = [Enemy("circle", "red", random.randint(-290, 290), random.randint(-290, 290)) for _ in range(6)]
    allies = [Ally("square", "blue", random.randint(-290, 290), random.randint(-290, 290)) for _ in range(6)]
    particles = [Particle("circle", "orange", 0, 0) for _ in range(20)]

    return game, player, missile, enemies, allies, particles