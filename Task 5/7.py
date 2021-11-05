import math
s , n = float(input()), float(input())
area = n * (s*s / (4 * math.tan(math.pi / n)))
print("{:.2f}".format(area))