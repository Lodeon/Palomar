# Wade Polo 2/10/14
# Starting out with Python pg. 78-79 #9
# Celsius to Fahrenheit Temperature Converter
# Takes input of temperateures in Celsius, calculates the Fahrenheit conversion, then displays the result
ctemp = float(input('What is the temperature in degrees Celsius? '))  #asks for celsius temp
ftemp = (((9 / 5) * ctemp) + 32)    #calcs temp in fahrenheit
print('The temperature in Fahrenheit is',format(ftemp, '.2f'),'degrees.')  #displays result
