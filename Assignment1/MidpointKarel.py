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


def move_to_opposite_corner():
    """
    Makes Karel bounce between two opposite corners while moving their markers
    closer to each other until they overlap (odd number) or become immediate
    neighbors (even number).

    Pre-condition: Karel is at the rightmost corner.

    Post-condition: Karel is at the midpoint, and there is a beeper.
    """
    # First, turn around and remove the existing marker (blue color).
    turn_around()
    paint_corner(BLANK)
    # Then, move for 1 step.
    move()

    # If this new corner has been marked already, Karel found the midpoint.
    if corner_color_is(BLUE):
        # Remove the existing marker
        paint_corner(BLANK)
        # And, put a beeper
        put_beeper()
        # DONE!!!
    else:
        # If the new corner has NOT been marked, mark it
        paint_corner(BLUE)
        # And keep moving until reaching the opposite corner that is marked
        move()
        while corner_color_is(BLANK):
            move()
        # Another marked corner is reached.
        # So, repeat the same action by moving to the opposite corner.
        move_to_opposite_corner()


def main():
    """
    Makes Karel put a single beeper at the midpoint of the 1st row.

    Pre-condition: None

    Post-condition: Karel is at the midpoint of the first row, and there is a
    beeper at this midpoint.
    """
    # If Karel's front is already blocked at the beginning, it must be 1x1 world
    # So, just put a beeper and we are done!
    if front_is_blocked():
        put_beeper()
    else:
        # Mark (paint) the leftmost corner
        paint_corner(BLUE)

        while front_is_clear():
            move()

        # Mark (paint) the rightmost corner
        paint_corner(BLUE)

        # Now, keep bouncing between two corners while marking their positions
        # and shrinking those markers until they overlap (odd number) or become
        # immediate neighbors (even number).
        move_to_opposite_corner()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
