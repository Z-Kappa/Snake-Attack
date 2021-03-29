#### FOR SCHOOL ####
from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0) #starting position of the food (x, y) from center
snake = [vector(10, 0)] #starting postion of snake each 'block' is 10 pixels
aim = vector(0, -10) #initial direction, 

def change(x, y): #Direction input
    "Change snake direction."
    aim.x = x #x = horizontal
    aim.y = y #y = vertical

def inside(head): #make sure snake is in window
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move(): #orients snake
    "Move snake forward one segment."
    head = snake[-1].copy() #moves first vector in snkae (the head)
    head.move(aim) #head moves where aimed 

    if not inside(head) or head in snake: #when head is in snkae or isnt in head 
        square(head.x, head.y, 9, 'red') #make snake red 
        update() #kill snake
        return

    snake.append(head) #add a box from aray to head

    if head == food: #when snake in food, make now food
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10  #creates food randomly in a 10x10 grid. 
        food.y = randrange(-15, 15) * 10  #^
    else:
        snake.pop(0)  #keeps head toghter 

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black') #aquare(type.x, tpye.y, size, 'color')

    square(food.x, food.y, 9, 'green')      #^^
    update()
    ontimer(move, 100) #on timer (move, amount) (large# - slow, small# -fast)

setup(420, 420, 370, 0) #(width, height, ?, ?)
hideturtle()  #Hides turtle
tracer(False) #Hides turtle drawing
listen()
onkey(lambda: change(10, 0), 'Right') #Establishes right and left
onkey(lambda: change(-10, 0), 'Left') #^
onkey(lambda: change(0, 10), 'Up')    #Establishes up and down
onkey(lambda: change(0, -10), 'Down') #^
move()
done()