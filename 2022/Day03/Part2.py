import json

with open(r".\2022\Day03\data.json") as f_in:
    data = json.load(f_in)

total = 0

def get_priority(A,B,C):
    while True:
        for a in A:
            if a in B:
                if a in C:
                    return(ord(a) - 38) if a.isupper() else (ord(a) - 96)

for i in range(int(len(data)/3)):
    total += get_priority(*data[3*i:(3*i)+3])

print(total)