f = open("1.txt", "w")
for i in range(1,6):
    x = str(i).center(20, "-")
    f.write(x)
    f.write("\n")