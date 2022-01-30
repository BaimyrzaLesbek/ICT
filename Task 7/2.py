a = int(input())
print("Leap year.") if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0) else print("Not leap year.")