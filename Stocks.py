# Wade Polo 2/10/14
# Starting out with Python pg. 78-79 #10
# Stock Transaction Program
# Find out if Joe made a profit or not (too much detail to type out)
paid = 1000 * 32.87 #total stocks were bought for
pcom = paid * 0.02  #purchase commission
sold = 1000 * 33.92 #total stocks were sold for
scom = sold * 0.02  #sale commission
profit = (sold - scom) - (paid - pcom)  #calcs profit
print('Joe paid ','$',format(paid, '.2f'),' for the stock.',sep='')  #displays paid
print('Joe paid ','$',format(pcom, '.2f'),' in commission for purchasing the stock.',sep='') #displays pcom
print('Joe sold his stock for ','$',format(sold, '.2f'),'.',sep='') #displays sold
print('Joe paid ','$',format(scom, '.2f'),' in commission for selling the stock.',sep='')    #displays scom
print('Joe made a profit of ','$',format(profit, '.2f'),'.',sep='')
