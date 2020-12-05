from turtle import *
from random import randrange
from freegames import square, vector

food1 = vector(0, 0)
food2 = vector(50, 10)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -500 < head.x < 390 and -500 < head.y < 390

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food1 or head == food2:
        print('Food1Storage:', len(snake))
        food1.x = randrange(-15, 15) * 10
        food1.y = randrange(-15, 15) * 10
        update()
    else: #head == food2:
        print('food2Storage:', len(snake))
        food2.x = randrange(-15, 15) * 10
        food2.y = randrange(-15, 15) * 10
        update()
        #print("total" , len(snake) + len(snake)+2)
    #else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'blue')

    square(food1.x, food1.y, 9, 'red')
    square(food2.x, food2.y, 9, 'purple')
    update()
    ontimer(move, 100)


hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()