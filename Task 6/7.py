n = int(input())
s = input().lower()
s1 = ""
for i in s:
    if i not in s1:
        s1 += i
if len(s1) == 26:
    print("YES")
else:
    print("NO")
