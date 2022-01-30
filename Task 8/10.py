a = int(input())
b = input()
for i in range(a):
    if b[i].isalpha():
        print(b[i],end="")
print(b[a:])