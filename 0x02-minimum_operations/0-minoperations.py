#!/usr/bin/python3
"""
Solution to minimum operations interview practice question. See README.md
for question specifics.
"""


def minOperations(n):

    current = 1
    starter = 0
    count = 0
    while now < n:
        remainder = n - current
        if (remainder % current == 0):
            starter = current
            current += starter
            count += 2
        else:
            current += starter
            count += 1
    return count
    """
    Calculates the minimum number of operations to go from one 'H' to n 'H's
    if the only available operations are "Copy All" and "Paste"
    """
    