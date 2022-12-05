import json

with open(r".\2022\Day05\data.json") as f_in:
    data = json.load(f_in)

def print_crate(crate_dict):
    s = ""
    for i in range(len(crate_dict)):
        try:
            s += crate_dict[i+1][-1]
        except IndexError:
            pass
    print(s)    

crate_dict = {
    int(k) : v
    for k,v in data['crate_dict'].items()
}
instructions = data['instructions']

for I in instructions:
    moving_crate_list = crate_dict[I['from']][(-1*I['move']):]
    crate_dict[I['to']].extend(moving_crate_list)
    del crate_dict[I['from']][(-1*I['move']):]
    print_crate(crate_dict)