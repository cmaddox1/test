list_1=[10,20]
AFC_east=['Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York jets']

a_nested_list = ['spam', 2.0,5, [10,20]]
print(AFC_east)
AFC_east[3]='New York Giants'
print(AFC_east)

print(AFC_east[0:2])
print(AFC_east[-2:])
print(AFC_east[2:4])

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    
]

numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    
print(numbers)


print(L[0][0])
print(L[2][2])
print(L[1][2][1])

for team in AFC_east:
    print(team)

my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(my_list))