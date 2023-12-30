import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2023,8)

data = ir.get_data()
testData = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

def processor(data):
    result = {}
    first_line,other_lines = data.split("\n\n")
    result['instructions'] = first_line
    for line in other_lines.split("\n"):
        if line == "":
            continue
        key,val0 = line.split(" = ")
        result[key] = val0[1:-1].split(", ")
    return result

ir.save_both(
    processor,
    [testData,data]
)