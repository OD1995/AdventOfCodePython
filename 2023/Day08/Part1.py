import json

with open(r".\2023\Day08\data.json") as f_in:
    data = json.load(f_in)

def get_instruction(instructions,step):
    return instructions[step % len(instructions)]

current_location = "AAA"
step = 0
while current_location != "ZZZ":
    instruction = get_instruction(data['instructions'],step)
    ix = 0 if instruction == "L" else 1
    current_location = data[current_location][ix]
    step += 1
    print(step,current_location)

print(step)