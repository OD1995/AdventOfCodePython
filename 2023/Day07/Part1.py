from functools import cmp_to_key
import json

with open(r".\2023\Day07\data.json") as f_in:
    data = json.load(f_in)

hand_types = {
    'five of a kind' : 7,
    'four of a kind' : 6,
    'full house' : 5,
    'three of a kind' : 4,
    'two pair' : 3,
    'one pair' : 2,
    'high card' : 1
}



def get_hand_type(hand):
    hand_set = set(hand)
    if len(hand_set) == 1:
        return 'five of a kind'
    counts = {
        x : hand.count(x)
        for x in hand_set
    }
    counts_values = list(counts.values())
    if 4 in counts_values:
        return 'four of a kind'
    if len(counts) == 2:
        return 'full house'
    if 3 in counts_values:
        return 'three of a kind'
    if counts_values.count(2) == 2:
        return 'two pair'
    if 2 in counts_values:
        return 'one pair'
    return 'high card'

def compare(x,y):
    if x[2] > y[2]:
        return 1
    if x[2] < y[2]:
        return -1
    else:
        cards = [
            'A','K','Q','J','T',
            '9','8','7','6','5',
            '4','3','2'
        ]
        for i in range(5):
            xi = cards.index(x[0][i])
            yi = cards.index(y[0][i])
            if xi < yi:
                return 1
            if yi < xi:
                return -1


res = []

for hand,bid in data:
    # print(hand,get_hand_type(hand))
    hand_type = get_hand_type(hand)
    hand_type_val = hand_types[hand_type]
    res.append([hand,hand_type,hand_type_val,bid])

res.sort(key=cmp_to_key(compare))

answer = 0

for i,r in enumerate(res,1):
    answer += i * r[3]

print(answer)