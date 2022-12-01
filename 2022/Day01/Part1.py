import json

with open(r".\2022\Day01\data.json") as f_in:
    data = json.load(f_in)

max_total = 0
for elf_cals_list in data:
    max_total = max(max_total,sum(elf_cals_list))

print(max_total)