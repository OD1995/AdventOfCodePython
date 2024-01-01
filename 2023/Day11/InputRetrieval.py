import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2023,11)

data = ir.get_data()
testData = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

def processor(data):
    result = []
    for line in data.split("\n"):
        if line == "":
            continue
        result.append(list(line))
    return result

ir.save_both(
    processor,
    [testData,data]
)