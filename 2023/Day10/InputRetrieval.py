import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2023,10)

data = ir.get_data()
testData = """..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
.........."""

def processor(data):
    result = []
    for line in data.split("\n"):
        if line == "":
            continue
        result.append(line)
    return result

ir.save_both(
    processor,
    [testData,data]
)