import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2023,3)

data = ir.get_data()
testData = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

def processor(data):
    list_of_strings = [
        x
        for x in data.split("\n")
        if x != ""
    ]
    return list_of_strings

ir.save_both(
    processor,
    [testData,data]
)