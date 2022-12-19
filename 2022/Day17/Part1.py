from Classes import Rock
import json

with open(r".\2022\Day17\data.json") as f_in:
    data = json.load(f_in)

jet_len = len(data)
max_height = 0
starting_x = 2
starting_y = 3
rock_index = 0
jet_index = 0
rock_list = []
other_rock_coords = []

def print_stuff(other_rock_coords):
    L = {
        i :["."] * 7
        for i in range(100)
    }
    maxY = 0
    for rc in other_rock_coords:
        L[rc[1]][rc[0]] = "#"
        maxY = max(maxY,rc[1])
    for a in range(maxY,-1,-1):
        print("".join(L[a]))
    print("--------------------------------------")

r = Rock(rock_index,starting_x,starting_y)
while True:
    jet_ix = jet_index % jet_len
    x_move_res = r.move_rock_x(data[jet_ix],other_rock_coords)
    y_move_res = r.move_rock_y(-1,other_rock_coords)
    
    if not y_move_res:
        rock_index += 1
        other_rock_coords.extend(r.get_final_coords())
        max_height = max(r.get_max_height(),max_height)
        starting_y = max_height + 4
        rock_list.append(r)
        # print(rock_index,max_height)
        # print_stuff(other_rock_coords)
        r = Rock(rock_index,starting_x,starting_y)
        if rock_index == 1000000000000:
            print(max_height+1)
            break
    jet_index += 1
a=1


