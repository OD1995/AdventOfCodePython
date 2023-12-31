import json

with open(r".\2023\Day10\data.json") as f_in:
    data = json.load(f_in)

D = []

lookup1 = {
    'U' : (0,-1),
    'D' : (0,1),
    'L' : (-1,0),
    'R' : (1,0)
}
lookup2 = {
    'S' : '?',
    'F' : 'RD',
    '7' : 'LD',
    'J' : 'LU',
    'L' : 'UR',
    '-' : 'LR',
    '|' : 'UD',
    '.' : ''
}

for y in range(len(data)):
    row = []
    for x in range(len(data[0])):
        d = []
        val = data[y][x]
        f = lookup2[val]            
        for v in f:
            if v == "?":
                s_coords = (x,y)
            else:
                d.append(lookup1[v])
        row.append(d)
    D.append(row)            

## Work out what S is
sx,sy = s_coords
g = []
for xd,yd in lookup1.values():
    if (-xd,-yd) in D[sy+yd][sx+xd]:
        g.append((xd,yd))
D[sy][sx] = g

nx,ny = g[0]
x,y = s_coords
distance_covered = 0
while True:
    nx,ny = D[y][x][0] if D[y][x][0] != (-nx,-ny) else D[y][x][1]
    x += nx
    y += ny
    distance_covered += 1
    if (sx,sy) == (x,y):
        break
print(int(distance_covered/2))