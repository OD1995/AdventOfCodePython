import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2022,1)

data = ir.get_data()
# data = """1000
# 2000
# 3000

# 4000

# 5000
# 6000

# 7000
# 8000
# 9000

# 10000"""

list_of_strings = data.split("\n\n")
list_of_lists = [
    [
        int(y)
        for y in x.split("\n")
        if y != ""
    ]
    for x in list_of_strings
]

ir.save(list_of_lists)