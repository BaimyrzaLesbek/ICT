import math
t1, g1 = float(input()), float(input())
t2, g2 = float(input()), float(input())
t1 *= math.pi / 180
g1 *= math.pi / 180
t2 *= math.pi / 180
g2 *= math.pi / 180

distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
print(distance)