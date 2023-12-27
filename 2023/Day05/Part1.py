import json

with open(r".\2023\Day05\data.json") as f_in:
    data = json.load(f_in)

for d in data["maps"]:
    d["ranges"].sort(key=lambda x: x[1])


def get_diff(val,ranges):
    for r in ranges:
        if val < r[1]:
            # return [val,val,1]
            return 0
        if r[1] + r[2] - 1 < val:
            continue
        return r[0] - r[1]
    return 0

def convert_val(val,map):
    diff = get_diff(val,map['ranges'])
    return val + diff

results = []

for seed in data['seeds']:
    # print('seed',seed)
    val = seed
    for map in data['maps']:
        val = convert_val(val,map)
        # print(map['to'],val)
    results.append(val)

print(min(results))