print('QUESTION1')


def crazy_about_9(a,b):
    if a==9:
        print('true')
    elif b==9:
        print('true')
    elif b+a==9:
        print('true')
    elif b-a==9:
        print('true')
    elif a-b==9:
        print('true')
    else:
        print('False')

print(crazy_about_9(2, 9))
print(crazy_about_9(4, 5))
print(crazy_about_9(3, 8))


print('QUESTION2')


def leap_year(year):

    if (year % 4)==0 and (year % 100)!=0:
        print('True')
    elif (year/400)==int(x=10):
        print('true')
    else:
        print('False')


print(leap_year(1900))
print(leap_year(2016))
print(leap_year(2017))
print(leap_year(2000))

print('Question 3')

def sum_squares(n):
    result = 1
    for i in range(n):
        if i % 1 == 0:
            result += i**2
            print(result)
print('print(sum_squares(1))')
print(sum_squares(1))
print('print(sum_squares(100))')
print(sum_squares(100))