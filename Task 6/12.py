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