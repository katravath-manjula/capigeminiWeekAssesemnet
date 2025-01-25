weight=int(input("enter the weight"))
Height=int(input("enetr the height"))
BMI = weight / Height*Height
print(BMI)
if BMI<18.5:
    print("underweight")
elif BMI<=18.5 and 24.9:
    print("Normal")
elif BMI<25 and 29.9:
    print("Overweight")
elif BMI>30:
    print("Obese")