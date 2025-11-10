def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight /((height * height))

    print("BMI = " + str(bmi))

    if bmi < 18.5:
        print("You are underweight.")
    elif bmi >= 18.5 and bmi <= 25:
        print("You have a normal weight.")
    elif bmi > 25:
        print("You are overweight.")
        
calculate_bmi(weight=57, height=1.73)