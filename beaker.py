##################################################
#
# def fart(x):
#     """This is a function for generating farts"""
#     for toots in range(x):
#         print("Toot")
#     if (x >= 10):
#         print("IMPRESSIVE!")
#
# x = int(input("How many beans did you eat? "))
# fart(x)
#
# print(fart.__doc__)
#

##################################################
#
# import turtle, random
# tess=turtle.Turtle()
# wn=turtle.Screen()
# rainbow = ["red", "orange", "yellow", "green", "blue", "violet"]
# tess.penup()
# tess.goto(-300,0)
# for sides in (3,4,6,8):
#    tess.penup()
#    tess.forward(100)
#    tess.pendown()
#    for i in range(sides):
#        tess.pencolor(random.choice(rainbow))
#        tess.forward(40)
#        tess.left(360/sides)
# wn.exitonclick()
##################################################
#Chapter 5 exercises
# Number 2
# import turtle
#
# def draw_square(t,side):
#     for i in range (4):
#         t.forward(side)
#         t.left(90)
# def rings(t, count, space, size):
#
#     for x in range(count):
#         draw_square(t,size)
#         size += space
#         t.up()
#         t.right(90)
#         t.forward(space/2)
#         t.right(90)
#         t.forward(space/2)
#         t.right(180)
#         t.down()
#
# def main():
#     wn = turtle.Screen()
#     wn.bgcolor("light green")
#     don = turtle.Turtle()
#     don.pencolor("pink")
#     don.pensize(3)
#
#     number_of_squares = 5
#     spacing = 20
#     initial_size = 20
#     rings(don, number_of_squares, spacing, initial_size)
#
#     wn.exitonclick()
#
# if __name__ == "__main__":
#     main()
##################################################
