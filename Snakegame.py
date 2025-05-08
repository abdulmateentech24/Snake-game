import turtle
import random

WIDTH = 500
HEIGHT = 500
FOOD_SIZE = 10
DELAY = 100

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def reset():
    global snake, snake_direction, food_pos
    # Snake starts facing down, so position the body to avoid self-collision
    snake = [[0, 60], [0, 40], [0, 20], [0, 0]]
    snake_direction = "down"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    move_snake()

def move_snake():
    global snake_direction

    # Calculate new head position
    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check for collision with itself
    if new_head in snake:
        reset()
    else:
        snake.append(new_head)
        if not food_collision():
            snake.pop(0)  # Only grow if food is eaten

        # Screen wrapping
        if snake[-1][0] > WIDTH / 2:
            snake[-1][0] -= WIDTH
        elif snake[-1][0] < -WIDTH / 2:
            snake[-1][0] += WIDTH
        elif snake[-1][1] > HEIGHT / 2:
            snake[-1][1] -= HEIGHT
        elif snake[-1][1] < -HEIGHT / 2:
            snake[-1][1] += HEIGHT

        pen.clearstamps()

        # Draw snake
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        screen.update()
        turtle.ontimer(move_snake, DELAY)

def food_collision():
    global food_pos
    # Use exact matching for grid-based collision
    if tuple(snake[-1]) == food_pos:
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

def get_random_food_pos():
    x = random.randint(-WIDTH // 2 + FOOD_SIZE, WIDTH // 2 - FOOD_SIZE)
    y = random.randint(-HEIGHT // 2 + FOOD_SIZE, HEIGHT // 2 - FOOD_SIZE)
    # Align to 20x20 grid
    x -= x % 20
    y -= y % 20
    return (x, y)

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

# Setup screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# Pen for drawing snake
pen = turtle.Turtle("square")
pen.penup()
pen.pencolor("yellow")

# Food turtle
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()

# Key bindings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

# Start the game
reset()
turtle.done()
