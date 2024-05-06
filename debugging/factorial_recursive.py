#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculate the factorial of a given number recursively.

    Parameters:
    - n: Integer representing the number whose factorial is to be calculated.

    Returns:
    Integer: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Extract the command line argument, calculate its factorial, and print the result
f = factorial(int(sys.argv[1]))
print(f)
