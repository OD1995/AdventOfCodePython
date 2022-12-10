import json

with open(r".\2022\Day10\data.json") as f_in:
    data = json.load(f_in)

cycle = 0
X = 1
cycle_scores = {}
for line in data:
    if line == "noop":
        cycle += 1
        cycle_scores[cycle] = X
    else:
        num = int(line.split(" ")[-1])
        cycle += 1
        cycle_scores[cycle] = X
        cycle += 1
        X += num
        cycle_scores[cycle] = X

during = {
    k + 1 : v
    for k,v in cycle_scores.items()
}
during[1] = 1

results = {}

screen = [
    ["."] * 40
    for i in range(6)
]

def get_xy(cycle):
    y = (cycle - 1) // 40
    x = (cycle - 1) - (40 * y)
    return x,y

for cycle in range(1,241):
    current_X = during[cycle]
    x,y = get_xy(cycle)
    if abs(current_X - x) <= 1:
        screen[y][x] = "#"

for S in screen:
    print("".join(S))