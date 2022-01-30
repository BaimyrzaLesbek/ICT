# ---------1----------
a = int(input("Enter rows number: "))
for i in range(a,0,-1):
    print(*(range(i, 0, -1)))
# ---------2----------
a = int(input("Enter number: "))
b = list(range(1,a+1))
print("Sum of ﬁrst 5 numbers is: " + str(sum(b)))
print("Average of 5 numbers is: " + str(sum(b) / a))
# ---------3----------
a = eval(input("numbers = "))
for i in a:
    if i > 300: exit()
    if i > 120: continue
    if i % 3 == 0: print(i)
# ---------4----------
a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))
for i in range(a, b+1):
    for j in range(2, i):
        if i % j == 0: break
    else:
        print(i)
# ---------5----------
a = int(input("Enter number of terms: "))
f,s = 0,1
print(f, s ,end= " ")
for i in range(a-2):
    f,s = s, f+s
    print(s, end = " ")