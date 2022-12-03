import json

with open(r".\2022\Day03\data.json") as f_in:
    data = json.load(f_in)

def get_both(comp1,comp2):
    for c in comp1:
        if c in comp2:
            return c

total = 0

for S in data:
    both = get_both(S[:int(len(S)/2)],S[int(len(S)/2):])
    total += (ord(both) - 38) if both.isupper() else (ord(both) - 96)

print(total)