#!/usr/bin/python3
# This line is called a shebang. It indicates that the script should be run using the Python 3 interpreter.

import sys
# The 'sys' module provides access to some variables and functions that interact with the Python runtime environment.
# Specifically, 'sys.argv' will be used to retrieve command-line arguments.

def factorial(n):
    # This function calculates the factorial of a given number 'n' using recursion.
    # A factorial is the product of an integer and all the integers below it, e.g., factorial(5) = 5 * 4 * 3 * 2 * 1.

    if n == 0:
        return 1
        # The base case: factorial(0) is defined to be 1.
    else:
        return n * factorial(n-1)
        # The recursive case: factorial(n) = n * factorial(n-1).
        # This keeps calling itself with smaller values of 'n' until it reaches the base case.

# The following line retrieves the first command-line argument provided by the user and converts it to an integer.
# This value is then passed to the 'factorial' function to compute the factorial of that number.
f = factorial(int(sys.argv[1]))

# Finally, the result of the factorial calculation is printed to the console.
print(f)
