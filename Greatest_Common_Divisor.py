a=int(input('please put in the first number'))
b=int(input('please put in the second number'))

def gcd(a,b):
    if b==0:
        return a
    elif a==0:
        return b
    else:
        return gcd(b,a % b)

if __name__ == '__main__':
    main()
    mainloop()

input()
    