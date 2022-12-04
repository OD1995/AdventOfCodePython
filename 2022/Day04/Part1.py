import json

with open(r".\2022\Day04\data.json") as f_in:
    data = json.load(f_in)

total = 0

for x in data:
    [[a,b],[c,d]] = x
    if (
        ((c <= a) & (b <= d))
        |
        ((a <= c) & (d <= b))
    ):
        total += 1

print(total)