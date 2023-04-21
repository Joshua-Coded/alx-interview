def pascal_triangle(n):
    if n <= 0:
        return list()
    empty_list = list([1])
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(empty_list[i-1] + empty_list[i-1][j])
            row.append(i)
            empty_list.append(row)
        return empty_list
