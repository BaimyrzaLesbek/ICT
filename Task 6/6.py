s = input()
s1 = s.lower()
s2 = s.upper()
cnt1 = 0
cnt2 = 0

for i in range(len(s)):
    if s[i] == s1[i]:
        cnt1 += 1
    else:
        cnt2 += 1

if cnt1 >= cnt2:
    print(s1)
else:
    print(s2)