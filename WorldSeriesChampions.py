# Wade Polo 4/28/14
# Starting out with Python pg. 340 #9
# World Series Champions
# Imports WorldSeriesWinners.txt then counts the number of wins for a specified team

def main():
    # Imports the .txt file and converts it to a list
    infile = open('WorldSeriesWinners.txt', 'r')
    winners = infile.readlines()
    infile.close()
    index = 0
    while index < len(winners):
        winners[index] = winners[index].rstrip('\n')
        index += 1

    # Removes any casing from the list
    casedWinners = [item.strip().lower() for item in winners]

    # Asks for a team name, removes casing, and counts the number of times it occurs in the list
    search = input('Enter the name of a baseball team: ')
    casedSearch = search.lower()
    count = casedWinners.count(casedSearch)

    # Prints the results with proper grammar
    plural = 0
    if count == 1:
        plural = ''
    else:
        plural = 's'
    print('The ', search, ' have won the World Series ', count, ' time', plural, '.', sep='')

main()
