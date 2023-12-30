
## 65783396797380896997090 too high
## 1563436666493426
from datetime import datetime
import json

with open(r".\2023\Day08\data.json") as f_in:
    data = json.load(f_in)

current_locations = [
    x
    for x in data.keys()
    if x[-1] == "A"
]

# final_locations = [
#     x
#     for x in data.keys()
#     if x[-1] == "Z"
# ]

# D = {}

# for k,v in data.items():
#     if k == 'instructions':
#         continue
#     for lr,loc in [
#         ['L',v[0]],
#         ['R',v[1]]
#     ]:
#         if loc not in D:
#             D[loc] = {
#                 lr : [k]
#             }
#         elif lr not in D[loc]:
#             D[loc][lr] = [k]
#         else:
#             D[loc][lr].append(k)

# locs = [
#     x
#     for x in data.keys()
#     if x[-1] == "Z"
# ]
# I = []
# while True:
#     prev_instructions = []
#     new_locs = []
#     for loc in locs:
#         d = D[loc]
#         if len(d) == 1:
#             instruction = next(iter(d))
#             # if len(d[instruction]) == 1:
#             #     prev_instructions.append(instruction)
#             #     new_locs.append(d[instruction][0])
#             # else:
#             #     raise ValueError('not sure what to do')
#             prev_instructions.append(instruction)
#             for e in d[instruction]:
#                 new_locs.append(e)
#     if len(set(prev_instructions)) == 1:
#         locs = new_locs
#         I.insert(0,prev_instructions[0])
#     else:
#         break
#         # R_count = prev_instructions.count("R")
#         # L_count = prev_instructions.count("L")
#         # if R_count == L_count:
#         #     locs = new_locs
#         #     I.insert(0,"X")
#         # else:
#         #     break

# print(I)


# start_count = len(current_locations)
# left_count = 0
# right_count = 0
# for k,v in data.items():
#     if k == 'instructions':
#         continue
#     if v[0][-1] == "Z":
#         left_count += 1
#     if v[1][-1] == "Z":
#         right_count += 1

# print(start_count,left_count,right_count)

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

def get_lowest_common_denominator(A):
    lcm = 1
    for i in A:
        lcm = lcm * i // gcd(lcm, i)
    return lcm

if True:
    instructions = data['instructions']

    results = []
    offsets = []
    for current_location in current_locations:
        print("-----> ",current_location)
        actual_step = 0
        loop_step = 0
        path = []
        is_z = []
        while (loop_step,current_location) not in path:
            path.append((loop_step,current_location))
            is_z.append(current_location[-1] == "Z")
            instruction = instructions[loop_step]
            ix = 0 if instruction == "L" else 1
            current_location = data[current_location][ix]
            actual_step += 1
            loop_step = actual_step % len(instructions)
            # print(loop_step,current_location)
        # print("Total steps:",actual_step)
        print(loop_step,len(is_z[loop_step:]))
        # results.append(actual_step - 1)
        results.append([loop_step-1,is_z[loop_step:]])
        offsets.append(loop_step-1)

## All final destinations are on the right of the previous mapping, so R has to be the last value

# min_offset = min(offsets)

# for i in range(len(results)):
#     results[i][0] -= min_offset

# print(get_lowest_common_denominator(results))

def get_loop_size(loop):
    if isinstance(loop,int):
        return loop
    L = [i for i,x in enumerate(loop) if x]
    if len(L) == 1:
        return len(loop)
    if loop[-1] != True:
        raise ValueError('Not sure what to do here')
    diffs = [
        L[i] - L[i-1]
        for i in range(1,len(L))
    ]
    if len(set(diffs)) != 1:
        raise ValueError('Not sure what to do here')
    return diffs[0]
    

def merge_two_with_offset(x_offset,x_loop,y_offset,y_loop):
    x_loop_size = get_loop_size(x_loop)
    y_loop_size = get_loop_size(y_loop)
    if x_offset == y_offset:
        return x_offset, get_lowest_common_denominator([x_loop_size,y_loop_size])
    # if x_loop_size >= y_loop_size:
    #     add_loop_size = x_loop_size
    #     running_total = x_offset
    #     other_offset = y_offset
    #     other_loop_size = y_loop_size
    # else:
    #     add_loop_size = y_loop_size
    #     running_total = y_offset
    #     other_offset = x_offset
    #     other_loop_size = x_loop_size
    if y_loop_size >= x_loop_size:
        # running_total = - x_offset# - x_loop_size
        off = y_offset - x_offset
        inc_at_end = x_offset
        add_loop_size = y_loop_size
        div_loop_size = x_loop_size
    else:
        # running_total = - y_offset# - y_loop_size
        off = x_offset - y_offset
        inc_at_end = y_offset
        add_loop_size = x_loop_size
        div_loop_size = y_loop_size
    running_total = off
    A = datetime.now()
    # a = relative_offset
    # ct = 0
    # new_offset = 'not set'
    while True:
        running_total += add_loop_size
        # ct += 1
        if (datetime.now() - A).seconds > 30:
            print('nope',running_total)
            return None
        # if (running_total - other_offset) % other_loop_size == 0:
        if running_total % div_loop_size == 0:
            # if new_offset == 'not set':
            #     new_offset = running_total
            # else:
            #     return new_offset, running_total - new_offset
            return (
                running_total + inc_at_end,
                get_lowest_common_denominator([x_loop_size,y_loop_size])
            )
        

# results = [
#     [2,8],
#     # [8,6],
#     [1,3],
#     [4,5],
#     # [3,5],
#     # [6,7]#118-140
# ]

# X = results[0]
# for i in range(1,len(results)):
#     X = merge_two_with_offset(*X,*results[i])
#     print(X)
        
def get_first_two_with_same_offset(R):
    for r in R:
        offset = r[0]
        R2 = [x for x in R if x[0] == offset]
        if len(R2) > 1:
            return r,R2[1]
    return R[:2]

R = results
while len(R) > 1:
    R = sorted(R,key=lambda x: x[0])
    X,Y = get_first_two_with_same_offset(R)
    Z = merge_two_with_offset(*X,*Y)
    print(Z)
    R.remove(X)
    R.remove(Y)
    R.append(Z)

print(R[0][0])