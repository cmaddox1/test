import turtle
t=turtle.Turtle()
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

square(t)
turtle.mainloop()  