def read_input():
    ranges = []
    with open("./day2_input.txt", "r", encoding="utf-8") as input:
        line = input.readline()
        input_ranges = line.strip().rstrip(",").split(",")
        for input_range in input_ranges:
            r = []
            split = input_range.split("-")
            val1 = int(split[0])
            val2 = int(split[1])
            for i in range(val1, val2+1):
                r.append(i)
            ranges.append(r)

    return ranges

def solve_1():
    ranges = read_input()

    val = 0
    for range in ranges:
        for id in range:
            invalid = is_invalid(str(id))
            if invalid:
                val += id
    
    print(val)

def solve_2():
    ranges = read_input()

    val = 0
    for range in ranges:
        for id in range:
            invalid = is_invalid2(str(id))
            if invalid:
                val += id
    
    print(val)

def is_invalid(id):
    mid = len(id)//2
    part1 = id[:mid]
    part2 = id[mid:]
    return part1 == part2

def is_invalid2(id):
    mid = len(id)//2
    for i in range(1, mid+1):
        if len(id)%i != 0:
            continue
        p = id[:i]
        n = len(id)//i
        if p*n == id:
            return True
    return False

solve_1()
solve_2()