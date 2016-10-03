def isPalindrome(s):
    i=0
    while i <= len(s)/2:
	    if s[i] != s[-i - 1]:
		    return False
	    i+=1
	    return True

inputStr = input("Enter a string: ")
if isPalindrome(inputStr):
    print("That's a palindrome.")
else:
    print("That isn't a palindrome.")