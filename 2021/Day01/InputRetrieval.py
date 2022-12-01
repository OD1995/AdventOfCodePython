import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2021,1)

data = ir.get_data()

L = [
    int(x)
    for  x in data.split("\n")
    if len(x) != 0
]

ir.save(L)