a, b, c = input("size = "), input("add peperoni = "), input("extra cheese = ")
d = {"L": 25, "M": 20, "S": 15}
k1 = {"YL": 3, "YM": 3, "YS": 2, "NL": 0, "NM": 0, "NS": 0}
k = {"Y": 1, "N": 0}
bill = 0
bill += d[a] + k1[b+a] + k[c]
print("Your final bill is:", bill)
