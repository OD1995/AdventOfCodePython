import json

with open(r".\2023\Day09\data.json") as f_in:
    data = json.load(f_in)

def get_next_number(last_nums,line_below):
    if sum(line_below) == 0:
        return sum(last_nums)
    new_line_below = [
        line_below[i] - line_below[i-1]
        for i in range(1,len(line_below))
    ]
    return get_next_number(last_nums + [line_below[-1]],new_line_below)

answer = 0
for line in data:
    answer += get_next_number([],line)

print(answer)