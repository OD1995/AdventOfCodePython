import json

with open(r".\2023\Day10\data.json") as f_in:
    data = json.load(f_in)

D2 = [
    ["unknown"]*len(data[0])
    for i in range(len(data))
]

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
        if val in ['O','I']:
            val = '.'
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
    D2[y][x] = "loop"
    nx,ny = D[y][x][0] if D[y][x][0] != (-nx,-ny) else D[y][x][1]
    x += nx
    y += ny
    distance_covered += 1
    if (sx,sy) == (x,y):
        break

## Set edges to 'no'
for x1 in range(len(data[0])):
    for y1 in range(len(data)):
        if (x1 == 0) or (y1 == 0) or (x1 == len(data[0]) - 1) or (y1 == len(data) - 1):
            if D2[y1][x1] == "unknown":
                D2[y1][x1] = 'no'

def get_type_count(D2,typs):
    type_count = 0
    for y,row in enumerate(D2):
        for x,val in enumerate(row):
            if val in typs:
                type_count += 1
    return type_count

def get_enclosed_count(D2,data,D):
    enclosed_count = 0
    for y,row in enumerate(D2):
        for x, val in enumerate(row):
            if val in ['unknown','enclosed']:
                if is_enclosed(D2,x,y,data,D):
                    enclosed_count += 1
                    # print(x,y)
    return enclosed_count

def is_enclosed(D2,x,y,data,D):
    ## # Horizontal
    ## Work out which edge we're closer to and x range
    if x <= len(D2[0]) / 2:
        x_range = reversed(range(x))
        direction = 'left'
        di = (-1,0)
    else:
        x_range = range(x+1,len(D2[0]))
        direction = 'right'
        di = (1,0)
    # x_range = range(x) if x <= len(D2[0])/2 else range(x+1,len(D2[0]))
    x_count = 0
    # last_val = None
    # last_val_lookup = {
    #     'right' : {
    #         'L' : ['-','7','J']
    #     }
    # }
    if (x,y) == (6,6):
        pass
    arrived_from = None
    for x1 in x_range:
        if D2[y][x1] != 'loop':
            continue
        if di not in D[y][x1]:
            going_to = D[y][x1][0] if D[y][x1][0] != (-di[0],-di[1]) else D[y][x1][1]
            if going_to != arrived_from:
                x_count += 1
            arrived_from = None
        elif arrived_from is None:
            arrived_from = D[y][x1][0] if D[y][x1][0] != di else D[y][x1][1]
    if x_count % 2 == 0:
        return False
    ## # Vertical
    if y <= len(D2) / 2:
        y_range = reversed(range(y))
        direction = 'up'
        di = (0,-1)
    else:
        y_range = range(y+1,len(D2))
        direction = 'down'
        di = (0,1)
    # y_range = range(y) if y <= len(D2)/2 else range(y+1,len(D2))
    y_count = 0
    arrived_from = None
    for y1 in y_range:
        if D2[y1][x] != 'loop':
            continue
        if di not in D[y1][x]:
            going_to = D[y1][x][0] if D[y1][x][0] != (-di[0],-di[1]) else D[y1][x][1]
            if going_to != arrived_from:
                y_count += 1
            arrived_from = None
        elif arrived_from is None:
            arrived_from = D[y1][x][0] if D[y1][x][0] != di else D[y1][x][1]
    if y_count % 2 == 0:
        return False
    return True
    

unknown_count = get_type_count(D2,'unknown')

while True:
    # print(unknown_count)
    for x1 in range(len(data[0])):
        for y1 in range(len(data)):
            if (
                (x1 == 0) or 
                (y1 == 0) or 
                (x1 == len(data[0]) - 1) or
                (y1 == len(data) - 1) or
                (D2[y1][x1] != 'unknown')
            ):
                continue
            # surrounding_vals = get_surrounding_vals(D2,x1,y1,lookup1)
            surrounding_vals = [
                D2[y1+yd][x1+xd]
                for xd,yd in lookup1.values()
            ]
            if 'no' in surrounding_vals:
                D2[y1][x1] = 'no'
            elif (len(set(surrounding_vals)) == 1) and (surrounding_vals[0] == 'loop'):
                D2[y1][x1] = 'enclosed'
            else:
                a = 1
    new_unknown_count = get_type_count(D2,['unknown'])
    if new_unknown_count - unknown_count == 0:
        break
    unknown_count = new_unknown_count
# print(get_type_count(D2,['enclosed','unknown'],True))
res = get_enclosed_count(D2,data,D)
print(res)