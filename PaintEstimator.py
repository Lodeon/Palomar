# Wade Polo 2/24/14
# Starting out with Python pg. 115 #9
# Paint Job Estimator
# Figures out the cost of a paint job

def main():
    paintGallons = 1
    sqaureFootage = float(input('Enter the square footage of the wall space to be painted: '))
    paintCost = float(input('Enter the cost per gallon of the paint being used: $'))
    paintRequired(paintGallons, sqaureFootage)
    laborRequired(sqaureFootage)
    totalPaintCost(sqaureFootage, paintCost)
    laborCharge(sqaureFootage)
    totalCost(sqaureFootage, paintCost)
    
def paintRequired(gallons, footage):
    gallons = footage / 115
    print('The number of gallons of paint required is', format(gallons, '.2f'))

def laborRequired(footage):
    lbr_rqd = 8 * (footage / 115)
    print('The number of hours of labor required is', format(lbr_rqd, '.2f'))

def totalPaintCost(footage, cost):
    cst_pnt = (footage / 115) * cost
    print('The cost of the paint will be ', '$', format(cst_pnt,'.2f'), sep='')

def laborCharge(footage):
    lbr_cst = (8 * (footage / 115)) * 20
    print('The cost of the labor will be ', '$', format(lbr_cst,'.2f'), sep='')

def totalCost(footage, cost):
    total = ((8 * (footage / 115)) * 20) + ((footage / 115) * cost)
    print('The total cost of the painting will be ', '$', format(total,'.2f'), sep='')

main()

# Inefficient, I know, but I ran out of time
