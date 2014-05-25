# Wade Polo 2/10/14
# Starting out with Python pg. 78-79 #8
# Tip, Tax, and Total
# Calculates the above after accepting user input, then displays all three.
bill = float(input('How much was the bill? $'))  #asks for bill amount
tip = bill * 0.15   #calcs tip
tax = bill * 0.07   #calcs tax
total = tip + tax + bill    #calcs total
print('A tip of 15% is ','$',format(tip, '.2f'),sep='')  #prints tip
print('The 7% tax is ','$',format(tax, '.2f'),sep='')  #prints tax
print('The total of the tip and the tax is ','$',format(total, '.2f'),sep='')  #prints total
