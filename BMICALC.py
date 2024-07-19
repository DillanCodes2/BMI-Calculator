gender = input("Male or Female: ")
unit = input("(M)etric or (I)mperial: ")
if unit.upper() == "M":
    height = input("What is your height in Meters? ")
    weight = input("What is your weight in Kilos?" )
    bmi = float(weight)/ (float(height) ** 2)
elif unit.upper() == "I":
    weight = input("How much do you weigh in Pounds?")
    height = input("What is your height in inches?")
    bmi = (float(weight) * 703)/ (float(height)) ** 2

print(f'Your bmi is {bmi}')

if gender.lower() == "female":
    if bmi < 18.5:
        print("You are underweight")
    elif 18.5 <= bmi <= 24.9:
        print("You are in the normal range")
    elif 25 <= bmi < 29.9:
        print("You are overweight")
    elif bmi >= 30:
        print("You are obese")
elif gender.lower() == "male":
    if bmi < 18.5:
        print("You are underweight")
    elif 18.5 <= bmi <= 24.9:
        print("You are in the normal range")
    elif 25 <= bmi < 29.9:
        print("You are overweight")
    elif 30 <= bmi < 34.9:
        print("You are obese")
    elif bmi >= 35:
        print("You are EXTREMELY obese")