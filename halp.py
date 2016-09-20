import turtle

from turtle import *

def yin(radius, color1, color2):
    width(3)
    color("black", color1)
    circle(radius/2., 180)
    circle(radius, 180)
    left(180)
    circle(-radius/2., 180)
    left(90)
    up()
    forward(radius*0.35)
    right(90)
    down()
    color(color1, color2)
    circle(radius*0.15)
    left(90)
    up()
    backward(radius*0.35)
    down()
    left(90)

def main():
    reset()
    yin(200, "black", "black")
    yin(200, "black", "black")
    ht()


if __name__ == '__main__':
    main()
    mainloop()