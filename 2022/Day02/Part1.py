import json

with open(r".\2022\Day02\data.json") as f_in:
    data = json.load(f_in)

elf_lookup = {
    "A" : "R",
    "B" : "P",
    "C" : "S"
}

me_lookup = {
    "X" : "R",
    "Y" : "P",
    "Z" : "S"
}

winning_combinations = [
    ("A","Y"),
    ("B","Z"),
    ("C","X")
]

selection_points = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

total_score = 0
for elf,me in data:
    if elf_lookup[elf] == me_lookup[me]:
        total_score += 3
    elif (elf,me) in winning_combinations:
        total_score += 6
    total_score += selection_points[me]

print(total_score)