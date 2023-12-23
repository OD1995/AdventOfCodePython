import json

with open(r".\2023\Day04\data.json") as f_in:
    data = json.load(f_in)

card_counts = {}
total_card_counts = {}

for card in data:
    key = card['card_no']
    if key in total_card_counts:
        total_card_counts[key] += 1
    else:
        total_card_counts[key] = 1
    this_card_count = total_card_counts[key]
    winners = 0
    for n in card['winning']:
        if n in card['drawn']:
            winners += 1
    cc = {}
    for i in range(winners):
        key = card['card_no'] + 1 + i
        cc[key] = 1
        if key in total_card_counts:
            total_card_counts[key] += this_card_count
        else:
            total_card_counts[key] = this_card_count
    card_counts[card['card_no']] = cc

print(sum(total_card_counts.values()))