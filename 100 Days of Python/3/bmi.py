h=float(input("Enter the height in m\n"))
w=float(input("Enter your weight in kg"))
bmi=w/(h*h)
print("your bmi :",round(bmi))
if bmi<=18.5:
    print("Underweight")
elif bmi>18.5 and bmi<=25:
    print("Normal")
elif bmi>25 and bmi<=30:
    print("Overweight")
elif bmi>30 and bmi<= 35:
    print("Obese")
else:
    print("Clinically obese")