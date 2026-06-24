height = float(input("Enter the height in cm: "))
weight = float(input("Enter the weight in kg: "))

BMI =weight/(height/100)**2

print("Your BMI is: ",BMI)

if BMI<=18.4:
    print("You are underweight")
elif BMI<=24.5:
    print("You are healthy")
elif BMI<=29.9:
    print("You are over weight")
elif BMI<=34.9:
    print("You are obese")
else:
    print("you are severly obese")