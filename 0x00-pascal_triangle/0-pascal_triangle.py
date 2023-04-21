#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the pascal triangle"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle


"""This implementation uses a nested loop to
build up the Pascal's triangle row by row.
The outer loop runs from 1 to n-1
(inclusive) to generate each row, and the inner loop
generates each element of the row based on the
values in the previous row. The triangle
is represented as a list of lists of integers,
with each inner list representing a row of the triangle."""
