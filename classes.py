import turtle
import random
import os

class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        #Draw border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, -300)
        self.pen.pendown()

        for side in range(4):
            self.pen.fd(600)
            self.pen.lt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()
    
    def show_status(self):
        self.pen.undo()
        msg = "Score: %s  Lives: %s" % (self.score, self.lives)
        self.pen.penup()
        self.pen.goto(-300, 310)
        self.pen.write(msg, font=("Arial", 16, "normal"))

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)

        self.move_speed = 1

    def move(self):
        self.fd(self.move_speed)

        #Boundary detection
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)
        
        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)
    
    def is_collision(self, other):
        #Check for collision with another sprite
        if (self.xcor() >= (other.xcor() - 20) and
            self.xcor() <= (other.xcor() + 20) and
            self.ycor() >= (other.ycor() - 20) and
            self.ycor() <= (other.ycor() + 20)):
            return True
        else: 
            return False
    

class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
        self.move_speed = 4
        self.lives = 3
    
    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.move_speed += 1

    def decelerate(self):
        self.move_speed -= 1

class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.move_speed = 6
        self.setheading(random.randint(0, 360))  # Random initial direction

class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.move_speed = 6
        self.setheading(random.randint(0, 360))  # Random initial direction

class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
        self.move_speed = 20
        self.status = "ready"
        self.goto(-1000, -1000)  # Start off-screen

    def fire(self, player):
        if self.status == "ready":
            os.system("afplay assets/laser.mp3&")
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"
    
    def move(self):
        if self.xcor() > 290 or self.xcor() < -290 or self.ycor() > 290 or self.ycor() < -290:
            self.goto(-1000, -1000)
            self.status = "ready"
        if self.status == "firing":
            self.fd(self.move_speed)

class Particle(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.goto(-1000, -1000)  # Start off-screen
        self.frame = 0

    def explode(self, startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0, 360))
        self.frame = 1
    
    def move(self):
        if self.frame > 0:
            self.fd(10)
            self.frame += 1
        
        if self.frame > 10:
            self.frame = 0
            self.goto(-1000, -1000)  # Move off-screen after explosion