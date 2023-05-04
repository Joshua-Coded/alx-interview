#!/usr/bin/python3
"""
Solution to minimum operations interview practice question. See README.md
for question specifics.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations to go from one 'H' to n 'H's
    if the only available operations are "Copy All" and "Paste"
    """
    
    if n < 1:
        return 0

    op = 0
    fact = 2
    prod = n
    
    while fact <= prod:
        while prod % fact == 0:
            op += fact
            prod /= fact
        fact += 1

    if op == 0:
        return n

    return op