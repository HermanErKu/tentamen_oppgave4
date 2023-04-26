# Importerer alle nødvendige libraries
import turtle, keyboard


# Setter alle turtle innstillingene riktig
turtle.speed(speed=10000)
turtle.showturtle()
turtle.title('Tentamen Oppgave 4b')


# Innstillinger for hvordan tegningen kommer til å se ut
n = 3                   # Hvilket nummer figur skal den tegne
height = 10             # Hvilken høyde skal tegningen starte på
squareSize = 35         # Hvor stor skal firkantene i tegningen være


# Klasse med figurer som programmet kan tegne
class objects:
    # Funksjon for å tegne en firkant
    def square(size:int, xPos:int, yPos:int):
        turtle.penup()
        turtle.goto(xPos, yPos)
        turtle.pendown()
        for i in range(4):
            turtle.forward(size)
            turtle.right(90)

            
    # Funksjon for å tegne en trekant
    def triangle(size:int, xPos:int, yPos:int):
        turtle.penup()
        turtle.goto(xPos, yPos)
        turtle.pendown()
        for i in range(3):
            turtle.forward(size)
            turtle.right(120)

            
    # Funksjon for å tegne en strek
    def line(xPosStart:int, yPosStart:int, xPosEnd:int, yPosEnd:int):
        turtle.penup()
        turtle.goto(xPosStart, yPosStart)
        turtle.pendown()
        turtle.goto(xPosEnd, yPosEnd)


# Finner posisjon og tegner de 3 første firkantene, 1 på hver side av figuren og 1 på toppen av figuren
startPosLastSquare = (n * squareSize) + squareSize
startPosFirstSquare = (-startPosLastSquare) + n*squareSize
startPosTopSquare = (n * squareSize) / 2
objects.square(squareSize, startPosFirstSquare, height)
objects.square(squareSize, startPosLastSquare, height)
objects.square(squareSize, startPosTopSquare, squareSize+10)

nn = (n+1)*squareSize


for i in range(0, nn, squareSize):                  # Looper gjennom hvor mange firkanter det skal være nedover i det midterste kvadratet  (n+1)*(n+1)  og tegner en firkant
    for x in range(0, nn, squareSize):              # Looper gjennom hvor mange firkanter det skal være bortover i det midterste kvadratet  (n+1)*(n+1)  og tegner en firkant
        objects.square(squareSize, x, height)
    height -= squareSize 


# Lukker vindu med tegning hvis du trykker på 'q'
turtle.hideturtle()
isPressed = False
while isPressed == False:
    if keyboard.is_pressed('q'):
        isPressed = True
