import json

with open(r".\2023\Day01\data.json") as f_in:
    data = json.load(f_in)

nums = {
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9
}
lens = []
for n in nums.keys():
    if len(n) not in lens:
        lens.append(len(n))
lens.sort()

def get_word(S,direction,nums,lens):
    ix = 0
    while True:
        for L in lens:
            s = S[ix:ix+L] if direction == 'first' else S[len(S)-ix-L:len(S)-ix]
            char = ix if direction == 'first' else len(S)-ix
            if s in nums:
                return char,str(nums[s])
        ix += 1
        if ix > len(S):
            break
    return [100000000,0] if direction == 'first' else [0,0]

def get_digit(S,direction):
    for i in range(len(S)):
        if direction == 'last':
            i = len(S)-1-i
        if S[i].isdigit():
            return i,S[i]
    return [100000000,0] if direction == 'first' else [0,0]

total = 0
for d in data:
    # print(d)
    # if d == '48jlqz':
    #     a = 1
    first_num = get_digit(d,'first')
    first_word = get_word(d,'first',nums,lens)
    first = first_num[1] if first_num[0] < first_word[0] else first_word[1]
    last_num = get_digit(d,'last')
    last_word = get_word(d,'last',nums,lens)
    last = last_num[1] if last_num[0] >= last_word[0] else last_word[1]
    res = int(first + last)
    # print(res)
    total += res
print(total)