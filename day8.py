import math

def read_input():
    boxes = []
    with open("./day8_input.txt", "r", encoding="utf-8") as input:
        for line in input:
            split = line.rstrip('\n').split(',')
            boxes.append((int(split[0]), int(split[1]), int(split[2])))

    return boxes

def solve_1():
    boxes = read_input()
    circuits = []
    sorted_circuits = distances(boxes)

    connections = 1000
    for i in range(connections):
        (distance, box1, box2) = sorted_circuits[i]
        circuit1 = []
        circuit2 = []
        for c in circuits:
            if box1 in c:
                circuit1 = c
            if box2 in c:
                circuit2 = c
        if len(circuit1) > 0 and len(circuit2) > 0:
            if circuit1 == circuit2:
                continue
            circuits.remove(circuit1)
            circuits.remove(circuit2)
            circuits.append(circuit1 + circuit2)
        elif len(circuit1) > 0:
            circuits.remove(circuit1)
            circuit1.append(box2)
            circuits.append(circuit1)
        elif len(circuit2) > 0:
            circuits.remove(circuit2)
            circuit2.append(box1)
            circuits.append(circuit2)
        else:
            circuits.append([box1, box2])           

    prod = 1
    sorted_length = sorted(circuits, key=lambda x: len(x), reverse=True)
    for circuit in sorted_length[:3]:
        prod *= len(circuit)
    print(prod)

def solve_2():
    boxes = read_input()
    circuits = []
    sorted_circuits = distances(boxes)

    i = 0
    while i < len(sorted_circuits):
        (distance, box1, box2) = sorted_circuits[i]
        circuit1 = []
        circuit2 = []
        for c in circuits:
            if box1 in c:
                circuit1 = c
            if box2 in c:
                circuit2 = c
        if len(circuit1) > 0 and len(circuit2) > 0:
            if circuit1 == circuit2:
                i += 1
                continue
            circuits.remove(circuit1)
            circuits.remove(circuit2)
            circuits.append(circuit1 + circuit2)
        elif len(circuit1) > 0:
            circuits.remove(circuit1)
            circuit1.append(box2)
            circuits.append(circuit1)
        elif len(circuit2) > 0:
            circuits.remove(circuit2)
            circuit2.append(box1)
            circuits.append(circuit2)
        else:
            circuits.append([box1, box2])    
        if len(circuits[0]) == len(boxes):
            print(box1[0]*box2[0])
            break
        i += 1

def distances(boxes):
    distances = []
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            box1 = boxes[i]
            box2 = boxes[j]
            d = math.sqrt((box1[0] - box2[0])**2 + (box1[1] - box2[1])**2 + (box1[2] - box2[2])**2)
            distances.append((d, box1, box2))
    return sorted(distances, key=lambda x: x[0])

solve_1()
solve_2()