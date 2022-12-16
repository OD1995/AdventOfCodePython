import sys
sys.path.insert(0,r"C:\Dev\AdventOfCodePython\Helpers")
from InputRetriever import InputRetriever

ir = InputRetriever(2022,15)

data = ir.get_data()
testData = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

def processor(data):
    L = []
    for line in data.split("\n"):
        if line == "":
            continue
        sensor_bit,beacon_bit = line.split(": ")
        sensor_list = sensor_bit.split("=")
        sensor_x = int(sensor_list[1].replace(", y",""))
        sensor_y = int(sensor_list[-1])
        beacon_list = beacon_bit.split("=")
        beacon_x = int(beacon_list[1].replace(", y",""))
        beacon_y = int(beacon_list[-1])
        L.append(
            (
                (sensor_x,sensor_y),
                (beacon_x,beacon_y)
            )
        )
    return L

ir.save_both(
    processor,
    [testData,data]
)