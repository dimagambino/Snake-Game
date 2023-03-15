import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

#Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

#head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("blue")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

#food in the game
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

#setting up the scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center", font=("candara", 24, "bold"))
post = turtle.Turtle()
post.speed(0)
post.shape("circle")
post.color("black")
post.penup()
post.goto(100, 100)
post1 = turtle.Turtle()
post1.speed(0)
post1.shape("circle")
post1.color("black")
post1.penup()
post1.goto(60, 200)
post2 = turtle.Turtle()
post2.speed(0)
post2.shape("circle")
post2.color("black")
post2.penup()
post2.goto(200, 60)

#assigning key directions of the object head
def group():
    if head.direction != "down":
        head.direction = "up"


def godown():
    if head.direction != "up":
        head.direction = "down"


def goleft():
    if head.direction != "right":
        head.direction = "left"


def goright():
    if head.direction != "left":
        head.direction = "right"

#defining a function to set the y coordinates and x coordinates for the object: head, and y and x respective direction
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


wn.listen() #to collect key events method .listen sets focus on the turtle screen

#.onkeypress method binds the first argument (a function with no arguments), to the second argument, a key (a string: key such as a letter "w", or a key symbol such as "space"). for key-events to be registered the screen must have focus, thus the listen method above is necessary
wn.onkeypress(group, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

segments = []

# Main Gameplay
#this ensures that the snake stays within the borders of the game and does not crash into the wall.  If so the snake dies.
while True:
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        food.goto(0, 100)
        post.goto(100, 100)
        post1.goto(60, 200)
        post2.goto(200, 60)
        head.direction = "Stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))

#if the snakes head is near food the food needs to disapear and respawn in a different location.      
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        a = random.randint(-270, 270)
        c = random.randint(-270, 270)
        e = random.randint(-270, 270)
        b = random.randint(-270, 270)
        d = random.randint(-270, 270)
        f = random.randint(-270, 270)

        delay = 0.1
        food.goto(x, y)
        post.goto(a, b)
        post1.goto(c, d)
        post2.goto(e, f)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light blue")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.06
        score += 1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

#Checking for head collisions with body segments and if it happens the snake, object head, must die
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()

    if head.distance(post) < 20:
        time.sleep(1)
        head.goto(0, 0)
        food.goto(0, 100)
        post.goto(100, 100)
        post1.goto(60, 200)
        post2.goto(200, 60)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

    if head.distance(post1) < 20:
        time.sleep(1)
        head.goto(0, 0)
        food.goto(0, 100)
        post.goto(100, 100)
        post1.goto(60, 200)
        post2.goto(200, 60)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

    if head.distance(post2) < 20:
        time.sleep(1)
        head.goto(0, 0)
        food.goto(0, 100)
        post.goto(100, 100)
        post1.goto(60, 200)
        post2.goto(200, 60)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            post.goto(100, 100)
            post1.goto(60, 200)
            post2.goto(200, 60)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(score, high_score), align="center",
                      font=("candara", 24, "bold"))
    time.sleep(delay)

wn.mainloop() #mainloop method applied to screen, this also must be the last statement of a turtle graphics program. event loop startsm starts an infinte loop for the application window