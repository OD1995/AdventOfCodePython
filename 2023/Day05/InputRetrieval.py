import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2023,5)

data = ir.get_data()
testData = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

def processor(data):
    res = {}
    for i,line in enumerate(data.split("\n\n")):
        if i == 0:
            #seeds: 79 14 55 13
            res['seeds'] = list(map(int,line.replace("seeds: ","").split(" ")))
            res['maps'] = []
        else:
            if line == "":
                continue
            # water-to-light map:
            # 88 18 7
            # 18 25 70
            d = {}
            for ii,row in enumerate(line.split("\n")):
                if ii == 0:
                    _from_,_to_ = row.replace(" map:","").split("-to-")
                    d['from'] = _from_
                    d['to'] = _to_
                    d['ranges'] = []
                else:
                    if row == "":
                        continue
                    d['ranges'].append(list(map(int,row.split(" "))))
            d['ranges'].sort(key=lambda x: x[0])
            res['maps'].append(d)

    return res

ir.save_both(
    processor,
    [testData,data]
)