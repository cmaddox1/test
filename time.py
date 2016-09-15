import time
x=time.time()
y=60
z=60
a=24
v=365.25
q=((((x/y)/z)/a)/v) #time in years and remainder
g=%.0f % (q)
print(g)
input()