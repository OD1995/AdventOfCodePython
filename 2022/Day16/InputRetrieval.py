import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2022,16)

data = ir.get_data()
testData = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

def processor(data):
    D = {}
    for line in data.split("\n"):
        if line == "":
            continue
        valve = line.split(" ")[1]
        rate = int(line[line.index("=")+1:line.index(";")])
        options1 = line[line.index("valve")+5:].replace("s ","").split(",")
        options = [x.strip() for x in options1]
        O = {
            'rate' : rate,
            'options' : options
        }
        D[valve] = O
    return D

ir.save_both(
    processor,
    [testData,data]
)