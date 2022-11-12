# Importing the turtle module
from turtle import *
from turtle import _CFG  # this dictionary to be imported separately
import random
import time
'''
Welcome to Tic-Tac-Toe by Josh!
You will be playing against a bot that does not use the random function

Unique Features:
- Choose your theme
- Exits on its own after the game ends
- Coloured text

'''
# WINNING CONDITION: 1,7,5,3

# Text Colours for Aesthetics
global PURPLE
global CYAN
global DARKCYAN
global BLUE
global GREEN
global RED
global YELLOW
global UNDERLINE
global BOLD
global END
global loser
global colourbg
loser = True
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\u001b[31m'
BOLD = '\033[1m'
BACKGROUND = '\u001b[44;1m'
BACKGROUND1 = '\u001b[41;1m'
UNDERLINE = '\033[4m'
END = '\033[0m'
winColour = (255, 13, 0)
_CFG["canvwidth"] = 1
_CFG["canvheight"] = 1
setup(400, 400)
title("Tic-Tac-Toe")
game = True
colormode(255)
backgroundColour = (31, 210, 255)
lineColour = (23, 158, 191)
XColour = (235, 235, 0)
OColour = (117, 235, 0)

bgcolor(backgroundColour)
numberz = (23, 158, 191)


# functions that will get called during game
def write():
    '''
  Function for Tutorial
  Turtles for each number on the grid during tutorial animation
  '''
    # hori 1
    write = True
    while write == True:
        num1 = Turtle()
        num1.speed(100)
        num1.hideturtle()
        num1.up()
        num1.goto(-150, 75)
        num1.color(numberz)

        num1.write("1", font=("Lemon", 50, "bold"))
        # hori 2
        num2 = Turtle()
        num2.speed(100)
        num2.hideturtle()
        num2.up()
        num2.goto(-25, 75)
        num2.color(numberz)
        num2.write("2", font=("Lemon", 50, "bold"))
        # hori 3
        num3 = Turtle()
        num3.speed(100)
        num3.hideturtle()
        num3.up()
        num3.goto(100, 75)
        num3.color(numberz)
        num3.write("3", font=("Lemon", 50, "bold"))
        # hori 2.1
        num4 = Turtle()
        num4.speed(100)
        num4.hideturtle()
        num4.up()
        num4.goto(-150, -50)
        num4.color(numberz)
        num4.write("4", font=("Lemon", 50, "bold"))
        # hori 2.2
        num5 = Turtle()
        num5.speed(100)
        num5.hideturtle()
        num5.up()
        num5.goto(-25, -50)
        num5.color(numberz)
        num5.write("5", font=("Lemon", 50, "bold"))
        # hori 2.3
        num6 = Turtle()
        num6.speed(100)
        num6.hideturtle()
        num6.up()
        num6.goto(100, -50)
        num6.color(numberz)
        num6.write("6", font=("Lemon", 50, "bold"))
        # hori 3.1
        num7 = Turtle()
        num7.speed(100)
        num7.hideturtle()
        num7.up()
        num7.goto(-150, -160)
        num7.color(numberz)
        num7.write("7", font=("Lemon", 50, "bold"))
        # hori 3.2
        num8 = Turtle()
        num8.speed(100)
        num8.hideturtle()
        num8.up()
        num8.goto(-25, -160)
        num8.color(numberz)
        num8.write("8", font=("Lemon", 50, "bold"))
        # hori 3.3
        num9 = Turtle()
        num9.speed(100)
        num9.hideturtle()
        num9.up()
        num9.goto(100, -160)
        num9.color(numberz)
        num9.write("9", font=("Lemon", 50, "bold"))
        # each string deletes and replaces itself!

        print(RED + "⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚ 0%", end="\r")
        time.sleep(.5)
        print("▧⬚⬚⬚⬚⬚⬚⬚⬚⬚ 10%", end="\r")
        time.sleep(.5)
        print("▧▧⬚⬚⬚⬚⬚⬚⬚⬚ 20%", end="\r")
        time.sleep(.25)
        print("▧▧▧⬚⬚⬚⬚⬚⬚⬚ 30%", end="\r")
        time.sleep(.25)
        print("▧▧▧▧⬚⬚⬚⬚⬚⬚ 40%", end="\r")
        time.sleep(.5)
        print("▧▧▧▧▧⬚⬚⬚⬚⬚ 50%", end="\r")
        time.sleep(.5)
        print("▧▧▧▧▧▧⬚⬚⬚⬚ 60%", end="\r")
        time.sleep(.5)
        print("▧▧▧▧▧▧▧⬚⬚⬚ 70%", end="\r")
        time.sleep(.1)
        print("▧▧▧▧▧▧▧▧⬚⬚ 80%", end="\r")
        time.sleep(.5)
        print("▧▧▧▧▧▧▧▧▧⬚ 90%", end="\r")
        time.sleep(.5)
        print(BOLD + "▩▩▩▩▩▩▩▩▩▩ 100%", end="\r" + END)
        time.sleep(.05)
        print("\n")  # new line
        time.sleep(1)  # time.sleep(.2) 3 seconds before next string starts

        num1.clear()
        num2.clear()
        num3.clear()
        num4.clear()
        num5.clear()
        num6.clear()
        num7.clear()
        num8.clear()
        num9.clear()

        break


def gridCreate():
    ''' 
  Creates the grid
  '''
    grid = Turtle()
    grid.color(lineColour)
    grid.speed(100)
    grid.width(7)
    grid.hideturtle()
    #line
    grid.penup()
    grid.goto(-60, -180)
    grid.pendown()
    grid.goto(-60, 180)
    #line
    grid.penup()
    grid.goto(60, 180)
    grid.pendown()
    grid.goto(60, -180)
    #line
    grid.penup()
    grid.goto(-180, 60)
    grid.pendown()
    grid.goto(180, 60)
    #line
    grid.penup()
    grid.goto(180, -60)
    grid.pendown()
    grid.goto(-180, -60)
    board = ["""1 2 3 4 5 6 7 8 9"""]
fork = Turtle()
fork.color("black")
fork.hideturtle()
fork.write("Game requires console to operate, \nfork the project to use the console.", align = "center")
time.sleep(3)
fork.color(backgroundColour)
fork.clear()

intro = True
print(BLUE + BOLD + UNDERLINE + BACKGROUND1 + "Tic-Tac-Toe by Josh Wu\n" + END)
setingss = False
name = input(GREEN + "Hello, what is your name?\n" + END + YELLOW + BOLD)

settings = True
numbers = ("1,2,3")


while intro == True:
    # While the intro is true
    global colourbg

    instructions = input(END + GREEN + "Welcome to Tic-tac-toe " + YELLOW +
                         BOLD + name.capitalize() + END + GREEN +
                         " type one of the numbers below to continue: \n" +
                         BOLD + UNDERLINE + RED + "1." + END + GREEN +
                         " for Tutorial\n" + BOLD + UNDERLINE + RED + '2.' +
                         END + GREEN + " to Play!\n" + BOLD + UNDERLINE + RED +
                         '3.' + END + GREEN + " for Settings!\n" + END +
                         YELLOW + BOLD)

    if instructions == '2':
        print(PURPLE + BOLD + "The Game has Started! \n" + END)
        break
    if instructions != '1' and instructions != '2' and instructions != '3':
        print(BOLD + UNDERLINE + RED +
              "Invalid Input\nThe required keys are: " + numbers + END + END +
              YELLOW + BOLD)

    if instructions == '1':

        print(
            GREEN +
            "Tic-tac-toe, noughts and crosses, or Xs and Os is a game for two players who take turns marking the spaces in a three-by-three grid with X or O. \n"
            + BOLD + YELLOW)
        time.sleep(3)

        print(
            END + GREEN +
            "To input your board position you will enter a value from 1-9 followed by the enter key!"
            + BOLD + YELLOW)
        time.sleep(3)

        print(BOLD + BACKGROUND +
              "\nPlease look at the screen for the grid positions!\n" + END +
              BOLD + YELLOW)
        # reprints
        time.sleep(2)
        grid = Turtle()
        grid.color(lineColour)
        grid.speed(100)
        grid.width(7)
        grid.hideturtle()
        #line
        grid.penup()
        grid.goto(-60, -180)
        grid.pendown()
        grid.goto(-60, 180)
        #line
        grid.penup()
        grid.goto(60, 180)
        grid.pendown()
        grid.goto(60, -180)
        #line
        grid.penup()
        grid.goto(-180, 60)
        grid.pendown()
        grid.goto(180, 60)
        #line
        grid.penup()
        grid.goto(180, -60)
        grid.pendown()
        grid.goto(-180, -60)
        write()
    if instructions == '3':
        setingss = True
        intro = False
        break
while setingss == True:
    colourbg = input(END + GREEN + UNDERLINE + "Select your theme:\n" + END +
                     BOLD + UNDERLINE + RED + "1." + END + GREEN +
                     " Halloween Theme\n" + BOLD + UNDERLINE + RED + '2.' +
                     END + GREEN + " Black and White\n" + BOLD + UNDERLINE +
                     RED + '3.' + END + GREEN + " Random Colours\n" + BOLD +
                     UNDERLINE + RED + '4.' + END + GREEN + " Play\n" + END +
                     YELLOW + BOLD)

    if colourbg == '1':
        bgcolor(255, 68, 0)
        lineColour = (86, 0, 94)
        XColour = (0, 0, 0)
        OColour = (227, 227, 0)
    if colourbg == '2':
        bgcolor(0, 0, 0)
        lineColour = (255, 255, 255)
        XColour = (255, 255, 255)
        OColour = (255, 255, 255)
    if colourbg == '3':
        r = random.randint(50, 255)
        g = random.randint(50, 255)
        b = random.randint(50, 255)
        bgcolor(r, g, b)
        XColour = (r, r, b)
        OColour = (g, g, r)
        lineColour = (g, b, r)
    if colourbg == '4':
        intro = True
        break


def o1():
    '''
  Circles from o1-o9()
  Circles will appear on the grid
  Self explanatory
  '''
    o1 = Turtle()
    o1.hideturtle()
    o1.width(7)
    o1.color(OColour)
    o1.speed(100)
    o1.penup()
    o1.goto(-125, 75)
    o1.pendown()
    o1.circle(50)


def o2():
    o2 = Turtle()
    o2.hideturtle()
    o2.width(7)
    o2.color(OColour)
    o2.speed(100)
    o2.penup()
    o2.goto(0, 75)
    o2.pendown()
    o2.circle(50)


def o3():
    o3 = Turtle()
    o3.hideturtle()
    o3.width(7)
    o3.color(OColour)
    o3.speed(100)
    o3.penup()
    o3.goto(125, 75)
    o3.pendown()
    o3.circle(50)


def o4():
    o4 = Turtle()
    o4.hideturtle()
    o4.width(7)
    o4.color(OColour)
    o4.speed(100)
    o4.penup()
    o4.goto(-125, -50)
    o4.pendown()
    o4.circle(50)


def o5():
    o5 = Turtle()
    o5.hideturtle()
    o5.width(7)
    o5.color(OColour)
    o5.speed(100)
    o5.penup()
    o5.goto(0, -50)
    o5.pendown()
    o5.circle(50)


def o6():
    o6 = Turtle()
    o6.hideturtle()
    o6.width(7)
    o6.color(OColour)
    o6.speed(100)
    o6.penup()
    o6.goto(125, -50)
    o6.pendown()
    o6.circle(50)


def o7():
    o7 = Turtle()
    o7.hideturtle()
    o7.width(7)
    o7.color(OColour)
    o7.speed(100)
    o7.penup()
    o7.goto(-125, -175)
    o7.pendown()
    o7.circle(50)


def o8():
    o8 = Turtle()
    o8.hideturtle()
    o8.width(7)
    o8.color(OColour)
    o8.speed(100)
    o8.penup()
    o8.goto(0, -175)
    o8.pendown()
    o8.circle(50)


def o9():
    o9 = Turtle()
    o9.hideturtle()
    o9.width(7)
    o9.color(OColour)
    o9.speed(100)
    o9.penup()
    o9.goto(125, -175)
    o9.pendown()
    o9.circle(50)


def x1():
    '''
  Xs from x1-x9()
  Xs will appear on the grid
  Self explanatory
  '''
    x1 = Turtle()
    x1.hideturtle()
    x1.width(7)
    x1.color(XColour)
    x1.speed(100)
    x1.penup()
    x1.goto(-175, 175)
    x1.pendown()
    x1.goto(-75, 75)
    x1.penup()
    x1.goto(-175, 75)
    x1.pendown()
    x1.goto(-75, 175)


def x2():
    x2 = Turtle()
    x2.hideturtle()
    x2.width(7)
    x2.color(XColour)
    x2.speed(100)
    x2.penup()
    x2.goto(-50, 175)
    x2.pendown()
    x2.goto(50, 75)
    x2.penup()
    x2.goto(50, 175)
    x2.pendown()
    x2.goto(-50, 75)


def x3():
    x3 = Turtle()
    x3.hideturtle()
    x3.width(7)
    x3.color(XColour)
    x3.speed(100)
    x3.penup()
    x3.goto(75, 175)
    x3.pendown()
    x3.goto(175, 75)
    x3.penup()
    x3.goto(175, 175)
    x3.pendown()
    x3.goto(75, 75)


def x4():
    x4 = Turtle()
    x4.hideturtle()
    x4.width(7)
    x4.color(XColour)
    x4.speed(100)
    x4.penup()
    x4.goto(-175, 50)
    x4.pendown()
    x4.goto(-75, -50)
    x4.penup()
    x4.goto(-75, 50)
    x4.pendown()
    x4.goto(-175, -50)


def x5():
    x5 = Turtle()
    x5.hideturtle()
    x5.width(7)
    x5.color(XColour)
    x5.speed(100)
    x5.penup()
    x5.goto(-50, 50)
    x5.pendown()
    x5.goto(50, -50)
    x5.penup()
    x5.goto(-50, -50)
    x5.pendown()
    x5.goto(50, 50)


def x6():
    x6 = Turtle()
    x6.hideturtle()
    x6.width(7)
    x6.color(XColour)
    x6.speed(100)
    x6.penup()
    x6.goto(75, 50)
    x6.pendown()
    x6.goto(175, -50)
    x6.penup()
    x6.goto(175, 50)
    x6.pendown()
    x6.goto(75, -50)


def x7():
    x7 = Turtle()
    x7.hideturtle()
    x7.width(7)
    x7.color(XColour)
    x7.speed(100)
    x7.penup()
    x7.goto(-175, -175)
    x7.pendown()
    x7.goto(-75, -75)
    x7.penup()
    x7.goto(-75, -175)
    x7.pendown()
    x7.goto(-175, -75)


def x8():
    x8 = Turtle()
    x8.hideturtle()
    x8.width(7)
    x8.color(XColour)
    x8.speed(100)
    x8.penup()
    x8.goto(-50, -175)
    x8.pendown()
    x8.goto(50, -75)
    x8.penup()
    x8.goto(-50, -75)
    x8.pendown()
    x8.goto(50, -175)


def x9():
    x9 = Turtle()
    x9.hideturtle()
    x9.width(7)
    x9.color(XColour)
    x9.speed(100)
    x9.penup()
    x9.goto(75, -175)
    x9.pendown()
    x9.goto(175, -75)
    x9.penup()
    x9.goto(175, -175)
    x9.pendown()
    x9.goto(75, -75)


def testCircles():  # organize tests
    o1()
    o2()
    o3()
    o4()
    o5()
    o6()
    o7()
    o8()
    o9()


def testX():  # organizes x tests
    x1()
    x2()
    x3()
    x4()
    x5()
    x6()
    x7()
    x8()
    x9()


def click1():
    '''
  Concept that I tried where I could click on the screen to place my board positions
  '''
    click1 = Turtle()
    # click1.hideturtle()
    click1.shape("square")
    click1.color(backgroundColour)
    click1.penup()
    click1.goto(-125, 125)
    click1.pendown()
    click1.shapesize(4, 4, 4)


def click2():
    '''
    Failed Function for clicking
  '''
    click2 = Turtle()
    click2.shape("square")
    click2.color(backgroundColour)
    click2.penup()
    click2.goto(0, 125)
    click2.pendown()
    click2.shapesize(4, 4, 4)


def click3():
    click3 = Turtle()
    click3.shape("square")
    click3.color(backgroundColour)
    click3.penup()
    click3.goto(125, 125)
    click3.pendown()
    click3.shapesize(4, 4, 4)


def click4():
    click4 = Turtle()
    click4.shape("square")
    click4.color(backgroundColour)
    click4.penup()
    click4.goto(-125, 0)
    click4.pendown()
    click4.shapesize(4, 4, 4)


def click5():
    click5 = Turtle()
    click5.shape("square")
    click5.color(backgroundColour)
    click5.penup()
    click5.goto(0, 0)
    click5.pendown()
    click5.shapesize(4, 4, 4)


def click6():
    click6 = Turtle()
    click6.shape("square")
    click6.color(backgroundColour)
    click6.penup()
    click6.goto(125, 0)
    click6.pendown()
    click6.shapesize(4, 4, 4)


def click7():
    click7 = Turtle()
    click7.shape("square")
    click7.color(backgroundColour)
    click7.penup()
    click7.goto(-125, -125)
    click7.pendown()
    click7.shapesize(4, 4, 4)


def click8():
    click8 = Turtle()
    click8.shape("square")
    click8.color(backgroundColour)
    click8.penup()
    click8.goto(0, -125)
    click8.pendown()
    click8.shapesize(4, 4, 4)


def click9():
    click9 = Turtle()
    click9.shape("square")
    click9.color(backgroundColour)
    click9.penup()
    click9.goto(125, -125)
    click9.pendown()
    click9.shapesize(4, 4, 4)


def clicks():  # testing function to check if they work
    click1()
    click2()
    click3()
    click4()
    click5()
    click6()
    click7()
    click8()
    click9()


def hori1():
    '''
  Horizontal wins drawing a red line!
  '''
    hori1 = Turtle()
    hori1.color(winColour)
    hori1.hideturtle()
    hori1.width(5)
    hori1.penup()
    hori1.goto(-175, 125)
    hori1.pendown()
    # hori1.setheading(90)
    hori1.speed(2)
    hori1.forward(350)


def hori2():
    '''
  Horizontal wins drawing a red line!
  '''
    hori2 = Turtle()
    hori2.color(winColour)
    hori2.hideturtle()
    hori2.width(5)
    hori2.penup()
    hori2.goto(-175, 0)
    hori2.pendown()
    # hori2.setheading(90)
    hori2.speed(2)
    hori2.forward(350)


def hori3():
    '''
  Horizontal wins drawing a red line!
  '''
    hori3 = Turtle()
    hori3.color(winColour)
    hori3.hideturtle()
    hori3.width(5)
    hori3.penup()
    hori3.goto(-175, -125)
    hori3.pendown()
    # hori3.setheading(90)
    hori3.speed(2)
    hori3.forward(350)


def vert1():
    '''
  Vertical wins drawing a red line!
  '''
    vert1 = Turtle()
    vert1.color(winColour)
    vert1.hideturtle()
    vert1.width(5)
    vert1.penup()
    vert1.goto(-125, 175)
    vert1.setheading(270)
    vert1.pendown()
    vert1.speed(2)
    vert1.forward(350)


def vert2():
    '''
  Vertical wins drawing a red line!
  '''
    vert2 = Turtle()
    vert2.color(winColour)
    vert2.hideturtle()
    vert2.width(5)
    vert2.penup()
    vert2.goto(0, 175)
    vert2.setheading(270)
    vert2.pendown()
    vert2.speed(2)
    vert2.forward(350)


def vert3():
    '''
  Vertical wins drawing a red line!
  '''
    vert3 = Turtle()
    vert3.color(winColour)
    vert3.hideturtle()
    vert3.width(5)
    vert3.penup()
    vert3.goto(125, 175)
    vert3.setheading(270)
    vert3.pendown()
    vert3.speed(2)
    vert3.forward(350)


def diag1():
    '''
  Diagonal wins drawing a red line!
  '''
    diag1 = Turtle()
    diag1.color(winColour)
    diag1.hideturtle()
    diag1.width(5)
    diag1.penup()
    diag1.goto(-150, 150)
    diag1.pendown()
    diag1.speed(2)
    diag1.goto(150, -150)


def diag2():
    '''
  Diagonal wins drawing a red line!
  '''
    diag2 = Turtle()
    diag2.color(winColour)
    diag2.hideturtle()
    diag2.width(5)
    diag2.penup()
    diag2.goto(150, 150)
    diag2.pendown()
    diag2.speed(2)
    diag2.goto(-150, -150)


def imp():
    '''
  failed concept for impossible level
  '''
    imp = Turtle()
    imp.hideturtle()
    imp.width(7)
    imp.color(OColour)
    imp.speed(100)
    imp.penup()
    imp.goto(250, -50)
    imp.pendown()
    imp.circle(50)


while game == True:
    # always creates the grid when the game is true
    gridCreate()

    # write()

    break
#console
# intro = True
# while intro == True:
#   print("Hello, welcome to Tic-Tac-Toe by Josh Wu!\nYou will see the Tic-tac-toe grid on the screen while you input the board position here!")
#   instructions = input("Would you like to see the board positions?  y/n")
#   if instructions == 'y':
#     write()
#     time.sleep(2)
#     clicks()
#     intro = False
#     break

# imp10 = False
# while imp10 == True:
#   input2 = input( END + RED + "Enter a valid board position!")
# impossible = False
# firstimp = False
# i1 = True
# i2 = True
# i3 = True

# while impossible == True:
#   if o1 == True or o2 == True or o3 == True or o4 == True or o5 == True or o6 == True or o7 == True or o8 == True or o9 == True and i1 == False:
#     o5()
#     i1 = True
#     firstimp = True
#   elif o1 == True or o2 == True or o3 == True or o4 == True or o5 == True or o6 == True or o7 == True or o8 == True or o9 == True and i2 == False:
#     o6()
#     i2 = True
#     secondimp = True
#   elif o1 == True or o2 == True or o3 == True or o4 == True or o5 == True or o6 == True or o7 == True or o8 == True or o9 == True and i3 == False:
#     imp()
#     i3 = True
#     thirdimp = True
# # turn
# while impossible == False:

#   if x1 == True or o1 == True:
#     impossible = True
#   elif input2 == '1' and o1 != True:
#     x1()
#     x1 = True
#     impossible = False

#   if x2 == True or o2 == True:
#     impossible = True
#   elif input2 == '2' and o2 != True:
#     x2()
#     x2 = True
#     impossible = False

#   if x3 == True or o3 == True:
#     impossible = True
#   elif input2 == '3'and o3 != True:
#     x3()
#     x3 = True
#     impossible = False

#   if x4 == True or o4 == True:
#     impossible = True
#   elif input2 == '4'and o4 != True:
#     x4()
#     x4 = True
#     impossible = False

#   if x5 == True or o5 == True:
#     impossible = True
#   elif input2 == '5'and o5 != True:
#     x5()
#     x5 = True

#     impossible = False

#   if x6 == True or o6 == True:
#     impossible = True
#   elif input2 == '6'and o6 != True:
#     x6()
#     x6 = True
#     impossible = False

#   if x7 == True or o7 == True:
#     impossible = True
#   elif input2 == '7'and o7 != True:
#     x7()
#     x7 = True
#     impossible = False

#   if x8 == True or o8 == True:
#     impossible = True
#   elif input2 == '8'and o8 != True:
#     x8()
#     x8 = True
#     impossible = False

#   if x9 == True or o9 == True:
#     impossible = True
#   elif input2 == '9'and o9 != True:
#     x9()
#     x9 = True
#     impossible = False

#   else:
#     impossible = True
#   # end

turn = True
botTurn = True

# if intructions == '3':
#   print(PURPLE + BOLD + "Let the Games Begin! \n" + END)
#   impossible = True

# player winning conditions
# go here
# not created yet
# X horizontal wins


def botTurn():
    '''
  The bots turn, biggest function in my code
  '''
    time.sleep(.5)
    global turn
    global o1
    global o2
    global o3
    global o4
    global o5
    global o6
    global o7
    global o8
    global o9
    global win
    global loser
    win = False
    loser = True
    if turn == True:
        pass
    while turn == False:
        #winning conditions go first
        # 1st Row Horiszontal win
        if x1 == True and x2 == True and x3 == True:
            hori1()
            turn = True
            win = True
            break
        elif x4 == True and x5 == True and x6 == True:
            hori2()
            turn = True
            win = True
            break
        elif x7 == True and x8 == True and x9 == True:
            hori3()
            turn = True
            win = True
            break
        # vertical
        elif x1 == True and x4 == True and x7 == True:
            vert1()
            turn = True
            win = True
            break
        elif x2 == True and x5 == True and x8 == True:
            vert2()
            turn = True
            win = True
            break
        elif x3 == True and x6 == True and x9 == True:
            vert3()
            turn = True
            win = True
            break
        # diagxnal
        elif x1 == True and x5 == True and x9 == True:
            diag1()
            turn = True
            win = True
            break
        elif x3 == True and x5 == True and x7 == True:
            diag2()
            turn = True
            win = True
            break

        # strat
        if o1 == True and o2 == True and x3 != True and o3 != True:
            o3()
            o3 = True
            turn = True
            # win
        elif o1 == True and o3 == True and o2 != True and x2 != True:
            o2()
            o2 = True
            turn = True
        # win
        elif o2 == True and o3 == True and x1 != True and o1 != True:
            o1()
            o1 = True
            turn = True
        # win
        # 2nd Row Horizontal win
        elif o4 == True and o5 == True and x6 != True and o6 != True:
            o6()
            o6 = True
            turn = True
        elif o4 == True and o6 == True and x5 != True and o5 != True:
            o5()
            o5 = True
            turn = True
        elif o5 == True and o6 == True and x4 != True and o4 != True:
            o4()
            o4 = True
            turn = True
        # 3rd Row Horizontal win
        elif o7 == True and o8 == True and x9 != True and o9 != True:
            o9()
            o9 = True
            turn = True
        elif o7 == True and o9 == True and x8 != True and o8 != True:
            o8()
            o8 = True
            turn = True
        elif o8 == True and o9 == True and o7 != True and x7 != True:
            o7()
            o7 = True
            turn = True
        # 1st Column Vertical Win
        elif o1 == True and o4 == True and o7 != True and x7 != True:
            o7()
            o7 = True
            turn = True
        elif o1 == True and o7 == True and o4 != True and x4 != True:
            o4()
            o4 = True
            turn = True
        elif o4 == True and o7 == True and o1 != True and x1 != True:
            o1()
            o1 = True
            turn = True
        # 2nd Column Vertical Win
        elif o2 == True and o5 == True and o8 != True and x8 != True:
            o8()
            o8 = True
            turn = True
        elif o2 == True and o8 == True and o5 != True and x5 != True:
            o5()
            o5 = True
            turn = True
        elif o5 == True and o8 == True and o2 != True and x2 != True:
            o2()
            o2 = True
            turn = True
        # 3rd Column Vertical Win
        elif o3 == True and o6 == True and o9 != True and x9 != True:
            o9()
            o9 = True
            turn = True
        elif o3 == True and o9 == True and o6 != True and x6 != True:
            o6()
            o6 = True
            turn = True
        elif o6 == True and o9 == True and o3 != True and x3 != True:
            o3()
            o3 = True
            turn = True
# diagonal wins /
        elif o3 == True and o5 == True and o7 != True and x7 != True:
            o7()
            o7 = True
            turn = True
        elif o3 == True and o7 == True and o5 != True and x5 != True:
            o5()
            o5 = True
            turn = True
        elif o7 == True and o5 == True and o3 != True and x3 != True:
            o3()
            o3 = True
            turn = True


# diagonal wins  \
        elif o1 == True and o5 == True and o9 != True and x9 != True:
            o9()
            o9 = True
            turn = True
        elif o5 == True and o9 == True and o1 != True and x1 != True:
            o1()
            o1 = True
            turn = True
        elif o1 == True and o9 == True and o5 != True and x5 != True:
            o5()
            o5 = True
            turn = True

    # defends top row horizontal
        elif x1 == True and x2 == True and x3 != True and o3 != True:
            o3()
            o3 == True
            turn = True
        elif x2 == True and x3 == True and x1 != True and o1 != True:
            o1()
            o1 = True
            turn = True
        elif x1 == True and x3 == True and x2 != True and o2 != True:
            o2()
            o2 = True
            turn = True
        # defend 2nd row horizontal
        elif x4 == True and x5 == True and x6 != True and o6 != True:
            o6()
            o6 = True
            turn = True
        elif x5 == True and x6 == True and x4 != True and o4 != True:
            o4()
            o4 = True
            turn = True
        elif x4 == True and x6 == True and x5 != True and o5 != True:
            o5()
            o4 = True
            turn = True
        # defend 3rd row horizontal
        elif x7 == True and x8 == True and x9 != True and o9 != True:
            o9()
            o9 = True
            turn = True
        elif x7 == True and x9 == True and x8 != True and o8 != True:
            o8()
            o8 = True
            turn = True
        elif x8 == True and x9 == True and x7 != True and o7 != True:
            o7()
            o7 = True
            turn = True
        # defend 1st column
        elif x1 == True and x4 == True and x7 != True and o7 != True:
            o7()
            o7 = True
            turn = True
        elif x1 == True and x7 == True and x4 != True and o4 != True:
            o4()
            o4 = True
            turn = True
        elif x4 == True and x7 == True and x1 != True and o1 != True:
            o1()
            o1 = True
            turn = True
        # defend 2nd column
        elif x2 == True and x5 == True and x8 != True and o8 != True:
            o8()
            o8 = True
            turn = True
        elif x2 == True and x8 == True and x5 != True and o5 != True:
            o5()
            o5 = True
            turn = True
        elif x5 == True and x8 == True and x2 != True and o2 != True:
            o2()
            o2 = True
            turn = True
        # defend 3rd column
        elif x3 == True and x6 == True and x9 != True and o9 != True:
            o9()
            o9 = True
            turn = True
        elif x3 == True and x9 == True and x6 != True and o6 != True:
            o6()
            o6 = True
            turn = True
        elif x6 == True and x9 == True and x3 != True and o3 != True:
            o3()
            o3 = True
            turn = True
        # defend on diagonal down \
        elif x1 == True and x5 == True and x9 != True and o9 != True:
            o9()
            o9 = True
            turn = True
        elif x1 == True and x9 == True and x5 != True and o5 != True:
            o5()
            o5 = True
            turn = True
        elif x5 == True and x9 == True and x1 != True and o1 != True:
            o1()
            o1 = True
            turn = True
        # defend on diagonal up /
        elif x3 == True and x5 == True and x7 != True and o7 != True:
            o7()
            o7 = True
            turn = True
        elif x3 == True and x7 == True and x5 != True and o5 != True:
            o5()
            o5 = True
            turn = True
        elif x5 == True and x7 == True and x3 != True and o3 != True:
            o3()
            o3 = True
            turn = True
        # strategy
        elif x1 != True and x2 == True and x3 == True and o1 != True:
            o1()
            o1 = True
            turn == True
        elif x1 == True and x4 == True and x7 != True and o7 != True:
            o7()
            o7 = True
            turn = True
        elif x1 == True and x2 != True and o2 != True or x1 == True and x3 == True and x2 != True and o2 != True:
            o2()
            o2 = True
            turn = True
        elif x3 == True and x9 == True and x6 != True and o6 != True:
            o6()
            o6 = True
            turn = True

        elif x1 == True and x2 == True and o3 != True or x9 == True and x6 == True and o3 != True or x7 == True and x5 == True and o3 != True:
            o3()
            o3 = True
            turn == True
        elif x1 == True and x7 == True and o4 != True and x4 != True:
            o4()
            o4 = True
            turn = True
        # elif x9 == True and x8 != True and o8 != True:
        #   o8()
        #   o8 == True
        #   turn = True

        elif x7 == True and x8 != True and o8 != True:
            o8()
            o8 = True
            turn = True

        elif x7 == True and x9 == True and x8 != True and o8 != True:
            o8()
            o8 = True
            turn = True

        elif o2 == True and o4 == True and x8 != True and o8 != True:
            o8()
            o8 = True
            turn = True
        elif x5 == True and o5 != True and o3 != True and x3 != True:
            o3()
            o3 = True
            turn = True
        elif x5 == True and o5 != True and o2 != True and x2 != True:
            o2()
            o2 = True
            turn = True
        elif x5 == True and o5 != True and o9 != True and x9 != True:
            o9()
            o9 = True
            turn = True
        elif x5 == True and o5 != True and o7 != True and x7 != True:
            o7()
            o7 = True
            turn = True
        elif x5 != True and o5 != True:
            o5()
            o5 = True
            turn = True
        elif x8 == True and o9 != True and x9 != True:
            o9()
            o9 = True
            turn = True
        elif x4 != True and o4 != True and x1 == True:
            o4()
            o4 = True
            turn = True
        elif x2 == True and x6 == True and x9 != True and o8 != True:
            o7()
            o7 = True
            turn = True

        # filler last
        elif x1 == True and o4 != True and x4 != True:
            o4()
            o4 = True
            turn = True

        elif x5 == True and x4 != True and o4 != True:
            o4()
            o4 = True
            turn = True
        elif x5 == True and x7 != True and o7 != True:
            o7()
            o7 = True
            turn = True
        elif x2 == True and x3 != True and o3 != True:
            o3()
            o3 = True
            turn = True
        elif x5 == True and x4 != True and o4 != True:
            o4()
            o4 = True
        elif x9 == True and x5 != True and o5 != True and o1 != True and x1 != True:
            o1()
            o1 = True
            turn = True
        elif x5 == True and x8 == True and o5 == True and o7 != True and x7 != True:
            o7()
            o7 = True
            turn = True

        elif x4 == True and x2 != True and o2 != True:
            o2()
            o2 = True
            turn = True
        elif o5 == True and o8 != True and x8 != True:
            o8()
            o8 = True
            turn = True
        else:
            print("Tie Game!")
            win = Turtle()
            win.shape("square")
            # win.hideturtle()
            win.goto(0, 0)
            win.color("cyan")
            win.shapesize(4, 7, 7)
            youlose = Turtle()
            youlose.hideturtle()
            youlose.penup()
            youlose.goto(0, -20)
            youlose.pendown()
            youlose.write("You Tied!",
                          align="center",
                          font=("Verdana", 20, "bold"))
            loser = False
            time.sleep(3)
            print(END + YELLOW + "Exiting in " + BACKGROUND1 + "5", end="\r")
            time.sleep(1)
            print(END + YELLOW + "Exiting in " + BACKGROUND1 + "4", end="\r")
            time.sleep(1)
            print(END + YELLOW + "Exiting in " + BACKGROUND1 + "3", end="\r")
            time.sleep(1)
            print(END + YELLOW + "Exiting in " + BACKGROUND1 + "2", end="\r")
            time.sleep(1)
            print(END + YELLOW + "Exiting in " + BACKGROUND1 + "1", end="\r")
            time.sleep(1)
            print(END + PURPLE + BOLD + "Play Again by Relaunching Game!" +
                  BACKGROUND1 + BOLD)
            exit()
            # winning conditions
            break

while turn == True:  #users turn
    intro = False
    input1 = input(END + GREEN + 'Please a valid board position!\n' + BOLD +
                   YELLOW)

    global win
    if x1 == True or o1 == True:
        turn = True
    elif input1 == '1' and o1 != True:
        x1()
        x1 = True
        turn = False
        botTurn()
    if x2 == True or o2 == True:
        turn = True
    elif input1 == '2' and o2 != True:
        x2()
        x2 = True
        turn = False
        botTurn()
    if x3 == True or o3 == True:
        turn = True
    elif input1 == '3' and o3 != True:
        x3()
        x3 = True
        turn = False
        botTurn()
    if x4 == True or o4 == True:
        turn = True
    elif input1 == '4' and o4 != True:
        x4()
        x4 = True
        turn = False
        botTurn()
    if x5 == True or o5 == True:
        turn = True
    elif input1 == '5' and o5 != True:
        x5()
        x5 = True

        turn = False
        botTurn()
    if x6 == True or o6 == True:
        turn = True
    elif input1 == '6' and o6 != True:
        x6()
        x6 = True
        turn = False
        botTurn()
    if x7 == True or o7 == True:
        turn = True
    elif input1 == '7' and o7 != True:
        x7()
        x7 = True
        turn = False
        botTurn()
    if x8 == True or o8 == True:
        turn = True
    elif input1 == '8' and o8 != True:
        x8()
        x8 = True
        turn = False
        botTurn()
    if x9 == True or o9 == True:
        turn = True
    elif input1 == '9' and o9 != True:
        x9()
        x9 = True
        turn = False
        botTurn()
    else:
        turn = True
    # winning conditions
    if x1 == True and x2 == True and x3 == True:
        hori1()
        turn = True
        win = True
        break
    elif x4 == True and x5 == True and x6 == True:
        hori2()
        turn = True
        win = True
        break
    elif x7 == True and x8 == True and x9 == True:
        hori3()
        turn = True
        win = True
        break
    # vertical
    elif x1 == True and x4 == True and x7 == True:
        vert1()
        turn = True
        win = True
        break
    elif x2 == True and x5 == True and x8 == True:
        vert2()
        turn = True
        win = True
        break
    elif x3 == True and x6 == True and x9 == True:
        vert3()
        turn = True
        win = True
        break
    # diagonal
    elif x1 == True and x5 == True and x9 == True:
        diag1()
        turn = True
        win = True
        break
    elif x3 == True and x5 == True and x7 == True:
        diag2()
        turn = True
        win = True
        break
    # -----
    elif o1 == True and o2 == True and o3 == True:
        hori1()
        turn = True
        win = False
        break
    elif o4 == True and o5 == True and o6 == True:
        hori2()
        turn = True
        win = False
        break
    elif o7 == True and o8 == True and o9 == True:
        hori3()
        turn = True
        win = False
        break
    # vertical
    elif o1 == True and o4 == True and o7 == True:
        vert1()
        turn = True
        win = False
        break
    elif o2 == True and o5 == True and o8 == True:
        vert2()
        turn = True
        win = False
        break
    elif o3 == True and o6 == True and o9 == True:
        vert3()
        turn = True
        win = False
        break
    # diagonal
    elif o1 == True and o5 == True and o9 == True:
        diag1()
        turn = True
        win = False
        break
    elif o3 == True and o5 == True and o7 == True:
        diag2()
        turn = True
        win = False
        break

if win == True:  # winning condition
    print("You Win!")
    win = Turtle()
    win.shape("square")
    # win.hideturtle()
    win.goto(0, 0)
    win.color("cyan")
    win.shapesize(4, 7, 7)
    youWin = Turtle()
    youWin.hideturtle()
    youWin.penup()
    youWin.goto(0, -20)
    youWin.pendown()
    youWin.write("You Win!", align="center", font=("Verdana", 20, "bold"))
    time.sleep(3)
    print(END + YELLOW + "Exiting in " + BACKGROUND1 + "5", end="\r")
    time.sleep(1)
    print(END + YELLOW + "Exiting in " + BACKGROUND1 + "4", end="\r")
    time.sleep(1)
    print(END + YELLOW + "Exiting in " + BACKGROUND1 + "3", end="\r")
    time.sleep(1)
    print(END + YELLOW + "Exiting in " + BACKGROUND1 + "2", end="\r")
    time.sleep(1)
    print(END + YELLOW + "Exiting in " + BACKGROUND1 + "1", end="\r")
    time.sleep(1)
    print(END + PURPLE + BOLD + "Play Again by Relaunching Game!" +
          BACKGROUND1 + BOLD)
    exit()

elif win == False and loser != False:  # losing condition
    print("You Lost!")
    lol = Turtle()
    lol.shape("square")
    # lol.hideturtle()
    lol.goto(0, 0)
    lol.color("cyan")
    lol.shapesize(4, 7, 7)
    youlose = Turtle()
    youlose.hideturtle()
    youlose.penup()
    youlose.goto(0, -20)
    youlose.pendown()
    youlose.write("You lose!", align="center", font=("Verdana", 20, "bold"))
    time.sleep(3)
    print(END + YELLOW + "Exiting in " + BACKGROUND1 + "5", end="\r")
    time.sleep(1)
    print(END + YELLOW + "Exiting in " + BACKGROUND1 + "4", end="\r")
    time.sleep(1)
    print(END + YELLOW + "Exiting in " + BACKGROUND1 + "3", end="\r")
    time.sleep(1)
    print(END + YELLOW + "Exiting in " + BACKGROUND1 + "2", end="\r")
    time.sleep(1)
    print(END + YELLOW + "Exiting in " + BACKGROUND1 + "1", end="\r")
    time.sleep(1)
    print(END + PURPLE + BOLD + "Play Again by Relaunching Game!" +
          BACKGROUND1 + BOLD)
    exit()
else:
    turn = True

done()  # finally
