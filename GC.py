#Guess and Check 
x = int(input('Enter an integer: '))
if x<0:
    x=x*(-1)
else:
    ans = 0
    while ans**3 < x:
        ans = ans + 1
    if ans**3 != x:
        print(str(x) + ' is not a perfect cube')
    else:
        print('Cube root of ' + str(x) + ' is ' + str(ans))