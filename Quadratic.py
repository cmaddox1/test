#Building the Quadratic formula
def quad():
    from math import sqrt
    print()

    a= int(input('Put the first number'))
    b=int(input('Put in the second number'))
    c=int(input('Put the third number'))

    print('The Quadratic formula to solve for X is (-b)+- the sqruare root of(b^2-4ac) all divided by 2a')
    disc=b**2-4*a*c
    root=sqrt(disc)
    solution1=((-b)+root)/2*a #this is the positive
    solution2=((-b)-root)/2*a #this is the negative
    print('the solution it written with posive first then negative') 
    print(solution1)
    print(solution2)
 

input()
 