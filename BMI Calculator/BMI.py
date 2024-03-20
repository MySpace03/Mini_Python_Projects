def BMI_cal(weight,height):
    BMI = (weight * 703)/(height * height)
    return format(BMI,".2f")

Name = input("Enter your name: ")
weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter you height in inches: "))
BMI = BMI_cal(weight,height)

print(Name,", your BMI is ",BMI)

BMI = float(BMI)

if(BMI>0):
    if(BMI<=18.5):
        print("you are underweight")
    elif (BMI>18.5 and BMI<=24.9):
        print("you have normal weight")
    elif (BMI>=25 and BMI<=29.9):
        print("you are overweight")
    else:
        print("you have obesity")
else:
    print("Enter the correct details")