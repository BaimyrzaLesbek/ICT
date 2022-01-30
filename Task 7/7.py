a = int(input())
s = "ABCDEF"
if a < 25:
    print(s[-1])
elif a >= 25 and a < 45:
    print(s[-2])
elif a >= 45 and a < 50:
    print(s[-3])
elif a >= 50 and a < 60:
    print(s[-4])
elif a >= 60 and a < 80:
    print(s[-5])
else:
    print(s[-6])
