import json

with open(r".\2023\Day03\data.json") as f_in:
    data = json.load(f_in)

def get_coords(i,j,i_max,j_max):
    L = [-1,0,1]
    res = []
    for x in L:
        for y in L:
            if [x,y] == [0,0]:
                continue
            if (i + x < 0) or (i + x > i_max):
                continue
            if (j + y < 0) or (j + y > j_max):
                continue
            res.append((i+x,j+y))
    return res


number_details = []
for j,line in enumerate(data):
    i = 0
    number = ""
    coords = []
    while True:
        if not line[i].isdigit():
            if number != "":
                number_details.append(
                    {
                        "val" : int(number),
                        "coords" : coords
                    }
                )
                number = ""
                coords = []
        else:
            number += line[i]
            coords.extend(get_coords(i,j,len(line)-1,len(data)-1))
        if i >= len(line) - 1:
            if number != "":
                number_details.append(
                    {
                        "val" : int(number),
                        "coords" : coords
                    }
                )
                number = ""
                coords = []
            break
        i += 1

def is_part_number(data,coords):
    for c in set(coords):
        v = data[c[1]][c[0]]
        if (not v.isdigit()) and (v != "."):
            return True
    return False

answer = 0

for d in number_details:
    num = d['val']
    if is_part_number(data,d['coords']):
        # print("yes",num)
        answer += num
    # else:
    #     print("no",num)

print(answer)

## 526341 too low