def read_input():
    banks = []
    with open("./day3_input.txt", "r", encoding="utf-8") as input:
        for line in input:
            banks.append([int(char) for char in line.rstrip('\n')])

    return banks

def solve_1():
    banks = read_input()

    joltage = 0
    for bank in banks:
        j = get_joltage(bank)
        joltage += j
    
    print(joltage)

def solve_2():
    banks = read_input()

    joltage = 0
    for bank in banks:
        j = get_joltage_max(bank)
        joltage += j
    
    print(joltage)

def get_joltage(bank):
    first_index = bank.index(max(bank[:-1]))
    second_index = bank.index(max(bank[(first_index+1):]))
    return int(str(bank[first_index]) + str(bank[second_index]))

def get_joltage_max(bank):
    indexes = []
    prev_index = -1
    for i in range(12):
        subarray = bank[(prev_index+1):] if i == 11 else bank[(prev_index+1):(-11+i)]
        i = subarray.index(max(subarray)) + (prev_index + 1)
        prev_index = i
        indexes.append(i)
    
    s = ''
    for i in indexes:
        s += str(bank[i])
    return int(s)

solve_1()
solve_2()