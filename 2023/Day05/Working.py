import pandas as pd
import json

with open(r".\2023\Day05\dataTest.json") as f_in:
    data = json.load(f_in)

dfs = {}

for a in reversed(data['maps']):
    _from_ = a['from']
    _to_ = a['to']
    b = {}
    _max_ = 0
    for c,d,e in a['ranges']:
        for f in range(e):
            b[c+f] = d+f
            _max_ = max(_max_,c+f)
    for g in range(_max_):
        if g not in b:
            b[g] = g
    df = pd.DataFrame(b,index=[0]).T
    df.reset_index(inplace=True)
    df.columns = [_to_,_from_]
    df.sort_values(
        by=_to_,
        inplace=True
    )
    dfs[f"{_to_} to {_from_}"] = df

path = r".\2023\Day05\day5.xlsx"

# df.to_excel(path)

with pd.ExcelWriter(path) as writer:
    for k,v in dfs.items():
        v.to_excel(
            writer,
            index=False,
            sheet_name=k
        )

# writer = pd.ExcelWriter(path)
# for k,v in dfs.items():
#     v.to_excel(writer,sheet_name=k)