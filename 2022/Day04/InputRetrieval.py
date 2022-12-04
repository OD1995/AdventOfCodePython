import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2022,4)

data = ir.get_data()
testData = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

def processor(data):
    list_of_strings = data.split("\n")
    list_of_lists = [
        [
            [
                int(z)
                for z in y.split("-")
            ]
            for y in x.split(",")
        ]
        for x in list_of_strings
        if x != ""
    ]
    return list_of_lists

ir.save_both(
    processor,
    [testData,data]
)