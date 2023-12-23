import json

with open(r".\2023\Day01\data.json") as f_in:
    data = json.load(f_in)

def get_digit(S,direction):
    for i in range(len(S)):
        if direction == 'last':
            i = len(S)-1-i
        if S[i].isdigit():
            return S[i]
        
total = 0
for d in data:
    total += int(
        get_digit(d,'first') +
        get_digit(d,'last')
    )
print(total)