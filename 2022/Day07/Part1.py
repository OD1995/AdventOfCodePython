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

total_size = root_dir.get_size()
answer = 0
for k,v in dir_dict.items():
    sz = v.get_size()
    if sz <= 100000:
        answer += sz
print(answer)