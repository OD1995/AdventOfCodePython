import json

with open(r".\2023\Day03\data.json") as f_in:
    data = json.load(f_in)

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
            coords.append((i,j))
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

coords_nums = {}
for nd in number_details:
    for c in nd['coords']:
        coords_nums[c] = nd

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

def get_gear_ratio(coords,coords_nums):
    nums = []
    res = 1
    for c in coords:
        if c in coords_nums:
            if coords_nums[c] not in nums:
                if len(nums) == 2:
                    return 0
                nums.append(coords_nums[c])
                res *= coords_nums[c]['val']
    if len(nums) == 1:
        return 0
    return res


gear_ratios = []

for x in range(len(data[0])):
    for y in range(len(data)):
        if data[y][x] == "*":
            coords = get_coords(x,y,len(data[0])-1,len(data)-1)
            gear_ratios.append(get_gear_ratio(coords,coords_nums))

print(sum(gear_ratios))