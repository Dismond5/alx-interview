#!/usr/bin/python3
"""0-pascal_triangle"""

def pascal_triangle(n):
    l = []
    if n <= 0:
        return l
    l = [[1]]
    for x in range(1, n):
        temp = [1]
        for y in range(len(l[x - 1]) - 1):
            curr = l[x - 1]
            temp.append(l[x - 1][y] + l[x - 1][y + 1])
        temp.append(1)
        l.append(temp)
    return l
