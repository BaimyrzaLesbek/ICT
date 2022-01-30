a = eval(input("numbers = "))
for i in a:
    if i > 300: exit()
    if i > 120: continue
    if i % 3 == 0: print(i)