def read_input():
    numbers = []
    operators = []
    with open("./day6_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        for index, line in enumerate(lines):
            n = []
            if index == len(lines) - 1:
                operators = line.strip('\n').split()
            else:
                n = [int(item) for item in line.rstrip('\n').split()]
                numbers.append(n)

    return (numbers, operators)

def read_input2():
    numbers = []
    operators = []
    with open("./day6_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        n = []
        for j in range(len(lines[0])-2, -1, -1):
            all_empty = True
            for i in range(len(lines)):
                if lines[i][j] != ' ':
                    all_empty = False
                    break
            if all_empty:
                numbers.append(n)
                n = []
                continue
            c = ''
            for i in range(len(lines)):
                a = lines[i][j]
                if a == '*' or a == '+':
                    operators.append(a)
                else:
                    c += a
            n.append(int(c.replace(' ', '')))
        numbers.append(n)

    return (numbers, operators)

def solve_1():
    (numbers, operators) = read_input()

    sum = 0

    for j in range(len(numbers[0])):
        operator = operators[j]
        n = 1 if operator == '*' else 0
        for i in range(len(numbers)):
            if operator == '*':
                n *= numbers[i][j]
            elif operator == '+':
                n += numbers[i][j]
        sum += n

    print(sum)

def solve_2():
    (numbers, operators) = read_input2()

    sum = 0

    for i in range(len(numbers)):
        operator = operators[i]
        n = 1 if operator == '*' else 0
        for j in range(len(numbers[i])):
            if operator == '*':
                n *= numbers[i][j]
            elif operator == '+':
                n += numbers[i][j]
        sum += n

    print(sum)

solve_1()
solve_2()