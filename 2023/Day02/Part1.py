import json

with open(r".\2023\Day02\dataTest.json") as f_in:
    data = json.load(f_in)

games_maxes = {}

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
    games_maxes[gameID] = game_maxes

maxes = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}
possibles = []
for gameID,_ in data:
    poss = {}
    for col in maxes.keys():
        poss[col] = maxes[col] >= games_maxes[gameID][col]
    if all(poss.values()):
        possibles.append(int(gameID))
print(sum(possibles))