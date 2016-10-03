def avoids(word, forbidden):
    """
    takes a word and a string of forbidden letters, and that returns True
    if the word doesn’t use any of the forbidden letters.
    """
    
    for letter in word:
        if letter in forbidden:
            return False
    return True

print(avoids('fat','abc'))