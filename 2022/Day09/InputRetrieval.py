import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2022,9)

data = ir.get_data()
testData = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

def processor(data):
    list_of_lists = [
        [
            x.split(" ")[0],
            int(x.split(" ")[1])
        ]
        for x in data.split("\n")
        if x != ""
    ]
    return list_of_lists

ir.save_both(
    processor,
    [testData,data]
)