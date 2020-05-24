from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def turn_right():
    """
    Makes Karel turn right.

    Pre-condition: None

    Post-condition: Karel is facing to the right.
    """
    turn_left()
    turn_left()
    turn_left()


def paint_wall():
    """
    Makes Karel paint one side (wall) of the rectangle (building).

    Pre-condition: None

    Post-condition: Karel is facing to the same direction as before, and every
    step between Karel's old and new positions has had a beeper added to it.
    """
    while left_is_blocked():
        put_beeper()
        move()


def paint_building():
    """
    Makes Karel paint one building (three sides of the rectangle).

    Pre-condition: None

    Post-condition: Karel is positioned at the different coordinate facing to
    the opposite direction, and there are beepers at the three sides of the
    rectangle.
    """
    # Paint the first wall
    paint_wall()

    # Turn left and position (move) at the second wall
    turn_left()
    move()

    # Paint the second wall
    paint_wall()

    # Turn left again and position (move) at the third wall
    turn_left()
    move()

    # Paint the third wall
    paint_wall()


def main():
    """
    Makes Karel paint the exterior of three buildings (rectangles) in its world.

    Pre-condition: None

    Post-condition: Karel is positioned at the different coordinate, but still
    facing to the same direction, and there are beepers at the three sides of
    all three rectangles.
    """
    # Paint the first building entirely (all three sides)
    paint_building()

    # Turn right to position at the first wall of the second building
    turn_right()

    # Paint the second building entirely (all three sides)
    paint_building()

    # Turn right to position at the first wall of the third building
    turn_right()

    # Paint the third building entirely (all three sides)
    paint_building()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
