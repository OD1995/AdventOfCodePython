import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2023,1)

data = ir.get_data()
testData = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

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