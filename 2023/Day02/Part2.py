import json

with open(r".\2023\Day02\data.json") as f_in:
    data = json.load(f_in)

games_maxes = {}
result = []
for gameID,games in data:
    game_maxes = {
        'red' : 0,
        'green' : 0,
        'blue' : 0
    }
    for game in games:
        for col,num in game.items():
            if num > game_maxes[col]:
                game_maxes[col] = num
    res = 1
    for col,val in game_maxes.items():
        res *= val
    result.append(res)

print(sum(result))