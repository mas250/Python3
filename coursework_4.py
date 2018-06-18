#    Matthew Shaw
#    Sunday, 1 November 2015 at 22:41:23
#    validate.py

def is_valid(cardNumber):
    """
    Checks a credit card number to see if it is a valid. This is found by:
    1. Checking the sum of the alternative digits starting from the first one
    2. Doubling the remaining digits
    3. Adding the digits together from part 2.
    4. Adding this value to the values from 1.
    5. Making sure the resulting sum devides by 10
    
    """
    cardList = []
    cardListReverse = []
    doubleDigit = []                    # Lists used instead of indexing
    xList =[]
    
    numCheck = False                    # Used to control select alternative digits
    cardSum = 0
    doubleCardSum = 0

    
    for i in cardNumber:                
                                        # Convert the string of the credit card
        cardList.append(int(i))         # into numbers and add to cardList

        
    cardListReverse = cardList
    cardList.reverse()
    

    for i in cardListReverse:   
        if numCheck == False:
            cardSum = i + cardSum       # Sum the alternative numbers together
            numCheck = True             

        else:
            i = i*2                     # For alternative digits, sum the double
            if i >= 10:
                i = i-9                 # Number trick for base 10 the sum of a doubled digit is the same as the original number minus 9
            doubleCardSum = i + doubleCardSum
            numCheck = False
            
 
    if (cardSum + doubleCardSum) % 10 == 0 :
        print (True)
    else:
        print(False)                    # Prints true or False depending on if
                                        # the sum as outlined in the docstring
                                        # is a factor of 10
    

def all_x(cardNumber):
    """
    Checks valid options for credit cards with missing digits
    """
    x_check = False                     # Used to control weather an X appears

    
    for i in cardNumber:
        
        if i == 'X':
            x_check= True
                                        # Run the following block if an X appears
    if x_check:
        for i in range (10):
            x_check=False               # Check all values of X for one X at a time
            xList =[]
            for j in cardNumber:
                if j == 'X' and not x_check:
                    
                    xList.append(i)
                    x_check = True
                else:
                    xList.append(j)
                    
            all_x(xList)
    else:
        if is_valid(cardNumber):        # Print only the valid card numbers by calling is_valid function
            print(cardNumber)
        
    
cardNumber = "49927398716"
cardList = list(cardNumber)
#all_x(cardString)
is_valid(cardNumber)

              


