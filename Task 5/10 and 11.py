#Task 10
s = input("Europe or England?: ")
if ( s == "England"):
    w, h = float(input()), float(input())
    bmt = w / (h*h) * 703
    print(bmt)
elif ( s == "Europe"):
    w, h = float(input()), float(input())
    bmt = w / (h*h)
    print(bmt)
else:
    print("Error")

# Task 11
t = float(input())
v = float(input())
if (t <= 10 and v > 4.8 ):
    wci = 13.12 + 0.6215*t - 11.37*v**(0.16) + 0.3965*t*v**0.16
    print(wci)
else:
    print("error")