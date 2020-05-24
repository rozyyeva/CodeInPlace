"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

MIN_RANDOM = 10
MAX_RANDOM = 99


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    count = 0

    while count != 3:
        a = random.randint(MIN_RANDOM, MAX_RANDOM)
        b = random.randint(MIN_RANDOM, MAX_RANDOM)
        result = a + b

        print("What is " + str(a) + " + " + str(b) + "?")
        answer = int(input("Your answer: "))

        if answer == result:
            count += 1
            print("Correct! You`ve gotten " + str(count) + " correct in a row")
        else:
            count = 0
            print("Incorrect. The expected answer is " + str(result))

    print("Congratulations! You mastered addition.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
