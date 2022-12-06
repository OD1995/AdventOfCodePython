import json

with open(r".\2022\Day06\data.json") as f_in:
    data = json.load(f_in)


def f(D):
    i = 4
    n = 4
    while True:
        S = D[i-n:i]
        if len(set(S)) == n:            
            return i
        i += 1

for D in data['datastreams']:
    print(f(D))