import json

with open(r".\2021\Day01\data.json") as f_in:
    data = json.load(f_in)

# data = [
#     199,
#     200,
#     208,
#     210,
#     200,
#     207,
#     240,
#     269,
#     260,
#     263,
# ]

window_size = 3

increases = 0

old_ix = 0
new_ix = window_size

while new_ix <= len(data) - 1:
    if data[new_ix] > data[old_ix]:
        increases += 1
    old_ix += 1
    new_ix += 1

print(increases)