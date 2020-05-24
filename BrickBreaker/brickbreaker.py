"""
File: brickbreaker.py
----------------
Python based desktop app that plays a classic Brick Breaker game.
"""

import tkinter
import time
import random

# How big is the playing area?
CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 800     # Height of drawing canvas in pixels

# Constants for the bricks
N_ROWS = 8              # How many rows of bricks are there?
N_COLS = 10             # How many columns of bricks are there?
SPACING = 5             # How much space is there between each brick?
BRICK_START_Y = 50      # The y coordinate of the top-most brick
BRICK_HEIGHT = 20       # How many pixels high is each brick
BRICK_WIDTH = (CANVAS_WIDTH - (N_COLS + 1) * SPACING) // N_COLS

# Constants for the ball
BALL_SIZE = 40
BALL_START_X = (CANVAS_WIDTH // 2) - (BALL_SIZE // 2)
BALL_START_Y = (CANVAS_HEIGHT // 2) - (BALL_SIZE // 2)

# Constants for the paddle
PADDLE_WIDTH = 80
PADDLE_X = (CANVAS_WIDTH // 2) - (PADDLE_WIDTH // 2)
PADDLE_Y = CANVAS_HEIGHT - 40

# Constants for the colors
RAINBOW_COLORS = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet"
]
N_ROWS_PER_COLOR = 2


def main():
    """
    Main function that includes all other function calls within entire program.
    """

    # Make the canvas with the given CANVAS_WIDTH and CANVAS_HEIGHT constants.
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, "Brick Breaker")

    # Preload 2 images that will be used in the application
    gemstone = tkinter.PhotoImage(file="images/gemstone.png").subsample(12, 16)
    heart_image = tkinter.PhotoImage(file="images/heart.png").subsample(32, 32)

    # Step 1: Create the bricks with some gemstones at random rows and columns.
    bricks = create_bricks(canvas, gemstone)

    # Step 2: Create the ball and move it to the particular location.
    ball = canvas.create_oval(
        BALL_START_X,
        BALL_START_Y,
        BALL_START_X + BALL_SIZE,
        BALL_START_Y + BALL_SIZE,
        fill="black",
        outline="red",
        tags="ball"
    )
    canvas.moveto(ball, BALL_START_X, BALL_START_X)

    # Step 3: Create the paddle.
    paddle = canvas.create_rectangle(
        PADDLE_X,
        PADDLE_Y,
        PADDLE_X + PADDLE_WIDTH,
        CANVAS_HEIGHT - 20,
        fill="brown",
        outline="brown",
        tags="paddle"
    )

    # Step 4: Create 3 small heart images at the top left corner of the canvas.
    # These hearts indicate the number of lives (aka. turns) left so far.
    lives = []
    for i in range(3):
        lives.append(
            canvas.create_image(
                SPACING * 4 + i * (32 + SPACING),
                SPACING * 4,
                image=heart_image
            )
        )

    # Step 4: Create a button which starts the game upon press.
    start_command = tkinter.IntVar()
    start_button = tkinter.Button(
        canvas,
        text="START",
        font="Times 16 bold",
        height=2,
        width=10,
        command=lambda: start_command.set(1)
    )

    # Step 5: Use "while" loop to keep track of the game progress.
    # For example, if "lives" list becomes empty, the game is lost.
    # On the other hand, if "brick" list becomes empty, the game is won.

    while len(bricks) and len(lives):
        # Place the "start" button at somewhere closer to the canvas center.
        start_button.place(relx=.5, rely=.6, anchor="c")
        # Wait for the "start" button press.
        start_button.wait_variable(start_command)
        # After the "start" button is pressed, make the button disappear and
        # start moving the ball.
        start_button.place_forget()
        canvas.moveto(ball, BALL_START_X, BALL_START_X)
        # All the actions are happening in this "start_game" function.
        start_game(canvas, paddle, ball, bricks, lives, start_command)

    # Display different message depending on the win or lose situation.
    result_text = "You "
    if len(bricks):
        result_text += "Lost :("
        fill_color = "red"
    else:
        result_text += "Won :)"
        fill_color = "green"
        canvas.delete("ball")

    canvas.create_text(
        CANVAS_WIDTH // 2,
        (CANVAS_HEIGHT // 2) - BALL_SIZE,
        fill=fill_color,
        font="Times 20 bold",
        text=result_text
    )

    # Main loop
    canvas.mainloop()


def start_game(canvas, paddle, ball, bricks, lives, start_command):
    """
    This function is responsible for all the actions in the game.
    """

    # Calculate the current width of the paddle
    paddle_curr_width = get_right_x(canvas, paddle) - get_left_x(canvas, paddle)

    # Pick a direction for the ball movement. 35° seems to be a good pick.
    dx = 10
    dy = 7

    # Main loop for the actions.
    while True:
        # Get the current mouse location.
        mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()

        # Adjust the x location of the paddle depending on where the mouse is.
        # For example, if the mouse is outside of canvas boundary, keep the
        # paddle right next to wall.
        if mouse_x < (paddle_curr_width // 2):
            paddle_next_x = 0
        elif mouse_x > (CANVAS_WIDTH - paddle_curr_width):
            paddle_next_x = CANVAS_WIDTH - paddle_curr_width
        else:
            paddle_next_x = mouse_x - (paddle_curr_width // 2)

        # Move the paddle to the adjusted location.
        canvas.moveto(paddle, paddle_next_x, PADDLE_Y)

        # Keep moving the ball at 35 degrees.
        canvas.move(ball, dx, dy)

        # If the ball hits the bottom wall (i.e. misses the paddle),
        # the player loses 1 life (aka. turn).
        if hit_bottom_wall(canvas, ball):
            # Remove 1 of the heart images.
            canvas.delete(lives[-1])
            del lives[-1]
            # Disable "start" command.
            start_command.set(0)
            # And break out from this "while" loop.
            break

        # If the ball hits the paddle or top wall, reverse "y" direction.
        if hit_paddle(canvas, paddle) or hit_top_wall(canvas, ball):
            dy *= -1
            # Fix the bug where the ball appears to be glued to the paddle.
            while hit_paddle(canvas, paddle):
                canvas.move(ball, dx, dy)

        # If the ball hits to the side walls, reverse "x" direction.
        if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
            dx *= -1

        # Now, check if the ball hits the brick.
        # Also, distinguish if it is a brick or gemstone.
        # If the ball hits the gemstone, the paddle width increases.
        brick_id = hit_brick(canvas, ball, bricks)
        if brick_id > 0:
            brick_tags = canvas.gettags(brick_id)
            if "gem" in brick_tags:
                # Add another PADDLE_WIDTH to the paddle's current width.
                paddle_curr_width += PADDLE_WIDTH
                x1, y1, x2, y2 = canvas.coords(paddle)
                # Update the paddle coordinates with the wider width.
                canvas.coords(
                    paddle,
                    x1 - (PADDLE_WIDTH // 2),
                    y1,
                    x2 + (PADDLE_WIDTH // 2),
                    y2
                )
            # Now delete this brick.
            canvas.delete(brick_id)
            bricks.remove(brick_id)
            # Change the direction to downward.
            dy *= -1
            # If no brick left, the game is won. Just break out from this loop.
            if not len(bricks):
                break

        # Redraw canvas.
        canvas.update()

        # Pause so that human eye can see the movement.
        time.sleep(1 / 50)


def create_bricks(canvas, image):
    """
    This function is responsible for creating bricks and gemstones.
    It returns the list of bricks' unique object ids.
    """
    # First, we select 3 random positions where can place the gemstones.
    gem_loc = set()
    while len(gem_loc) < 3:
        row = random.randint(1, N_ROWS - 2)
        col = random.randint(1, N_COLS - 2)
        gem_loc.add((row, col))
    # Now, let's put the bricks with a different rainbow color in every 2 rows.
    bricks = []
    for row in range(N_ROWS):
        color_index = (row // N_ROWS_PER_COLOR) % (N_ROWS - 1)
        fill_color = RAINBOW_COLORS[color_index]
        for col in range(N_COLS):
            y1 = row * (BRICK_HEIGHT + SPACING) + BRICK_START_Y
            x1 = col * (BRICK_WIDTH + SPACING) + SPACING
            if (row, col) in gem_loc:
                bricks.append(
                    canvas.create_image(
                        x1 + (BRICK_WIDTH // 2),
                        y1 + (BRICK_HEIGHT // 2),
                        image=image,
                        tags="gem"
                    )
                )
            else:
                bricks.append(
                    canvas.create_rectangle(
                        x1,
                        y1,
                        x1 + BRICK_WIDTH,
                        y1 + BRICK_HEIGHT,
                        fill=fill_color
                    )
                )
    # Return the list of brick ids.
    return bricks


def hit_paddle(canvas, paddle):
    x1, y1, x2, y2 = canvas.coords(paddle)
    results = canvas.find_overlapping(x1, y1, x2, y2)
    return len(results) > 1


def hit_brick(canvas, ball, bricks):
    """
    This function checks if the ball hits the brick. If a brick is hit, its id
    is returned. Otherwise, -1 is returned to indicate that none of the bricks
    are hit by the ball.
    """
    x1, y1, x2, y2 = canvas.coords(ball)
    results = canvas.find_overlapping(x1, y1, x2, y2)
    for brick_id in results:
        if brick_id in bricks:
            return brick_id
    return -1


def hit_left_wall(canvas, item):
    return get_left_x(canvas, item) <= 0


def hit_top_wall(canvas, item):
    return get_top_y(canvas, item) <= 0


def hit_right_wall(canvas, item):
    return get_right_x(canvas, item) >= CANVAS_WIDTH


def hit_bottom_wall(canvas, item):
    return get_bottom_y(canvas, item) >= CANVAS_HEIGHT


def get_left_x(canvas, item):
    """
    This friendly method returns the x coordinate of the left of an item.
    Recall that canvas.coords(item) returns a list of the items
    bounding box: [x_1, y_1, x_2, y_2]. The element at index 0 is the left-x
    """
    return canvas.coords(item)[0]


def get_top_y(canvas, item):
    """
    This friendly method returns the y coordinate of the top of an item.
    Recall that canvas.coords(item) returns a list of the item
    bounding box: [x_1, y_1, x_2, y_2]. The element at index 1 is the top-y
    """
    return canvas.coords(item)[1]


def get_right_x(canvas, item):
    return canvas.coords(item)[2]


def get_bottom_y(canvas, item):
    return canvas.coords(item)[3]


def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    top.resizable(False, False)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas


if __name__ == '__main__':
    main()
