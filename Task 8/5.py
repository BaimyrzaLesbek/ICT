def prime(k):
    for i in range(2,k):
        if k % i == 0:
            return False
    return True
a = int(input("start = "))
b = int(input("end = "))
for i in range(a, b+1):
    if prime(i):
        print(i)