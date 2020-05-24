"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    player = 1
    stones = 20
    while stones > 0:
        print("There are " + str(stones) + " stones left")
        answer = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones? "))
        while (answer < 1) or (answer > 2):
            answer = int(input("Please enter 1 or 2: "))
        stones -= answer
        print()
        if player == 1:
            player = 2
        else:
            player = 1
    print("Player " + str(player) + " wins!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
