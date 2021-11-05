s = input()
s1 = ""
if "a" <= s[0] <= "z":
    s1 += chr(ord(s[0]) - 32)
else:
    s1 += s[0]
for i in s[1:]:
    if "A" <= i <= "Z":
        s1 += chr(ord(i) + 32)
if s1:
    print(s1)
else:
    print(s)
