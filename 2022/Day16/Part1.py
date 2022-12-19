import json
from Classes import Valve

with open(r".\2022\Day16\dataTest.json") as f_in:
    data = json.load(f_in)

v = Valve('AA',data)
res = v.get_path_to('JJ',[])
a=1
# already_on = []

# ## Get path shortest path from/to each valve
# routes = {}
# for valve_from in data.keys():
#     for valve_to in data.keys():
#         if valve_from == valve_to:
#             continue
#         path = []
#         if valve_to in data[valve_from]['options']:
#             path.append(valve_to)
#         else:
#             pass
        

## Given minutes left, benefit of turning each one on, talking into account path

minutes_remaining = 30
starting_position = 'AA'