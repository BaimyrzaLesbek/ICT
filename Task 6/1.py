s = input().lower()
s1 = ""
vowels = "eyuioa"
for i in s:
    if i not in vowels:
        s1 += "." + i
print(s1)