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