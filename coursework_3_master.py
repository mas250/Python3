#    Matthew Shaw
#    Sunday, 1 November 2015 at 22:37:13
#    prize.py


file = input("enter path to file: ")    # Ask the user for the prize file
prize_file_1 = open(file)

List = []
prizes = []
def check_prize():
    """
    Checks which prizes can be excahnged for the credits owned by a user
    for the website WinTwoPrizes.com
    """
    for line in prize_file_1:
        List.append(int(line))          # Put the lines in the file into a List
    
    first_line = List.pop(0)            # Use the first value in the list

    for i in List:
        
        for j in List:                  # Compare two items in the list against
            if i + j == first_line:     # each other, if their total equalls
                prizes.append((i,j))    # the amount of prize money, add it to
                                        # the list of prizes
        
check_prize()
if prizes == []:                        # Checks the list, offers a consolation 
    print("Hard Luck")                  # message if no prizes can be obtained
else:
    print( "You can have:", prizes)
