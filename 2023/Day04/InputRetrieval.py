import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2023,4)

data = ir.get_data()
testData = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def processor(data):
    res = []
    for line in data.split("\n"):
        if line == "":
            continue
        a,b = line.split(": ")
        card_num = a.replace("Card ","")
        w,m = b.split(" | ")
        res.append(
            {
                "card_no" : int(card_num),
                "winning" : list(map(int,w.strip().replace("  "," ").split(" "))),
                "drawn" : list(map(int,m.strip().replace("  "," ").split(" "))),
            }
        )

    return res

ir.save_both(
    processor,
    [testData,data]
)