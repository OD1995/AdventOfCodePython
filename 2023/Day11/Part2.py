import json

with open(r".\2023\Day11\data.json") as f_in:
    data = json.load(f_in)


add_new_rows = []
for i,row in enumerate(data):
    if (len(set(row)) == 1) and (row[0] == "."):
        add_new_rows.append(i)

add_new_columns = []
for j in range(len(data[0])):
    column = [
        row[j]
        for row in data
    ]
    if (len(set(column)) == 1) and (column[0] == "."):
        add_new_columns.append(j)

count = 0
addresses = {}
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "#":
            count += 1
            data[y][x] = str(count)
            addresses[count] = (x,y)

L = []
combos = []
for i in range(1,count+1):
    for ii in range(1,count+1):
        if (i == ii) or (ii in L):
            continue
        combos.append((i,ii))
    L.append(i)

multiplier = 1000000

def get_empty_lanes_crossed_over(empty_ixs,n1,n2):
    min_n = min(n1,n2)
    max_n = max(n1,n2)
    ixs = [
        x
        for x in empty_ixs
        if (min_n <= x) and (x <= max_n)
    ]
    return len(ixs)

answer = 0
for a,b in combos:
    if (a,b) == (1,7):
        pass
    res = 0
    for k in [0,1]:
        n1 = addresses[a][k]
        n2 = addresses[b][k]
        res += abs(n2 - n1)
        empty_lanes = get_empty_lanes_crossed_over([add_new_columns,add_new_rows][k],n1,n2,)
        res += empty_lanes * (multiplier - 1)
    # print(a,b,res)
    answer += res

print(answer)