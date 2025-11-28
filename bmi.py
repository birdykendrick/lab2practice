def calculate_bmi(height, weight):
    print("Height: " + str(height))
    print("Weight: " + str(weight))

    bmi = weight / (height * height)
    print("Your BMI is: " + str(bmi))

    if bmi < 18.5:
        return -1
    elif bmi >= 18.5 and bmi <= 25:
        return 0
    else:
        return 1

calculate_bmi(weight=57, height=1.73)

def calc_average(avg):
    print("calculate average")
    totallen = len(avg)
    totalval = sum(avg)
    avg = totalval / totallen

    return avg

def find_min_max(minmax):
    minimum = min(minmax)
    maximum = max(minmax)

    return[minimum, maximum]

def sort_temperature(values):
    newlist = sorted(values)

    return newlist

def calc_median_temperature(values):
    vallist = sorted(values)
    total_len = len(vallist)

    if total_len %2 == 0:
        mid1 = total_len // 2
        mid2 = total_len // 2 + 1
        medium = (vallist[mid1] + vallist[mid2]) / 2
    else:
        middle = total_len // 2
        medium = vallist[middle]
    return medium
    
def display_main_menu():
    print("Enter some numbers seperated by commas (eg 5, 67, 32)")

def get_user_input():
    num_list = []
    x = input("Enter a list of number with a ,")
    x = x.split(",")
    for item in x:
        num_list.append(float(item))

    return num_list


def main():
    print("ET0735 (DevOps for AIoT) -Lab 2- Introduction to python")
    display_main_menu()
    num_list = get_user_input()

if __name__ == "__main__":
    main()
