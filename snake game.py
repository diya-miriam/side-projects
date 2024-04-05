import turtle
import random
import time

# Initialize screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.tracer(0)

# White boundary
boundary = turtle.Turtle()
boundary.speed(0)
boundary.color("white")
boundary.penup()
boundary.goto(-300, 300)
boundary.pendown()
for _ in range(4):
    boundary.forward(600)
    boundary.right(90)
boundary.hideturtle()

# Snake head
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Snake segments
segments = []

# Food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("red")
fruit.penup()
fruit.goto(0, 100)

# Score
score = 0
delay = 0.1

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

# Functions to move the snake
def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    elif snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    elif snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    elif snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Main game loop
while True:
    screen.update()

    # Move the snake
    move()

    # Check for collision with food
    if snake.distance(fruit) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        fruit.goto(x, y)

        # Add a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Increase score and update score display
        score += 10
        score_display.clear()
        score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

    # Check for collision with boundary
    if (
        snake.xcor() > 280
        or snake.xcor() < -280
        or snake.ycor() > 280
        or snake.ycor() < -280
    ):
        score_display.clear()
        score_display.goto(0, 0)
        score_display.write(
            "Game Over\nYour Score: {}".format(score),
            align="center",
            font=("Courier", 30, "bold"),
        )
        time.sleep(2)
        snake.goto(0, 0)
        snake.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)  # Move segments off-screen
        segments.clear()
        score = 0
        score_display.clear()
        score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

    time.sleep(delay)

# This line will not be reached as the game loop runs indefinitely
turtle.done()
