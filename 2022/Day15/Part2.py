import json

with open(r".\2022\Day15\data.json") as f_in:
    data = json.load(f_in)

def get_no_beacons(sx,sy,md,Q):
    D = {}
    for y in range(max(sy-md,0),min(sy+md+1,Q+1)):
        start = max(sx - md + abs(sy-y),0)
        end = min(sx + md - abs(sy-y),Q)
        # print(y,start,end+1)
        # for x in range(max(start,0),min(end+1,Q+1)):
        #     L.append((x,y))
        D[y] = (start,end)
    return D

# y:x
yes_beacon_dict = {}
no_beacon_ranges = {}

Q = 4000000
# Q = 20

def allowed(bx,by,Q):
    X = (0 <= bx) & (bx <= Q)
    Y = (0 <= by) & (by <= Q)
    return X & Y


for [sx,sy],[bx,by] in data:
    md = abs(bx-sx) + abs(by-sy)
    for y,x in get_no_beacons(sx,sy,md,Q).items():
        if y not in no_beacon_ranges:
            no_beacon_ranges[y] = [x]
        else:
            no_beacon_ranges[y].append(x)
    if allowed(bx,by,Q):
        if by not in yes_beacon_dict:
            yes_beacon_dict[by] = [bx]
        else:
            if bx not in yes_beacon_dict[by]:
                yes_beacon_dict[by].append(bx)

def combine_two_ranges(R1,R2):
    s1,e1 = R1
    s2,e2 = R2
    if (
        (s1 > e2 + 1) | (e1 + 1 < s2)
    ):
        return False
    else:
        return (min(s1,s2),max(e1,e2))

def consolidate_ranges(no_beacon_ranges):
    no_beacon_ranges.sort(key=lambda x: x[0])
    not_possible_count = 0
    while True:
        result = combine_two_ranges(
            no_beacon_ranges[not_possible_count],
            no_beacon_ranges[not_possible_count+1]
        )
        if result:
            no_beacon_ranges[not_possible_count] = result
            del no_beacon_ranges[not_possible_count+1]
        else:
            not_possible_count += 1
        if len(no_beacon_ranges) == not_possible_count + 1:
            break
    return no_beacon_ranges

def get_missing_number(cr):
    # M = []
    # for a,b in cr:
    #     for ix in range()
    # S = sorted(M)
    # for i,e in enumerate(S[1:]):
    #     if e - S[i] != 1:
    #         return e - 1
    if len(cr) == 1:
        if cr[0] != 0:
            return 0
        else:
            return cr[1] + 1
    elif len(cr) > 2:
        a=1
    else:
        return cr[0][1] + 1

for Y,nos in no_beacon_ranges.items():
    L = nos
    if Y in yes_beacon_dict:
        for bx in yes_beacon_dict[Y]:
            L.append((bx,bx))
    cr = consolidate_ranges(L)
    if ((len(cr) == 1) & (cr[0][0] == 0) & (cr[0][1] == Q)):
        pass
    else:
        X = get_missing_number(cr)
        print((X*4000000) + Y)


# no_beacon_y_x = {}
# for (x,y) in set(no_beacons):
#     if (x,y) not in yes_beacons:
#         if y not in no_beacon_y_x:
#             no_beacon_y_x[y] = [x]
#         else:
#             no_beacon_y_x[y].append(x)


# def get_answer(
#     no_beacon_y_x,
#     Q
# ):
#     for k,v in no_beacon_y_x.items():
#         if len(v) != Q + 1:
#             missing_x = get_missing_number(v)
#             potential = (missing_x,k)
#             if potential not in yes_beacons:
#                 return (missing_x*4000000) + k
# print(get_answer(no_beacon_y_x,Q))
# print(len(no_beacon_y_x[Q]))
# a=1
# def get_x_range(y,sy,sx,md):
#     if abs(y-sy) == 0:
#         start = sx - md
#         end = sx + md
#     elif abs(y-sy) == 1:
#         start = -1 * y - 1
#         end = y - 1


#     return range(start,end)