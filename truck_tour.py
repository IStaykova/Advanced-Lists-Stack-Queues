from collections import deque

pumps_num = int(input())
pumps = deque()

for _ in range(pumps_num):
    curr_fuel, distance = map(int, input().split())
    pumps.append((curr_fuel, distance))

starting_position = 0
stops = 0

while stops < pumps_num:
    tank_fuel = 0
    for curr_fuel, distance in pumps:
        tank_fuel += curr_fuel
        if tank_fuel < distance:
            pumps.rotate(-1)
            starting_position += 1
            stops = 0
            break
        tank_fuel -= distance
        stops += 1
print(starting_position)