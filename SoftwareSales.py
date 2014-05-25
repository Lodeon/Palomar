# Wade Polo 3/10/14
# Starting out with Python pg. 154 #8
# Software Sales
# Determines the discount on large orders of software

def main():
    amountPurchased = float(input('Enter the number of software packages that you are purchasing: '))

    if amountPurchased >= 10 and amountPurchased <= 19:
        twentyDiscount(amountPurchased)
    elif amountPurchased >= 20 and amountPurchased <= 49:
        thirtyDiscount(amountPurchased)
    elif amountPurchased >= 50 and amountPurchased <= 99:
        fortyDiscount(amountPurchased)
    elif amountPurchased >= 100:
        fiftyDiscount(amountPurchased)
    else:
        print('You did not receive a discount on this purchase')
        print('The total of your purchase is ','$',format((amountPurchased * 99),'.2f'),sep='')

def twentyDiscount(amountPurchased):
    discount = ((amountPurchased * 99) * 0.2)
    print('You have received a 20% discount on this purchase for a savings of ','$',format(discount,'.2f'),sep='')
    print('The total of your purchase is ','$',format((amountPurchased * 99 - discount),'.2f'),sep='')

def thirtyDiscount(amountPurchased):
    discount = ((amountPurchased * 99) * 0.3)
    print('You have received a 30% discount on this purchase for a savings of ','$',format(discount,'.2f'),sep='')
    print('The total of your purchase is ','$',format((amountPurchased * 99 - discount),'.2f'),sep='')

def fortyDiscount(amountPurchased):
    discount = ((amountPurchased * 99) * 0.4)
    print('You have received a 40% discount on this purchase for a savings of ','$',format(discount,'.2f'),sep='')
    print('The total of your purchase is ','$',format((amountPurchased * 99 - discount),'.2f'),sep='')

def fiftyDiscount(amountPurchased):
    discount = ((amountPurchased * 99) * 0.5)
    print('You have received a 50% discount on this purchase for a savings of ','$',format(discount,'.2f'),sep='')
    print('The total of your purchase is ','$',format((amountPurchased * 99 - discount),'.2f'),sep='')


main()
