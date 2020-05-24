from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def turn_around():
    """
    Makes Karel turn around.

    Pre-condition: None

    Post-condition: Karel is facing to the opposite direction.
    """
    turn_left()
    turn_left()


def main():
    """
    Makes Karel put a single beeper at the midpoint of the 1st row.

    Pre-condition: None

    Post-condition: Karel is at the midpoint of the first row facing to the
    opposite direction, and there is a beeper at this midpoint.
    """
    # Start moving to the right until reaching the wall.
    # And count how many steps it took to reach the wall.
    count = 0
    while front_is_clear():
        move()
        count += 1

    # Divide step count by 2 to find how many step we need to move back.
    midpoint = count // 2

    # Turn around and move back half of the steps we passed so far.
    turn_around()
    for _ in range(midpoint):
        move()

    # Finally, put a beeper.
    put_beeper()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
