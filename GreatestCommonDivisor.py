a=int(input('First Number'))
b=int(input('Second Number'))
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a % b)

if __name__ == '__main__':
    import doctest
    
print(gcd(a,b))
    