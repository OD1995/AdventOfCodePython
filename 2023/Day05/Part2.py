import json
from datetime import datetime

START = datetime.now()

with open(r".\2023\Day05\data.json") as f_in:
    data = json.load(f_in)

levels = {}

# 79 - 81 - 81 - 81 - 74 - 78 - 78 - 82
# 14 - 14 - 53 - 49 - 42 - 42 - 43 - 43
# 55 - 57 - 57 - 53 - 46 - 82 - 82 - 86
# 13 - 13 - 52 - 41 - 34 - 34 - 35 - 35
# 00 - 01 - 02 - 03 - 04 - 05 - 06 - 07

# for X in range(1,8):

for level_num, map in enumerate(data['maps']):
    level_dict = {}
    R = []
    for r in map['ranges']:
        level_dict[tuple(r)] = r[0] - r[1]
        R.append((r[1],r[1]+r[2]-1))
    R.sort(key=lambda x: x[0])
    last_max = -1
    for rr in R:
        if rr[0] - last_max == 1:
            last_max = rr[1]
            continue
        ab = last_max + 1
        c = rr[0] - last_max - 1
        level_dict[(ab,ab,c)] = 0
        last_max = rr[1]
    level_dict[(last_max+1,last_max+1,None)] = 0
    levels[level_num+1] = level_dict

max_levels = max(levels.keys())

routes = {}

def get_current_min(current_min,k,change):
    if k == (None,None,None):
        if current_min is None:
            return None
        return current_min
    if current_min is None:
        return k[0]
    if k[2] is not None:
        if current_min > k[1] + k[2] - 1:
            return 'no'
    cm = current_min if current_min is not None else k[1]
    k1 = k[1] if k[1] is not None else cm
    return max(cm,k1) + k[0] - k[1]

def get_current_max(current_max,k,v):
    if k == (None,None,None):
        if current_max is None:
            return None
        return current_max
    if k[2] is None:
        return current_max
    if current_max is None:
        return k[0] + k[2] - 1
    if current_max < k[1]:
        return 'no'
    cm = current_max if current_max is not None else k[1] + k[2] - 1
    sumK = k[1] + k[2] - 1 if k[1] is not None else cm
    return min(cm,sumK) + k[0] - k[1]

def compare_vals(new_current_min,new_current_max):
    # new_current_min <= new_current_max
    if (new_current_max is None) or (new_current_min is None):
        return True
    if (new_current_max == 'no') or (new_current_min == 'no'):
        return False
    return new_current_min <= new_current_max

def traverse_levels(
        level_num,
        routes,
        levels,
        route_so_far,
        # starting_min,
        # starting_max,
        current_min,
        current_max,
        change
):
    for k,v in levels[level_num].items():
        if (k == (0,0,50)):
            a=1
        new_change = change + v
        ## New values after they've passed through the mapping
        new_current_min = get_current_min(current_min,k,new_change)
        new_current_max = get_current_max(current_max,k,new_change)
        if compare_vals(new_current_min,new_current_max):
            new_route_so_far = route_so_far + [k]
            if level_num == max(levels.keys()):
                key = tuple(new_route_so_far)
                val = {
                    'min' : new_current_min,
                    'max' : new_current_max,
                    'change' : new_change
                }
                routes[key] = val
            else:
                # routes = traverse_levels(
                #         level_num+1,
                #         routes,
                #         levels,
                #         new_route_so_far,
                #         # starting_min,
                #         # starting_max,
                #         new_current_min,
                #         new_current_max,
                #         new_change
                # )
                routes = traverse_levels(level_num+1,routes,levels,new_route_so_far,new_current_min,new_current_max,new_change)
    return routes

routes = traverse_levels(1,routes,levels,[],None,None,0)

for k,v in routes.items():
    a = v['min'] - v['change'] if v['min'] is not None else 'any'
    b = v['max'] - v['change'] if v['max'] is not None else 'any'
    c = v['min']
    d = v['max']
    # print(f"Between {a} and {b} leads to between {c} and {d}")

res_pairs = [
    ([
        v['min'] - v['change'] if v['min'] is not None else None,
        v['max'] - v['change'] if v['max'] is not None else None
    ],v['min'],v['change'])
    for k,v in routes.items()
]
res_pairs.sort(key=lambda x: x[1])

# seed_pairs = [
#     [79,1],
#     [14,1],
#     [55,1],
#     [13,1],
# ]
lst = data['seeds']
n = 2
seed_pairs = [lst[i:i + n] for i in range(0, len(lst), n)]
seed_pairs.sort(key=lambda x: x[0])

def get_min_using_pairs(rp,sp):
    for r in rp:
        a=1
        for s in sp:
            new_min = max(r[0][0] or s[0],s[0])
            new_max = min(r[0][1] or s[0] + s[1] - 1,s[0] + s[1] - 1)
            if compare_vals(new_min,new_max):
                return new_min + r[2]

print(get_min_using_pairs(res_pairs,seed_pairs))

END = datetime.now()

print(END - START)