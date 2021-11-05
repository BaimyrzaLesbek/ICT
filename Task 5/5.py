cent = int(input())
toonie = cent // 200
cent = cent % 200
loonie = cent // 100
cent = cent % 100
quarter = cent // 25
cent = cent % 25
dime = cent // 10
cent = cent % 10
nickel = cent // 5
cent = cent % 5
penny = cent
print("toonie:",toonie)
print("loonie:",loonie)
print("quarter:",quarter)
print("dimes:",dime)
print("nickels:",nickel)
print("pennies:",penny)