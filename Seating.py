# Wade Polo 2/24/14
# Starting out with Python pg. 115 #8
# Stadium Seating
# Accepts user input of seats sold, then displays calc of income generated

A_COST = 15
B_COST = 12
C_COST = 9

def main ():
    a_count = float(input('Enter the number of Class A seats that were sold: '))
    b_count = float(input('Enter the number of Class B seats that were sold: '))
    c_count = float(input('Enter the number of Class C seats that were sold: '))
    calc_total(a_count, b_count, c_count)

def calc_total(a, b, c):
    total = a * A_COST + b * B_COST + c * C_COST
    print('The total income generated from ticket sales was ','$',format(total, '.2f'),sep='')

main()
