from collections import defaultdict

def read_input():
    maps = defaultdict(list)
    with open("./day4_input.txt", "r", encoding="utf-8") as input:
        for i, line in enumerate(input):
            row = defaultdict(str)
            rowarray = [char for char in line.rstrip('\n')]
            for j, col in enumerate(rowarray):
                row[j] = col
            maps[i] = row

    return maps

def solve_1():
    map = read_input()
    rolls = 0

    leny = len(map)
    lenx = len(map[0])
    for i in range(0, leny):
        for j in range(0, lenx):
            if map[i][j] != '@':
                continue
            count = 0
            for y in range(-1,2):
                for x in range(-1,2):
                    if y == 0 and x == 0:
                        continue
                    row = map[i+y]
                    if len(row) == 0:
                        continue
                    col = row[j+x]
                    if col == '@':
                        count += 1
            if count < 4:
                rolls += 1

    print(rolls)

def solve_2():
    map = read_input()
    rolls = 0

    leny = len(map)
    lenx = len(map[0])
    while True:
        removed = 0
        for i in range(0, leny):
            for j in range(0, lenx):
                if map[i][j] != '@':
                    continue
                count = 0
                for y in range(-1,2):
                    for x in range(-1,2):
                        if y == 0 and x == 0:
                            continue
                        row = map[i+y]
                        if len(row) == 0:
                            continue
                        col = row[j+x]
                        if col == '@':
                            count += 1
                if count < 4:
                    rolls += 1
                    map[i][j] = '.'
                    removed += 1
        if removed == 0:
            break

    print(rolls)

solve_1()
solve_2()