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

for r_ix in reversed(add_new_rows):
    data.insert(r_ix+1,["."] * len(data[0]))

for c_ix in reversed(add_new_columns):
    for m in range(len(data)):
        data[m].insert(c_ix+1,".")

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

answer = 0
for a,b in combos:
    res = 0
    for k in [0,1]:
        res += abs(addresses[a][k] - addresses[b][k])
    # print(a,b,res)
    answer += res

print(answer)