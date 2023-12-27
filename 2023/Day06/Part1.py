import json

with open(r".\2023\Day06\dataTest.json") as f_in:
    data = json.load(f_in)
answer = 1
for i in range(len(data['times'])):
    time = data['times'][i]
    record_distance = data['distances'][i]
    options = 0
    speeds = []
    for speed in range(1,time):
        time_left = time - speed
        distance_travelled = speed * time_left
        if distance_travelled > record_distance:
            options += 1
            speeds.append(speed)
    print(speeds)
    answer *= options
print(answer)