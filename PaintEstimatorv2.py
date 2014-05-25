# Wade Polo 2/24/14
# Starting out with Python pg. 115 #9
# Paint Job Estimator
# Figures out the cost of a paint job

def main():
    sqaureFootage = float(input('Enter the square footage of the wall space to be painted: '))
    paintCostGallon = float(input('Enter the cost per gallon of the paint being used: $'))
    chargeCalcs(sqaureFootage, paintCostGallon)
    
def chargeCalcs(sqaureFootage, paintCostGallon):
    paintGallons = sqaureFootage / 115
    print('The number of gallons of paint required is', format(paintGallons, '.2f'))
    laborHours = 8 * paintGallons
    print('The number of hours of labor required is', format(laborHours, '.2f'))
    totalPaintCost = paintGallons * paintCostGallon
    print('The cost of the paint will be ', '$', format(totalPaintCost,'.2f'), sep='')
    totalLaborCost = laborHours * 20
    print('The cost of the labor will be ', '$', format(totalLaborCost,'.2f'), sep='')
    total = totalLaborCost + totalPaintCost
    print('The total cost of the painting will be ', '$', format(total,'.2f'), sep='')

main()
