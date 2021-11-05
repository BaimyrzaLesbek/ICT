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