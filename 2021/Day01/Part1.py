import json

with open(r".\2021\Day01\data.json") as f_in:
    data = json.load(f_in)

increases = 0

for i,val in enumerate(data):
    if i == 0:
        continue
    if val > data[i-1]:
        increases += 1
    
print(increases)