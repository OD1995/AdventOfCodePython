import json

with open(r".\2023\Day06\data.json") as f_in:
    data = json.load(f_in)
time_available = int("".join(list(map(str,data['times']))))
record_distance = int("".join(list(map(str,data['distances']))))

def get_time(speed,diff,time_available,record_distance):
    while True:
        time_left = time_available - speed
        distance_travelled = speed * time_left
        if distance_travelled > record_distance:
            return speed
        speed += diff


first = get_time(1,1,time_available,record_distance)
last = get_time(time_available-1,-1,time_available,record_distance)
print(last - first + 1)