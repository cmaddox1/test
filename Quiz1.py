print('QUESTION1')


def crazy_about_9(a,b):
    if a==9:
        return True
    elif b==9:
        return True
    elif b+a==9:
        return True
    elif b-a==9:
        return True
    elif a-b==9:
        return True
    else:
        return False

print(crazy_about_9(2, 9))
print(crazy_about_9(4, 5))
print(crazy_about_9(3, 8))


print('QUESTION2')


def leap_year(year):

    if (year % 400)==0:
        return True
    elif (year % 4)==0 and (year % 100)!=0:
        return True
   
    else:
        return False


print(leap_year(1900))
print(leap_year(2016))
print(leap_year(2017))
print(leap_year(2000))

print('Question 3')

def sum_squares(n):
    result = 1
    for i in range(n):
            result += i**2
    return result
print('print(sum_squares(1))')
print(sum_squares(1))
print('print(sum_squares(100))')
print(sum_squares(100))