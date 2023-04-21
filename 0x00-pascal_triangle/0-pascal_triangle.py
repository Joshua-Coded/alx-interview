#!/usr/bin/python3

def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the pascal triangle"""
    if n <= 0:
        return list()

    empty_list = list([1])

    for i in range(1, n):
        row = list([1])

        for j in range(1, i):
            row.append(empty_list[i-1][j-1] + empty_list[i-1][j])
        row.append(1)
        empty_list.append(row)

    return empty_list
