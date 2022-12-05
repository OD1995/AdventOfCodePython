import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2022,5)

data = ir.get_data()
testData = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

def top_bit(data):
    D = data.split("\n\n")[0]
    lines = list(reversed(D.split("\n")))
    crate_dict = {}
    important_indexes = [
        (j*4) + 1
        for j in range(int((len(lines[0])+1)/4))
    ]
    for i,line in enumerate(lines):
        if i == 0:
            for j in important_indexes:
                crate_dict[int(line[j])] = []
        else:
            for ix,k in enumerate(important_indexes):
                if line[k] != " ":
                    crate_dict[ix+1].append(line[k])
    return crate_dict

def bottom_bit(data):
    D = data.split("\n\n")[1]
    lines = D.split("\n")
    instructions = []
    for line in lines:
        if line != "":
            _,MOVE,_,FROM,_,TO = line.split(" ")
            instructions.append(
                {
                    'move' : int(MOVE),
                    'from' : int(FROM),
                    'to' : int(TO)
                }
            )
    return instructions

def processor(data):
    crate_dict = top_bit(data)
    instructions = bottom_bit(data)
    return {
        'crate_dict' : crate_dict,
        'instructions' : instructions
    }

ir.save_both(
    processor,
    [testData,data]
)