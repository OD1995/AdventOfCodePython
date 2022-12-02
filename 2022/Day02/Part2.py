import json

with open(r".\2022\Day02\data.json") as f_in:
    data = json.load(f_in)


result_lookup = {
    "X" : {
        "A" : 3,
        "B" : 1,
        "C" : 2
    },
    "Y" : {
        "A" : 1,
        "B" : 2,
        "C" : 3
    },
    "Z" : {
        "A" : 2,
        "B" : 3,
        "C" : 1
    }
}
result_points = {
    "X" : 0,
    "Y" : 3,
    "Z" : 6
}

total_score = 0
for elf,needed_result in data:
    total_score += result_lookup[needed_result][elf]
    total_score += result_points[needed_result]

print(total_score)