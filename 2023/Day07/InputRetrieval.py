import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2023,7)

data = ir.get_data()
testData = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

def processor(data):
    result = []
    for line in data.split("\n"):
        if line == "":
            continue
        a,b = line.split(" ")
        result.append([a,int(b)])
    return result

ir.save_both(
    processor,
    [testData,data]
)