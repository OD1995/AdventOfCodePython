# from Classes import Forest
import json

with open(r".\2022\Day09\data.json") as f_in:
    data = json.load(f_in)


def get_head_position(head_position,direction):
    if direction == "L":
        head_position[0] -= 1
    elif direction == "U":
        head_position[1] += 1
    elif direction == "R":
        head_position[0] += 1
    elif direction == "D":
        head_position[1] -= 1
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
            elif head_position[0] < tail_position[0]:
                tail_position[0] -= 1
    ## Diagonal
    else:
        if (
            (abs(head_position[0] - tail_position[0]) <= 1) &
            (abs(head_position[1] - tail_position[1]) <= 1)
        ):
            pass
        else:
            if head_position[1] > tail_position[1]:
                tail_position[1] += 1
            else:
                tail_position[1] -= 1
            if head_position[0] > tail_position[0]:
                tail_position[0] += 1
            else:
                tail_position[0] -= 1
    return tail_position
    

def print_grid2(tail_positions):
    Xs = [
        tp[0]
        for tp in tail_positions
    ] + [0]
    Ys = [
        tp[1]
        for tp in tail_positions
    ] + [0]
    grid = {
        y : {
            x : "."
            for x in range(min(Xs),max(Xs)+1)
        }
        for y in range(min(Ys),max(Ys)+1)
    }
    for X,Y in tail_positions:
        grid[Y][X] = "#"
    grid[0][0] = "s"
    for y in range(max(Ys),min(Ys)-1,-1):
        PM = ""
        for x in range(min(Xs),max(Xs)+1):
            PM += grid[y][x]
        print(PM)

def print_grid(head_position,tail_position):
    Xs = [head_position[0],tail_position[0],0]
    Ys = [head_position[1],tail_position[1],0]
    grid = {
        y : {
            x : "."
            for x in range(min(Xs),max(Xs)+1)
        }
        for y in range(min(Ys),max(Ys)+1)
    }
    grid[0][0] = "s"
    grid[tail_position[1]][tail_position[0]] = "T"
    grid[head_position[1]][head_position[0]] = "H"
    for y in range(max(Ys),min(Ys)-1,-1):
        PM = ""
        for x in range(min(Xs),max(Xs)+1):
            PM += grid[y][x]
        print(PM)
    print("------------------")

tail_positions = []
head_position = [0,0]
tail_position = [0,0]

# data = [
#     ['D',3],
#     ['R',2],
#     ['L',5],
#     ['U',2]
# ]
positions = {
    x : [0,0]
    for x in range(10)
}
for direction,steps in data:
    # print("---",direction,steps,"---")
    for i in range(steps):
        positions[0] = get_head_position(positions[0],direction)
        for j in range(1,10):
            x,y = get_tail_position(positions[j-1],positions[j])
            positions[j] = [x,y]
            if j == 9:
                tail_positions.append((x,y))
            # print_grid(head_position,tail_position)
print_grid2(tail_positions)
print(len(set(tail_positions)))

a=1
# 5385 too low