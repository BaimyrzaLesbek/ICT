# ---------------------------1---------------------------
s = input().lower()
s1 = ""
vowels = "eyuioa"
for i in s:
    if i not in vowels:
        s1 += "." + i
print(s1)
# ---------------------------2---------------------------
s = input().split("+")
s.sort()
print(*s, sep="+")
# ---------------------------3---------------------------
s = input()
print(s[0].upper() + s[1:])
# ---------------------------4---------------------------
s = input()
cnt0 = 0
cnt1 = 0
for i in s:
    if cnt1 == 7 or cnt0 == 7:
        print("YES")
        break
    if i == "0":
        cnt0 += 1
        cnt1 = 0
    elif i == "1":
        cnt1 += 1
        cnt0 = 0
else:
    print("NO")
# ---------------------------5---------------------------
s = input()
s1 = ""
for i in s:
    if i not in s1:
        s1 += i
if len(s1) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
# ---------------------------6---------------------------
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
# ---------------------------7---------------------------
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
# ---------------------------8---------------------------
s = input()
t = input()
if s[::-1] == t:
    print("YES")
else:
    print("NO")
# ---------------------------9---------------------------
n = int(input())
s = input()
if s.count("A") > s.count("D"):
    print("Anton")
elif s.count("A") < s.count("D"):
    print("Danik")
else:
    print("Friendship")
# ---------------------------10--------------------------
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
# ---------------------------11--------------------------
s = input()
for i in sorted(s):
    if i == "n":
        print(1, end=" ")
    if i == "z":
        print(0, end=" ")
# ---------------------------12--------------------------
s = input()
cnt1 = 0
cnt2 = 0
for i in s:
    if i == "x":
        cnt1 += 1
    else:
        cnt1 = 0
    if cnt1 >= 3:
        cnt2 += 1
print(cnt2)
# ---------------------------end--------------------------
