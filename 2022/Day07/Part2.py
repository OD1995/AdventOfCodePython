from Classes import Directory,File
import json

with open(r".\2022\Day07\data.json") as f_in:
    data = json.load(f_in)

current_path = []
root_dir = Directory(
    name="/",
    path=current_path
)
dir_dict = {
    tuple(current_path) : root_dir
}
for line in data:
    current_dir = dir_dict[tuple(current_path)]
    command = line['command']
    output = line['output']
    if command == "ls":
        for o in output:
            if o.startswith("dir"):
                new_dir = Directory(
                    name=o.split(" ")[1],
                    path=current_path
                )
                dir_dict[tuple(current_path+[new_dir.name])] = new_dir
                current_dir.add_child_directory(new_dir)
            else:
                new_file = File(
                    name=o.split(" ")[1],
                    size=int(o.split(" ")[0])
                )
                current_dir.add_file(new_file)
    elif command == "cd ..":
        current_path = current_path[:-1]
    else:
        current_path.append(command.split(" ")[1])
capacity = 70000000
needed = 30000000
used = root_dir.get_size()
unused = capacity - used
delete_req = needed - unused
answer = capacity
options = []
for k,v in dir_dict.items():
    sz = v.get_size()
    if sz >= delete_req:
        answer = min(answer,sz)
print(answer)