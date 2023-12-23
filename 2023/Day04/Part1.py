import json

with open(r".\2023\Day04\data.json") as f_in:
    data = json.load(f_in)

points = []

for card in data:
    p = 0
    for n in card['winning']:
        if n in card['drawn']:
            if p == 0:
                p += 1
            else:
                p *= 2
    points.append(p)

print(sum(points))