from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def turn_around():
    """
    Makes Karel turn around.

    Pre-condition: None

    Post-condition: Karel is facing to the opposite direction.
    """
    turn_left()
    turn_left()


def repair_column():
    """
    Makes Karel replace the missing stones in a single column of the quad with
    the beepers.

    Pre-condition: None

    Post-condition: Karel is back at its original position facing to the same
    direction as before, and the missing stones in the column are replaced by
    the beepers.
    """
    # Turn left to start climbing up the column
    turn_left()

    # Keep moving up until the top of the column
    # At each step, check if there is a beeper. If not, put a beeper.
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()

    # At the very last step, check if there is a beeper again.
    # If not, put a beeper there as well.
    if no_beepers_present():
        put_beeper()

    # After reaching the top of the column, turn around.
    turn_around()

    # And move back to the bottom of the column.
    while front_is_clear():
        move()

    # Finally, turn left to face to the same direction as before.
    turn_left()


def repair_next_column():
    """
    Makes Karel move to the next column and replace the missing stones in that
    column with the beepers.

    Pre-condition: Karel repaired the column where it is standing.

    Post-condition: Karel is at the bottom of the column facing to the same
    direction as before, and the missing stones in the column are replaced by
    the beepers.
    """
    # Move 4 step to reach the next column
    for _ in range(4):
        move()

    # Start repairing the column
    repair_column()


def main():
    """
    Makes Karel repair the columns of the Main Quad.

    Pre-condition: None

    Post-condition: Karel is at the bottom of the very last column facing to the
    same direction as before, and the missing stones in all columns are replaced
    by the beepers.
    """
    # Repair the first column
    repair_column()

    # Start moving to the right until reaching the wall.
    # And repair all the columns along the way.
    while front_is_clear():
        repair_next_column()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
