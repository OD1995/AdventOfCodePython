# from Classes import Forest
import json

with open(r".\2022\Day09\dataTest.json") as f_in:
    data = json.load(f_in)


def get_head_position(head_position,direction):
    if direction == "L":
        head_position[0] -= 1
    elif direction == "U":
        head_position[1] -= 1
    elif direction == "R":
        head_position[0] += 1
    elif direction == "D":
        head_position[1] += 1
    return head_position

def get_tail_position(head_position,tail_position):
    ## On top of each other
    if head_position == tail_position:
        return tail_position
    ## Up/down from each other
    elif head_position[0] == tail_position[0]:
        if abs(head_position[1] - tail_position[1]) > 1:
            if head_position[1] > tail_position[1]:
                tail_position[1] += 1
            elif head_position[1] < tail_position[1]:
                tail_position[1] -= 1
    ## Left/right from each other
    elif head_position[1] == tail_position[1]:
        if abs(head_position[0] - tail_position[0]) > 1:
            if head_position[0] > tail_position[0]:
                tail_position[0] += 1
            elif head_position[0] < tail_position[1]:
                tail_position[0] -= 1
    ## Diagonal
    else:
        if (
            (abs(head_position[0] - tail_position[0]) <= 1) &
            (abs(head_position[1] - tail_position[1]) <= 1)
        ):
            pass
        else:
            b = 1
    return tail_position
    

def print_grid(head_position,tail_position):
    grid = [
        ["."] * (max(head_position[0],tail_position[0]) + 1)
        for i in range(max(head_position[1],tail_position[1])+1)
    ]
    grid[0][0] = "s"
    grid[head_position[1]][head_position[0]] = "H"
    grid[tail_position[1]][tail_position[0]] = "T"
    for g in grid:
        print("".join(g))
    print("------------------")

tail_positions = []
head_position = [0,0]
tail_position = [0,0]

for direction,steps in data[:2]:
    for i in range(steps):
        head_position = get_head_position(head_position,direction)
        tail_position = get_tail_position(head_position,tail_position)
        tail_positions.append(tail_position)
        print_grid(head_position,tail_position)
