def factorz(a):
    results=[]
    if a==1:
        return a
    else:
        for i in range(2,a+1,1):
            while a % i==0:
                results.append(i)
                a=a/i

        return results
a=int(input('Please Put in the number'))
factorz(a)


