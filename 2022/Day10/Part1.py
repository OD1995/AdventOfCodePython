import json

with open(r".\2022\Day10\data.json") as f_in:
    data = json.load(f_in)

cycle = 0
X = 1
cycle_scores = {}
for line in data:
    if line == "noop":
        cycle += 1
        cycle_scores[cycle] = X
    else:
        num = int(line.split(" ")[-1])
        cycle += 1
        cycle_scores[cycle] = X
        cycle += 1
        X += num
        cycle_scores[cycle] = X

during = {
    k + 1 : v
    for k,v in cycle_scores.items()
}

results = {}

for i in range(6):
    ix = 20 + (i * 40)
    print(ix,ix * during[ix])
    results[ix] = ix * during[ix]
print(sum(results.values()))