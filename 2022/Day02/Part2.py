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

loss_lookup = {
    "A" : "Z",
    "B" : "X",
    "C" : "Y"
}
win_lookup = {
    "A" : "Y",
    "B" : "Z",
    "C" : "X"
}
draw_lookup = {
    "A" : "X",
    "B" : "Y",
    "C" : "Z"
}


winning_combinations1 = {
    ("A","Y") : 1,
    ("B","Z") : 1,
    ("C","X") : 1
}

winning_combinations2 = [
    ("A","Y"),
    ("B","Z"),
    ("C","X")
]

selection_lookup = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

total_score = 0
for elf,needed_result in data:
    if needed_result == "X":
        me = loss_lookup[elf]        
    elif needed_result == "Y":
        me = draw_lookup[elf]
        total_score += 3
    else:
        me = win_lookup[elf] 
        total_score += 6   
    total_score += selection_lookup[me]
       

print(total_score)