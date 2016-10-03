def factor():
    a=int(input('Please put in the number '))
    results=[]
    if a==1:
        return a
    else:
        for i in range(2,a+1,1):
            while a % i==0:
                results.append(i)
                a=a/i

    return results

print(factor())
