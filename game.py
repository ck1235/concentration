import random
       
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    # YOUR CODE GOES HERE
    print('Shuffling the deck...\n')
    random.shuffle(deck)

def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def board_stars(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='*'
    for i in range(len(board)):
          board[i]=letter
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')

def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()

def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    # YOUR CODE GOES HERE
    if original_board[p1]==original_board[p2]:
        discovered[p1] = original_board[p1]
        discovered[p2] = original_board[p2]
        print_board(discovered)
    else:
        discovered2 = discovered[:]
        discovered2[p1] = original_board[p1]
        discovered2[p2] = original_board[p2]
        print_board(discovered2)

        wait_for_player()
        print('\n'*35)
        print_board(discovered)

#############################################################################
#   FUNCTIONS FOR OPTION 2 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board

def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board = []

    l = sorted(l)                     #n*logn
    i = 0
    while i < len(l) - 1:             #logn
        c1 = l[i]
        c2 = l[i + 1]
        if c1 == c2 and c1 != '*':
            playable_board.append(c1) #1
            playable_board.append(c2) #1
            i = i+1
        i = i + 1       
    return playable_board

# O(n*logn) < O(n^2)

def is_rigorous(l):
    '''list of str->True or None
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''

    # YOUR CODE GOES HERE
    l = sorted(l)                #n * logn
    for i in range(len(l)-2):    #n
        if l[i] == l[i+2]:       #n
            return False         #<=1
    return True                  #<=1

# O(n*log(n)) < O(n^2)

def ascii_name_plaque(name):
    """(str) -> str
    Takes a string representing a person's name as input and prints a name plaque"""
    print ("*"*(len(name)+10))
    print ("*" + " "*(len(name)+8) +"*")
    print ("*  __" + str(name) +"__  *")
    print ("*" + " "*(len(name)+8) +"*")
    print ("*"*(len(name)+10))

###############################################################

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''
    print("Ready to play ...\n")

    if '*' not in board:
        size = len(board)
        stars = board_stars(size)
        shuffle_deck(board)

    discovered = stars
    original_board = board
    print_board(discovered)

    counter = 0
    
    while '*' in discovered:
        print('\nEnter two distinct positions on the board that you want revealed.\ni.e. two integers in the range [1, ' + str(size) + ']')
        p1 = int(input('Enter position 1: ')) - 1
        p2 = int(input('Enter position 2: ')) - 1
        while (p1<0 or p2<0) or (p1>=len(original_board)) or (p2>=len(original_board)):
            print('\nOne or both of your chosen positions is out of range.\nPlease try again. This guess did not count. Your current number of guesses is ' +str(counter) + '\nEnter two distinct positions on the board that you want revealed.\ni.e. two integers in the range [1, ' + str(size) + ']')
            p1 = int(input('Enter position 1: ')) - 1
            p2 = int(input('Enter position 2: ')) - 1
        if p1 == p2:
            print('One or both of your chosen positions has already been paired.\nYou chose the same positions.\nPlease try again. This guess did not count. Your current number of guesses is ' + str(counter))
        elif ('*' not in discovered[p1] or '*' not in discovered[p2]):
            print('One or both of your chosen positions has already been paired.\nPlease try again. This guess did not count. Your current number of guesses is '+ str(counter))
        else:
            print_revealed(discovered, p1, p2, original_board)
            counter += 1
    print('\nCongratulations! You completed the game with '+ str(counter) + ' guesses. That is ' + str(counter - len(board)//2) + ' more than the best possible.')


#main

# YOUR CODE TO GET A CHOICE 1 or CHOICE 2 from a player GOES HERE
ascii_name_plaque('Welcome to my Concentration game')
choice = int(input('Would you like (enter 1 or 2 to indicate your choice):\n(1) me to generate a rigorous deck of cards for you\n(2) or, would you like me to read a deck from a file?\n'))
while (choice!=1 and choice!=2):
    choice = int(input(str(choice) + ' is not an existing option. Please try again. Enter 1 or 2 to indicate your choice\n'))

# YOUR CODE FOR OPTION 1 GOES HERE
if choice==1:
    print('You chose to have a rigorous deck generated for you')
    size = int(input('\nHow many cards do you want to play with?\nEnter an even number between 2 and 52: '))
    while (size < 2 or size > 52 or size % 2 != 0):
        size = int(input('\nHow many cards do you want to play with?\nEnter an even number between 2 and 52: '))

    wait_for_player()
    board = create_board(size) #creates the board

    play_game(board)

# YOUR CODE FOR OPTION 2 GOES HERE
else:
    print("You chose to load a deck of cards from a file")
    file=input("Enter the name of the file: ")
    file=file.strip()
    board=read_raw_board(file)
    board=clean_up_board(board)

    if is_rigorous(board) == False:
        ascii_name_plaque("This deck is now playable but not rigorous and it has " + str(len(board)) + " cards")
    elif is_rigorous(board) == True:
        ascii_name_plaque("This deck is now playable and rigorous and it has " + str(len(board)) + " cards")
    wait_for_player()

    if len(board) == 0:
        shuffle_deck(board)
        print('The resulting board is empty.\nPlaying Concentration game with an empty board is impossible.\nGoodbye')
    else:
        play_game(board)
    
