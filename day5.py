def read_input():
    fresh_lists = []
    ingredients = []
    reading_ingredients = False
    with open("./day5_input.txt", "r", encoding="utf-8") as input:
        for line in input:
            if line == '\n':
                reading_ingredients = True
                continue

            if reading_ingredients:
                ingredients.append(int(line.rstrip('\n')))
            else:
                split = line.rstrip('\n').split('-')
                start = int(split[0])
                end = int(split[1])
                fresh_lists.append((start, end))

    return (fresh_lists, ingredients)

def solve_1():
    (fresh_lists, ingredients) = read_input()

    fresh = 0
    for ingredient in ingredients:
        for fresh_list in fresh_lists:
            if ingredient >= fresh_list[0] and ingredient <= fresh_list[1]:
                fresh += 1
                break
    print(fresh)

def solve_2():
    (fresh_lists, ingredients) = read_input()
    fresh_lists = sorted(fresh_lists, key=lambda x: x[0])

    while True:
        new_list = []
        index = 0
        overlap_found = False
        while index < len(fresh_lists):
            r = fresh_lists[index]
            if index == len(fresh_lists) - 1:
                new_list.append(r)
                break
            
            nr = fresh_lists[index+1]
            if((r[1] + 1) >= nr[0]):
                if(r[1] < nr[1]):
                    new_list.append((r[0], nr[1]))
                else:
                    new_list.append(r)
                overlap_found = True
                index += 1
            else:
                new_list.append(r)
            index += 1
        if not overlap_found:
            break
        fresh_lists = new_list
    
    sum = 0
    for list in fresh_lists:
        sum += (list[1] - list[0]) + 1
    
    print(sum)


solve_1()
solve_2()