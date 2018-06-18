from random import shuffle

deck = []
Nplayers = 3
pile =[]
talkative = True
player = [[] for i in range(Nplayers)]
penalty = 0
def beggar(Nplayers, deck, talkative):

    for i in range (4):                 #for each of the four suits
        for i in range (2,15):          #add cards from two to Ace
            deck.append(i)
    shuffle(deck)


    


    while len(deck)>Nplayers:

        for i in range(0, Nplayers):
            player[i].append(  deck.pop())
        if i == Nplayers:
            i ==0
        
    for i in range(0,len(deck)):
        
        player[i].append(deck.pop())
    turn()


def finished(player):
    for i in range(0,Nplayers):
##        if len(players[i]) == 52:
        if  len(pile) == 52:
            return True
        else:
            False


def turn():
    
    for i in range (0, Nplayers):
        
            

        print( i, player[i])
    j=-1
    while finished(player) != True:

        
    ##    for i in range(0,Nplayers):
        j +=1
        if j ==Nplayers:
            j=0
        if len(player[j]) == 0:
            j+=1
        penalty = player[j][0]

        if penalty >= 11:
            penalty = penalty%10
        else:
            penalty = 0
        
        if penalty > 0 and len (player[j]) >= penalty:
            pile.append(player[j].pop([0][0]))
            if j == Nplayers-1:
                    j=-1
            for i in range(0,penalty):
                    if len(player[j]) >= penalty:
                        j+=1
                        if j >= Nplayers:
                            j=0
                        break
                    pile.append(player[j+1].pop([0][0]))
                    
                    
                    
                    if player[j+1][0] >=11:
                        break                 #player takes pile here
                    
            for i in range(0, len(pile)-1):
                player[j].append(pile.pop(0))
            
                
                        
                        
        if len(player[j]) >= penalty:
           pile.append(player[j].pop([0][0]))

        

        
        
        print("pile: ", pile)
        print("penalty = ", penalty)
        print()
        for i in range (0, Nplayers):
            
            
            if i == j:
               print("* ",i, player[i])
            else:
                print("  ", i, player[i])
                
        finished(player)
        if finished(player)==True:
            break
    
    
    ##        print(players[i])

beggar(Nplayers, deck, talkative)

