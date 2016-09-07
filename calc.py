print('Seconds in 42min 42sec')
print((42*60)+42)

print('Miles in 10kil')
print(10/1.61)

print('Average Pace per mile in minutes')
print((42+(42/60))/(10/1.61))

print('Average Pace per mile in seconds')
print(((42+(42/60))/(10/1.61))*60)

print('Average Speed')
print((42+(42/60))/(60/(10/1.61)))

print('Session 2 Question 1')
print('Volume of a Sphere')
x=5
pi=3.1415926
print('(4/3)πr^3=')
print((4/3)*pi*(x**3))
print('Question 2')
print('Books at 24.95 with 40% discount with $3 first shipping and $.75 after that')
Book_Price= 24.95
Discount=.6
First_Shipping=3
Second_Shipping=.75
Num_Books=60
print((Book_Price*Discount)*Num_Books+(First_Shipping+(Second_Shipping*(Num_Books-1))))

print('Question 3')
print('Time you get back from Breakfast')
print("Time of first mile in seconds=")
x=(8*60+15)
print(x)

print('Time of next 3 miles at 7:12 pace in seconds =')
y=(7*60*3+12*3)
print(y)
print('Time of last mile')
z=(8*60+15)
print(z)
print('Total Time of Run in Sec')
print(y+x+z)
tot=(x+y+z)#this is the total time of the run 
print('Initial Start Time in Seconds')
q=((6*60+52)*60)
print(q)
print('Time home for Breakfast in Seconds')
print(q+tot)
print('Time home in hours')
t=(((q+tot)/60)/60)#time home in hours
print(t)
print('Time home')
l=(t-7)*60
print('%s hr,%.0f min' % (7,l))
print('Question 4')
print('Percent change in Grade Average from 82-89')
New_avg=89
Old_avg=82
a=(((New_avg-Old_avg)/Old_avg)*100)
print('%.1f %%' % (a))
