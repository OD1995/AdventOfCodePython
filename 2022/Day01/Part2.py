import json

with open(r".\2022\Day01\data.json") as f_in:
    data = json.load(f_in)

top_3 = [0,0,0]
min_val = 0
min_ix = 0

for elf_cals_list in data:
    if sum(elf_cals_list) > min_val:
        top_3[min_ix] = sum(elf_cals_list)
        min_val = min(top_3)
        min_ix = top_3.index(min_val)

print(sum(top_3))