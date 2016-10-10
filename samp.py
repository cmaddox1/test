# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()



def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:#this is used to check if the secretWord was guessed
      if letter not in lettersGuessed:
          return False
    return True
# When you've completed your function isWordGuessed, uncomment these three lines
# and run this file to test!

#secretWord = 'apple'
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(isWordGuessed(secretWord, lettersGuessed))

# Expected output:
# False
 
def getGuessedWord(secretWord, lettersGuessed):
    results=[]#this is used to collect the letters that have been guessed so the user knows how much of the word they have completed
    for letter in secretWord:
      if letter in lettersGuessed:
          results.append(letter)
      else:
          results.append('_')#this put's the underscore in for missing letters'
    print(results)
# When you've completed your function getGuessedWord, uncomment these three lines
# and run this file to test!

#secretWord = 'apple'
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(getGuessedWord(secretWord, lettersGuessed))

# Expected output:
# '_ pp_ e'


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # Hint: You might consider using string.ascii_lowercase, which
    # is a string comprised of all lowercase letters.

    # FILL IN YOUR CODE HERE...
    import string
    a=string.ascii_lowercase
    for letter in lettersGuessed:
      if len(lettersGuessed)==0:#this was put in for the start when the lettersGuessed has nothing in it because the if letter in a would not run if there are no letters in lettersGuessed
        return a
      if letter in a:
        a=a.replace(letter,'')#this replaces the missing letter with nothing 
    return a
# When you've completed your function getAvailableLetters, uncomment these two lines
# and run this file to test!

#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(getAvailableLetters(lettersGuessed))

# Expected output:
# abcdfghjlmnoqtuvwxyz
    
print('Let the games begin!')

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
        '''
    # FILL IN YOUR CODE HERE...
    
    print('Welcome to Hangman!')
    print('The number of letters in the word is...', len(secretWord))
    print('----------------------')
    MaxGuess=8 #sets the number of turns
    lettersGuessed=[]#collects the letters
    mx=len(lettersGuessed)#checks how many letters guessed so that it knows how many turns have been taken
    while mx < MaxGuess and isWordGuessed(secretWord, lettersGuessed) == False:#false statement added to break loop when game should end
        newlettersGuessed=[]#collects letters that get guessed
        newlettersGuessed=lettersGuessed#redefines the lettersGuessed variable so other functions know what to reference
        mx=len(newlettersGuessed)#changes the number of turns taken
        Maxguesses=(MaxGuess-mx)#says how many turns left
        print('You have %d guesses left' % Maxguesses )
        print('Available letters:',getAvailableLetters(lettersGuessed))
        letta = input('Please input a letter or guess the word')#used to collect the letter
        if letta == secretWord:#added this if statement so the player has the change to guess the whole word if they feel they know the answer
            break#this break stops the while loop so it can go to the end of the game if they are right
        newlettersGuessed.append(letta)#adds the letters to the previously guessed section 
        getGuessedWord(secretWord, lettersGuessed)
        isWordGuessed(secretWord, lettersGuessed)#checks to see if the word has been guessed
    if isWordGuessed(secretWord, lettersGuessed)==True or letta==secretWord:#there are two ways you can win, by guessing the word in one input or if you have guessed all the letters before running our of turns
        print('You Won')
    else:
        print('Sorry you lost, but good try!')
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
