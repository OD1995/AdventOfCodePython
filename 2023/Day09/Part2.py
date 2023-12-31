import json

with open(r".\2023\Day09\data.json") as f_in:
    data = json.load(f_in)

def get_next_number(first_nums,line_below):
    if sum(line_below) == 0:
        res = 0
        for i,e in enumerate(first_nums):
            if i % 2 == 0:
                res += e
            else:
                res -= e
        return res
    new_line_below = [
        line_below[i] - line_below[i-1]
        for i in range(1,len(line_below))
    ]
    return get_next_number(first_nums + [line_below[0]],new_line_below)

answer = 0
for line in data:
    val = get_next_number([],line)
    # print(val)
    answer += val

print("---->",answer)