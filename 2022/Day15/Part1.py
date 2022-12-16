import json

with open(r".\2022\Day15\data.json") as f_in:
    data = json.load(f_in)

def get_no_beacons(sx,sy,md,Q):
    L = []
    if ((sy-md <= Q) & (Q <= sy+md)):
        start = sx - md + abs(sy-Q)
        end = sx + md - abs(sy-Q)
        L.append((start,end))
    return L

no_beacon_ranges = []
yes_beacons = []

Q = 2000000

for [sx,sy],[bx,by] in data:
    md = abs(bx-sx) + abs(by-sy)
    no_beacon_ranges.extend(get_no_beacons(sx,sy,md,Q))
    if ((bx not in yes_beacons) & (by == Q)):
        yes_beacons.append(bx)
no_beacon_ranges.sort(key=lambda x: x[0])
not_possible_count = 0
def combine_two_ranges(R1,R2):
    s1,e1 = R1
    s2,e2 = R2
    if (
        (s1 > e2) | (e1 < s2)
    ):
        return False
    else:
        return (min(s1,s2),max(e1,e2))

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

answer = -1 * len(yes_beacons)

for f,t in no_beacon_ranges:
    answer += abs(f-t) + 1

print(answer)