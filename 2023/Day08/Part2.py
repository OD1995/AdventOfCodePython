import json

with open(r".\2023\Day08\dataTest3.json") as f_in:
    data = json.load(f_in)

current_locations = [
    x
    for x in data.keys()
    if x[-1] == "A"
]

D = {}

instructions = data['instructions']

for loc in current_locations:
    key = loc
    step = 0
    z_count = 0
    while True:
        instruction = instructions[step % len(instructions)]
        ix = 0 if instruction == "L" else 1
        loc = data[loc][ix]
        step += 1
        if loc[-1] == "Z":
            D[key] = step
            break

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

def get_lowest_common_mulitple(A):
    lcm = 1
    for i in A:
        lcm = lcm * i // gcd(lcm, i)
    return lcm

print(get_lowest_common_mulitple(list(D.values())))