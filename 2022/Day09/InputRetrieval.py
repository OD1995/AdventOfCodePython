import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2022,9)

data = ir.get_data()
testData = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

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