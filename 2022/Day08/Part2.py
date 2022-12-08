from Classes import Forest
import json

with open(r".\2022\Day08\data.json") as f_in:
    data = json.load(f_in)

f = Forest(data)
print(f.get_max_scenic_score())