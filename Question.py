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