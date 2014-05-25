# Wade Polo 3/10/14
# Starting out with Python pg. 154 #7
# Book Club Points
# Determines the number of Book Club points earned

def main():
    booksPurchased = float(input('Enter the number of books that you have purchased this month: '))

    if booksPurchased == 1:
        print('You have earned 5 points this month.')
    elif booksPurchased == 2:
        print('You have earned 15 points this month.')
    elif booksPurchased == 3:
        print('You have earned 30 points this month.')
    elif booksPurchased >= 4:
        print('You have earned 60 points this month.')
    else:
        print('You have not earned any points this month.') 

main()
