import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2023,9)

data = ir.get_data()
testData = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

def processor(data):
    result = []
    for line in data.split("\n"):
        if line == "":
            continue
        result.append(list(map(int,line.split(" "))))
    return result

ir.save_both(
    processor,
    [testData,data]
)