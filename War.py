import random as r

# List containing the deck of cards
deck = ['H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13',
        'D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13',
        'C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13',
        'S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S12','S13',]

# Function Shuffling the deck
def shuffleDeck():

    r.shuffle(deck)
    return deck

shuffleDeck()

# Split the deck into two hands by splicing the deck at the middle

p1Hand = deck[:(len(deck))//2]

p2Hand = deck[(len(deck))//2:]

# Play the game

print('Lets Play War!!\n')

# Ends game when one player has an empty hand
while len(p1Hand) != 0 or len(p2Hand) != 0 :
    
    #Play card and display what card was played 
    
    #P1 Chooses
    while True:
        p1choice = input("Player 1"+
                        "\n1)Play your card"+
                        "\n2) Shuffle your hand"+
                        "\nQ) Quit"+
                        "\nEnter here: ")
        
        #Choose to play there card
        if p1choice == '1':

            p1played = p1Hand[0]
            print('\nPlayer 1 plays ' + p1played + "\n")
            break
        
        elif p1choice == '2':

            r.shuffle(p1Hand)
            print("\nYou shuffle your hand!\n")

        elif p1choice == 'Q' or p1choice == 'q':

            break

        else:

            print('Enter 1 to play or Q to quit please....')
    
    #P2 Chooses
    while True:
        p2choice = input("Player 2"+
                        "\n1)Play your card"+
                        "\n2) Shuffle your hand"+
                        "\nQ) Quit"+
                        "\nEnter here: ")
        
        #Choose to play there card
        if p2choice == '1':

            p2played = p2Hand[0]
            print('\nPlayer 2 plays ' + p2played + "\n")
            break

        elif p2choice == '2':

            r.shuffle(p2Hand)
            print("\nYou shuffle your hand!\n")

        elif p2choice == 'Q' or p2choice == 'q':
            
            break

        else:

            print('Enter 1 to play or Q to quit please....\n')
    
    #End program if players select q to quit       
    if p1choice == 'Q' or p1choice == 'q':

        break

    # Add both cards to winning list
    winnings = [p1played, p2played]

    #End program if players select q to quit       
    if p2choice == 'Q' or p2choice == 'q':

        break

    #Display what was played
    print("Player One plays: "+ p1played)
    print("Player Two plays: "+ p2played)

    #Compare the two played cards and add both cards to the end of the winners deck
    if int(p1played[1:]) > int(p2played[1:]) and int(p2played[1:]) != 1:

        print("P1 wins that round, the cards will be added to the end of your deck.\n")
        p1Hand.pop(0)
        p2Hand.pop(0)
        p1Hand.extend(winnings)

    elif int(p1played[1:]) < int(p2played[1:]) and int(p1played[1:]) != 1:

        print("P2 wins that round, the cards will be added to the end of your deck.\n")
        p1Hand.pop(0)
        p2Hand.pop(0)
        p2Hand.extend(winnings)
    
    #Aces
    elif int(p1played[1:]) == 1 and int(p2played[1:]) != 1:

        print("P1 wins that round, the cards will be added to the end of your deck.\n")
        p1Hand.pop(0)
        p2Hand.pop(0)
        p1Hand.extend(winnings)
    
    elif int(p2played[1:]) == 1 and int(p1played[1:]) != 1:

        print("P2 wins that round, the cards will be added to the end of your deck.\n")
        p1Hand.pop(0)
        p2Hand.pop(0)
        p2Hand.extend(winnings)

    # Ties
    elif int(p1played[1:]) == int(p2played[1:]):
        print("It's a TIE!! Go To WAR!")
        tie = True

        #Continue the I declare War sequence until tie is broken
        while tie:
            #Remove the cards that made the tie and add them to winnings
            p1Hand.pop(0)
            p2Hand.pop(0)

            #Add the first 3 cards in players hands to winnings and remove from deck
            for i in range(3):

                winnings.append(p1Hand[0])
                winnings.append(p2Hand[0])

                p1Hand.pop(0)
                p2Hand.pop(0)

            #Play the 4th card and add them to winnings
            p1played = p1Hand[0]
            p2played = p2Hand[0]
            winnings.extend([p1played,p2played])

            # Display cards played
            print(f"P1 declares {p1Hand[0]}")
            print(f"P2 declares {p2Hand[0]}")

            #Compare the 4th card
            if int(p1played[1:]) > int(p2played[1:]) and int(p2played[1:]) != 1:

                print("P1 wins that round, the cards will be added to the end of your deck.\n")
                p1Hand.pop(0)
                p2Hand.pop(0)
                p1Hand.extend(winnings)
                tie = False

            elif int(p1played[1:]) < int(p2played[1:]) and int(p1played[1:]) != 1:
            
                print("P2 wins that round, the cards will be added to the end of your deck.\n")
                p1Hand.pop(0)
                p2Hand.pop(0)
                p2Hand.extend(winnings)
                tie = False

            #Aces
            elif int(p1played[1:]) == 1 and int(p2played[1:]) != 1:
            
                print("P1 wins that round, the cards will be added to the end of your deck.\n")
                p1Hand.pop(0)
                p2Hand.pop(0)
                p1Hand.extend(winnings)
                tie = False

            elif int(p2played[1:]) == 1 and int(p1played[1:]) != 1:
            
                print("P2 wins that round, the cards will be added to the end of your deck.\n")
                p1Hand.pop(0)
                p2Hand.pop(0)
                p2Hand.extend(winnings)
                tie = False

            # If tie again repeat
            else:
                tie = True

    #Display amount of cards
    print("P1 has "+ str(len(p1Hand)) + " cards!")
    print("P2 has "+ str(len(p2Hand)) + " cards!")


if len(p1Hand) > len(p2Hand):

    print('P1 Wins!!! Thank you for playing!')

if len(p1Hand) < len(p2Hand):

    print('P2 Wins!!! Thank you for playing!')

if len(p1Hand) == len(p2Hand):

    print('Ended in a Tie!!! Thank you for playing!')