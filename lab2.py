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

def calc_average(float_list):
    total = 0
    for num in float_list:
        total = total + sum(num)
        average = total / len(float_list)
    return average

def find_min_max(float_list):
    minvalue = min(float_list)
    maxvalue= max(float_list)
    return(minvalue, maxvalue)

def sort_temperatures(float_list):
    float_list.sort()
    return float_list

def calc_median(float_list):
    float_list.sort()
    length = len(float_list)
    if length % 2 == 0:
        median = (float_list[length // 2 - 1] + float_list[length // 2]) / 2
    else:
        median = float_list[length // 2]
    return median
        
    