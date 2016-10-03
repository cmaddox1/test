def isPalindrone(word):
    i=0
    while i <= len(word)/2:
	    if word[i] != word[-i - 1]:
		    return False
	    i+=1
	    return True

print(isPalindrone('hannah'))