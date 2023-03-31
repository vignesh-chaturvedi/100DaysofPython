import tkinter as tk
import random

# game constants
WIDTH = 400
HEIGHT = 500
BALL_RADIUS = 10
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 10
BRICK_WIDTH = 50
BRICK_HEIGHT = 20
BRICKS_PER_ROW = 8
NUM_ROWS = 4
GAME_SPEED = 20
BALL_SPEED = 5

# game variables
score = 0
lives = 3
paddle_speed = 20
ball_speed_x = BALL_SPEED
ball_speed_y = BALL_SPEED
game_over = False

# create window
root = tk.Tk()
root.title("Breakout")
root.resizable(0, 0)
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# create game objects
paddle = canvas.create_rectangle(WIDTH/2-PADDLE_WIDTH/2, HEIGHT-PADDLE_HEIGHT-10, WIDTH/2+PADDLE_WIDTH/2, HEIGHT-10, fill="blue")
ball = canvas.create_oval(WIDTH/2-BALL_RADIUS, HEIGHT/2-BALL_RADIUS, WIDTH/2+BALL_RADIUS, HEIGHT/2+BALL_RADIUS, fill="red")
bricks = []
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"]
for i in range(NUM_ROWS):
    color = colors[i]
    for j in range(BRICKS_PER_ROW):
        x = j * BRICK_WIDTH + 50
        y = i * BRICK_HEIGHT + 50
        brick = canvas.create_rectangle(x, y, x+BRICK_WIDTH, y+BRICK_HEIGHT, fill=color)
        bricks.append(brick)
        
# create score and lives display
score_label = tk.Label(root, text="Score: {}".format(score))
score_label.pack()
lives_label = tk.Label(root, text="Lives: {}".format(lives))
lives_label.pack()

# define game functions
def update_score(new_score):
    global score
    score = new_score
    score_label.config(text="Score: {}".format(score))

def update_lives(new_lives):
    global lives
    lives = new_lives
    lives_label.config(text="Lives: {}".format(lives))

def move_paddle(event):
    if not game_over:
        if event.keysym == "Left":
            canvas.move(paddle, -paddle_speed, 0)
        elif event.keysym == "Right":
            canvas.move(paddle, paddle_speed, 0)

def move_ball():
    global ball_speed_x, ball_speed_y, game_over, lives
    canvas.move(ball, ball_speed_x, ball_speed_y)
    ball_pos = canvas.coords(ball)
    paddle_pos = canvas.coords(paddle)
    if ball_pos[0] <= 0 or ball_pos[2] >= WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_pos[1] <= 0:
        ball_speed_y = -ball_speed_y
    if ball_pos[3] >= HEIGHT:
        lives -= 1
        update_lives(lives)
        if lives == 0:
            game_over = True
            canvas.create_text(WIDTH/2, HEIGHT/2, text="Game Over!", font=("Arial", 24))
        else:
            canvas.coords(ball, WIDTH/2-BALL_RADIUS, HEIGHT/2-BALL_RADIUS, WIDTH/2+BALL_RADIUS, HEIGHT/2+BALL_RADIUS)
            ball_speed
