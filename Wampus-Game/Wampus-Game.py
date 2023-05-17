import numpy as np
import math

dim = (10, 10)
map = np.zeros(dim)
print(map)

# start path mark as one
start = [0, 0]
map[start[0]][start[1]] = 1
# end path mark as 1000
end = [9, 9]
map[end[0]][end[1]] = 1000
# create barrier
map[1][2] = -1
map[2][2] = -1
map[3][2] = -1
map[0][4] = -1
map[4][2] = -1
print(map)

"""A*"""

# calculate heuristic value
h = np.zeros(dim)
g = np.zeros(dim)
print(h)
for i in range(dim[0]):
    for j in range(dim[1]):
        dist = math.sqrt(((end[0] - i) ** 2) + ((end[1] - j) ** 2))
        h[i][j] = dist
        g[i][j] = math.inf
print(g)

list1 = []  # open list
list2 = []  # close list
cost1 = math.inf  # cost l1
cost2 = []  # cost list2

# main
list1.append(start)
list2.append(list1[0])
cost2.append(0)
g[start[0]][start[1]] = 0
xi = start[0]
xj = start[1]
t = 1
flag = True
while flag:
    list1 = []
    cost1 = math.inf
    # 1
    if xi < (dim[0] - 1) and xj < (dim[1] - 1):
        x1 = xi + 1
        x2 = xj + 1
        if map[x1][x2] == 1000:
            list2.append([x1, x2])
            break
        if map[x1][x2] != -1:
            f = g[xi][xj] + 1 + h[x1][x2]
            if f < cost1:
                list1.append([x1, x2])
                cost1 = f

    # 2
    if xi < (dim[0] - 1):
        x1 = xi + 1
        x2 = xj
        if map[x1][x2] == 1000:
            list2.append([x1, x2])
            break
        if map[x1][x2] != -1:
            f = g[xi][xj] + 1 + h[x1][x2]
            if f < cost1:
                list1.append([x1, x2])
                cost1 = f

    # 3
    if xi < (dim[0] - 1) and xj > 0:
        x1 = xi + 1
        x2 = xj - 1
        if map[x1][x2] == 1000:
            list2.append([x1, x2])
            break
        if map[x1][x2] != -1:
            f = g[xi][xj] + 1 + h[x1][x2]
            if f < cost1:
                list1.append([x1, x2])
                cost1 = f

    # 4
    if xj > 0:
        x1 = xi
        x2 = xj - 1
        if map[x1][x2] == 1000:
            list2.append([x1, x2])
            break
        if map[x1][x2] != -1:
            f = g[xi][xj] + 1 + h[x1][x2]
        if f < cost1:
            list1.append([x1, x2])
            cost1 = f

    # 5
    if xi > 0 and xj > 0:
        x1 = xi - 1
        x2 = xj - 1
        if map[x1][x2] == 1000:
            list2.append([x1, x2])
            break
        if map[x1][x2] != -1:
            f = g[xi][xj] + 1 + h[x1][x2]
            if f < cost1:
                list1.append([x1, x2])
                cost1 = f

    # 6
    if xi > 0:
        x1 = xi - 1
        x2 = xj
        if map[x1][x2] == 1000:
            list2.append([x1, x2])
            break
        if map[x1][x2] != -1:
            f = g[xi][xj] + 1 + h[x1][x2]
            if f < cost1:
                list1.append([x1, x2])
                cost1 = f

    # 7
    if xi > 0 and xj < dim[1] - 1:
        x1 = xi - 1
        x2 = xj + 1
        if map[x1][x2] == 1000:
            list2.append([x1, x2])
            break
        if map[x1][x2] != -1:
            f = g[xi][xj] + 1 + h[x1][x2]
            if f < cost1:
                list1.append([x1, x2])
                cost1 = f

    # 8
    if xj < (dim[1] - 1):
        x1 = xi
        x2 = xj + 1
        if map[x1][x2] == 1000:
            list2.append([x1, x2])
            break
        if map[x1][x2] != -1:
            f = g[xi][xj] + 1 + h[x1][x2]
            if f < cost1:
                list1.append([x1, x2])
                cost1 = f
    next = list1.pop()
    x = next[0]
    y = next[1]

    xi = x
    xj = y
    list2.append(next)
    g[x][y] = cost1
    t = t + 1
    map[x][y] = t

print(map)  # see the path on board

print(list2)  # this is path from start point to end
