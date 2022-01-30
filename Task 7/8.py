a, b, c = int(input("first: ")), int(input("second: ")), int(input("third: "))
if a > b:
    print("Oldest is:", end=" ")
    print(a) if a > c else print(c)
    print("Youngest is:", end=" ")
    print(b) if b < c else print(c)
else:
    print("Oldest is:", end=" ")
    print(b) if b > c else print(c)
    print("Youngest is:", end=" ")
    print(a) if a < c else print(c)
