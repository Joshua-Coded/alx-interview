#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    '''calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    Returns: Integer
        if n is impossible to achieve, return 0
    '''
    chars = 1  # how many chars in the file
    start = 0  # how many H's copied
    count = 0  # operations counter

    while chars < n:
        # if the clipboard is empty, copy all the characters in the file
        if start == 0:
            # copyall
            start = chars
            # increment the operations counter
            count += 1

        # if nothing has been pasted yet
        if chars == 1:
            # paste
            chars += start
            # increment the operations counter
            counter += 1
            # continue to the next loop
            continue

        remaining = n - chars  # remaining chars to Paste
        # check if is impossible by checking if the clipboard
        # has more than what is required to reach the number
        # which also means num of chars in file is equal
        # or more than in the clipboard.
        # in either situations, it's impossible to achieve n of chars
        if remaining < start:
            return 0

        # if can't be devided
        if remaining % chars != 0:
            # paste current clipboard
            chars += start
            # increment the operations counter
            count += 1
        else:
            # copyall
            start = chars
            # paste
            chars += start
            # increment the operations counter
            count += 2

    # if got the desired result
    if chars == n:
        return count
    else:
        return 0