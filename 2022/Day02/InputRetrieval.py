import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2022,2)

data = ir.get_data()
testData = """A Y
B X
C Z"""

def processor(data):
    list_of_strings = data.split("\n")
    list_of_lists = [
        x.split(" ")
        for x in list_of_strings
        if x != ""
    ]
    return list_of_lists

ir.save_both(
    processor,
    [testData,data]
)