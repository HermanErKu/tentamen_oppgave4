import turtle, keyboard, time


turtle.speed(speed=10000)
turtle.showturtle()
turtle.title('Tentamen Oppgave 4b')

n = 3
height = 10
squareSize = 35


class objects:
    def square(size:int, xPos:int, yPos:int):
        turtle.penup()
        turtle.goto(xPos, yPos)
        turtle.pendown()
        for i in range(4):
            turtle.forward(size)
            turtle.right(90)

    def triangle(size:int, xPos:int, yPos:int):
        turtle.penup()
        turtle.goto(xPos, yPos)
        turtle.pendown()
        for i in range(3):
            turtle.forward(size)
            turtle.right(120)

    def line(xPosStart:int, yPosStart:int, xPosEnd:int, yPosEnd:int):
        turtle.penup()
        turtle.goto(xPosStart, yPosStart)
        turtle.pendown()
        turtle.goto(xPosEnd, yPosEnd)


startPosLastSquare = (n * squareSize) + squareSize
startPosFirstSquare = (-startPosLastSquare) + n*squareSize
startPosTopSquare = (n * squareSize) / 2
objects.square(squareSize, startPosFirstSquare, height)
objects.square(squareSize, startPosLastSquare, height)
objects.square(squareSize, startPosTopSquare, squareSize+10)

nn = (n+1)*squareSize

for i in range(0, nn, squareSize):
    for x in range(0, nn, squareSize):
        objects.square(squareSize, x, height)
    height -= squareSize 


turtle.hideturtle()

isPressed = False
while isPressed == False:
    if keyboard.is_pressed('q'):
        isPressed = True
