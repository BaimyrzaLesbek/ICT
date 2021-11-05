c = float(input())
tax_p = 0.12
tax = float("{:.2f}".format(tax_p * c))
tip_p = 0.18
tip = float("{:.2f}".format(tip_p * c))
print("tax is", tax)
print("tip is", tip)
print("sum is", "{:.2f}".format(c + tip + tax))