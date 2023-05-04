#!/usr/bin/python3

'''
In a text file, there is a single character H. Your text editor can execute only two operations in a file: copy All and paste. Given a number n, write a method that calculate the fewest number of operations needed to result in exactly n H charcter in the file. 
'''


def minOperations(n):
    if n < 1:
        return 0

    op = 0, fact = 2, prod = n

    while fact <= prod:
        while prod % fact == 0:
            op += fact
            prod /= fact
        fact += 1

    if op == 0:
        return n
    return op
