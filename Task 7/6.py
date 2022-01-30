a = int(input("Purchased quantity: "))
print(round((100*a) * 1.1)) if 100*a >= 1000 else print(100*a)
