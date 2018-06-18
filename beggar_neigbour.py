from random import shuffle
def take_turn(player, pile):
    """The next player places a card onto the pile"""
    if len(pile) > 0 and pile[-1]>=11:      #following block executed if the last card is a penalty
        penalty = pile[-1]-10               #the penality value is the cards value minus ten
        for i in range(penalty):            #keep paying a penality...
            if len(player) > 0:             #...if you are still in the game
                card = player.pop(0)
                pile.append(card)           #fist card player holds becomes last on the pile
                if card >=11:
                    return player, pile, [] #another penalty appears, the next player must now pay a penalty
        return player, [], pile             #player is passed over
    else:
        pile.append(player.pop(0))          #first move
        return player, pile, []             #normal card played was paid

def create_deck():
    """Create a deck of cards without refernce to suit: 14 = Ace, 2 = two etc """
    deck = []
    for j in range (4):                 #for each of the four suits
        for i in range (2,15):          #add cards from two to Ace
            deck.append(i)
    return deck

def deal_deck(Nplayers, deck):
    """Give each player a card"""
    players = [[] for i in range(Nplayers)]     #create a list of lists to represent players hands
    for i in range(len(deck)):
        players[i % Nplayers].append(deck[i])   #iterate through deck, giving a card to each player
    return players
    
def beggar(Nplayers, deck, talkative):
    """Play a single game of Beggar your Neighbour"""
    players = deal_deck(Nplayers, deck)
    pile = []
    currentplayer = 0
    lastplayer = 0
    turn = 0

    while finished(players) != True:
        if len(players[currentplayer]) > 0:     #a player is out when they have no more cards
            turn += 1
            
            newplayer, newpile, reward = take_turn(players[currentplayer], pile)
            players[currentplayer] =  newplayer
            pile = newpile
            players[lastplayer] += reward       
            if talkative == True:               
                print("turn: ", turn)
                print("pile: ", pile)           #output showing all players and pile
                for i in range (Nplayers):               
                    if i == currentplayer:
                       print("* ",i, players[i]) #current player indicator
                    else:
                        print("  ", i, players[i])
            lastplayer = currentplayer
        currentplayer += 1
        if currentplayer >= Nplayers:           #when the last player has had a turn, start from the first player again
            currentplayer = 0
    return turn
    
def finished(players):
    """Check to see the game is actually over"""
    activeplayers = 0
    for player in players:
        if len(player) > 0:
            activeplayers += 1
    if activeplayers > 1:           #game is complete when one player holds the entire deck
        return False
    else:
        return True

if __name__ == "__main__":          #run a game for three players unless the program has been imported
    deck = create_deck()
    shuffle(deck)
    beggar(3, deck, True)

