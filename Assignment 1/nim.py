#
# You need to replace 'pass' with your code
#


from random import randint
from math import log

# Define constant variables.
HUMAN = 0
COMPUTER = 1
SMART = 0
DUMB = 1

# Create the initial pile, determine the starting player and the computer's
# strategy.



def nim():
    """
    return True if the winner is human, False if winner is computer.
    """
    # While the game is still being played.
    
    pile = randint(10, 100)
    turn = randint(0, 1)
    strategy = randint(0, 1)
    while pile > 0:
        if turn == COMPUTER:
            if pile == 1:
                # Take the last marble.
                return False
            elif strategy == DUMB:
                # Take a random, legal number of marbles from the pile.
                take=randint(1,(pile/2))
                pile=pile-take
            elif pile == 3 or pile == 7 or pile == 15 or pile == 31 or pile == 63:
                # The computer is smart, but can't make a smart move.
                # Take a random, legal number of marbles from the pile.
                take=randint(1,(pile/2))
                pile=pile-take
            else:
                # The computer is smart and can make a smart move.
                # Take marbles so that the pile will be be a power of 2, minus
                # 1.
                goodlist=[3,7,15,31,63]
                n=int((log(pile+1))/log(2)) #this solves for the power of 2 that is half 
                g=n-2 #this determines the number on the list to pull
                take = pile - goodlist[g]


            # Update pile
            pile=pile-take
            print("The computer took %d marbles, leaving %d.\n" % (take, pile))
            # take is the variable you might need above
            turn = HUMAN

        elif turn == HUMAN:
            print("Your turn.   The pile currently has", pile, "marbles in it.")

            take = int(input("How many marbles will you take? "))
            # Force the user to take a legal number of marbles.
            if take>(pile/2):
                print('Invalid Number')
                take = int(input("Please input new number. "))
            else:
                # Update pile
                    pile=pile-take
            print("Now the pile has", pile, "marbles in it.\n")
            turn = COMPUTER

    return turn == COMPUTER

if nim():
    print("You Won!")
else:
    print("The computer won!")