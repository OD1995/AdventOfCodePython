import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2022,8)

data = ir.get_data()
testData = """30373
25512
65332
33549
35390"""

def processor(data):
    list_of_lists = [
        [
            int(y)
            for y in x
        ]
        for x in data.split("\n")
        if x != ""
    ]
    return list_of_lists

ir.save_both(
    processor,
    [testData,data]
)