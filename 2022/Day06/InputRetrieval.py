import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2022,6)

data = ir.get_data()
testData = """
mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
"""

def processor(data):
    datastreams = [
        x
        for x in data.split("\n")
        if x != ""
    ]
    return {
        'datastreams' : datastreams
    }

ir.save_both(
    processor,
    [testData,data]
)