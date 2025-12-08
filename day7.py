def read_input():
    start = (0,0)
    beam_map = []
    with open("./day7_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        for index, line in enumerate(lines):
            beam_map.append(list(line.rstrip('\n')))
            s = line.find('S')
            if s != -1:
                start = (index, s)

    return (start, beam_map)

def solve_1():
    (start, beam_map) = read_input()

    splits = 0

    beams = set()
    beams.add(start)

    for i in range(len(beam_map) - 1):
        new_beams = set()
        for beam in beams:
            new_coordinate = (beam[0] + 1, beam[1])
            m = beam_map[new_coordinate[0]][new_coordinate[1]]
            if m == '^':
                new_beams.add((new_coordinate[0], new_coordinate[1] - 1))
                new_beams.add((new_coordinate[0], new_coordinate[1] + 1))
                splits += 1
            else:
                new_beams.add(new_coordinate)
        beams = new_beams

    print(splits)

def solve_2():
    (start, beam_map) = read_input()

    beams = {start[1]: 1}

    for i in range(len(beam_map) - 1):
        new_beams = {}
        for beam in beams:
            new_coordinate = (i, beam)
            m = beam_map[new_coordinate[0]][new_coordinate[1]]
            if m == '^':
                add_beam(new_coordinate[1] - 1, new_beams, beams[beam])
                add_beam(new_coordinate[1] + 1, new_beams, beams[beam])
            else:
                add_beam(new_coordinate[1], new_beams, beams[beam])
        beams = new_beams

    print(sum(beams.values()))

def add_beam(x, beams, curr_beams):
    if x in beams:
        beams[x] += curr_beams
    else:
        beams[x] = curr_beams

solve_1()
solve_2()