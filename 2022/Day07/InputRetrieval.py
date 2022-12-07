import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2022,7)

data = ir.get_data()
testData = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

def processor(data):
    blocks = data.split("\n$ ")
    ix = 0
    info = []
    # while True:
    for cb in blocks:
        # cb = blocks[ix]
        if cb == "$ cd /":
            pass
        elif cb.startswith("ls"):
            L = cb.strip().split("\n")
            info.append(
                {
                    'command' : L[0],
                    'output' : L[1:]
                }
            )
        elif cb.startswith("cd"):
            info.append(
                {
                    'command' : cb,
                    'output' : None
                }
            )
        else:
            a = 1
    return info

ir.save_both(
    processor,
    [testData,data]
)