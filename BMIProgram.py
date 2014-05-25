# Wade Polo 3/10/14
# Starting out with Python pg. 155 #10
# Body Mass Index Program Enhancement
# Determines a persons BMI and informs them of their health

def main():
    weight = float(input('Enter your weight in pounds: '))
    height = float(input('Enter your height in inches: '))

    bmi = (weight * 703) / (height ** 2)

    print('You have a Body Mass Index of',format(bmi,'.0f'))

    if bmi < 18.5:
        print('You are considered to be underweight')
    elif bmi >= 18.5 and bmi <= 25:
        print('Your weight is considered to be optimal')
    else:
        print('You are considered to be overweight')

main()
