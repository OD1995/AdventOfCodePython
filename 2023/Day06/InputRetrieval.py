import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2023,6)

data = ir.get_data()
testData = """Time:      7  15   30
Distance:  9  40  200"""

def helper(S):
    _,S = S.split(":")
    while True:
        S = S.strip().replace("  "," ")
        try:
            return list(map(int,S.split(" ")))
        except ValueError:
            pass

def processor(data):
    t,d = [
        x
        for x in data.split("\n")
        if x != ""
    ]
    times = helper(t)
    distances = helper(d)
    return {
        'times' : times,
        'distances' : distances
    }

ir.save_both(
    processor,
    [testData,data]
)