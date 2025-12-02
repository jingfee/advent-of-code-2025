def read_input():
    instructions = []
    with open("./day1_input.txt", "r", encoding="utf-8") as input:
        for line in input:
            direction = line[0]
            val = int(line[1:])
            instructions.append(val if direction == 'R' else -1 * val)
    return instructions

def solve_1():
    instructions = read_input()

    dial = 50
    password = 0

    for instruction in instructions:
        dial = (dial + instruction)%100
        if dial == 0:
            password += 1
    
    print(password)

def solve_2():
    instructions = read_input()

    dial = 50
    password = 0

    for instruction in instructions:
        val = dial + instruction

        if (val >= 100 or val <= 0):
            if val > 0:
                password += val//100
            else:
                password += max(1, ((abs(val) + 100) // 100))
                if dial == 0:
                    password -= 1

        dial = val%100

    
    print(password)

solve_1()
solve_2()