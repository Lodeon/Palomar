# Wade Polo 2/24/14
# Starting out with Python pg. 115 #7
# Calories from Fat and Carbohydrates
# Accepts user input of grams of fat and carbs, then displays calc of resulting calories

def main ():
    fat_grams = float(input('Enter the number of grams of fat that you consumed today: '))
    carb_grams = float(input('Enter the number of grams of carbohydrates that you consumed today: '))
    show_fat(fat_grams)
    show_carb(carb_grams)

def show_fat(grams):
    fat_cals = grams * 9
    print('You consumed', fat_cals, 'calories from fat today.')

def show_carb(grams):
    carb_cals = grams * 4
    print('You consumed', carb_cals, 'calories from carbohydrates today.')

main()
