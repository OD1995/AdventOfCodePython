import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2022,17)

data = ir.get_data()
testData = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

def processor(data):
    D = []
    for x in list(data):
        if x == ">":
            D.append(1)
        elif x == "<":
            D.append(-1)
    return D

ir.save_both(
    processor,
    [testData,data]
)