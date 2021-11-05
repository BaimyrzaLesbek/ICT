s = int(input())
d = s / 86400
s %= 86400
h = s / 3600
s %= 3600
m = s / 60
s %= 60
print("%d:%02d:%02d:%02d"%(d,h,m,s))