""" Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird

Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird. """

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    # Read an integer from the user

    # Check if the number is odd
    if n % 2 == 1:
        print("Weird")
    else:
        # Check if the number is even and in the inclusive range of 2 to 5
        if n >= 2 and n <= 5:
            print("Not Weird")
        # Check if the number is even and in the inclusive range of 6 to 20
        elif n >= 6 and n <= 20:
            print("Weird")
        # Check if the number is even and greater than 20
        else:
            print("Not Weird")
