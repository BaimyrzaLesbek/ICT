a, b = int(input("weight = ")), float(input("height = "))
bmi = round(a / (b*b))
print("Your BMI is", bmi, end=",")
print(" you are", end=" ")
if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
elif bmi >= 25 and bmi < 30:
    print("slightly overweight")
elif bmi >= 30 and bmi < 35:
    print("obese")
else:
    print("clinically obese")