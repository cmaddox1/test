import turtle
import random 
import math

def drunkard_walk(x,y,n):
    t=turtle.Turtle()
    q=x
    r=y
    for i in range(n):
        t.rt(q)
        t.lt(q)
        t.fd(r)
        t.bk(r)
        z = random.choice(['east','west','north','south'])
        
        if z == 'east':
            q = q + 1
            t.rt(q)
        if z == 'west':
            q = q - 1
            t.lt(q)
            
        if z == 'north':
            r = r+1
            t.fd(r)
        if z == 'south':
            r = r-1
            t.bk(r)
    
    return math.sqrt((q-x)**2+(r-y)**2)
    turtle.mainloop()



x=int(input('please put in x cord'))
y=int(input('please put in y cord'))
n=int(input('please put in number of moves'))

print("The drunkard started from (%d,%d)." % (x, y))
distance = drunkard_walk(x, y, n)
print(" After", n, "intersections, he's",
      distance, "blocks from where he started.")