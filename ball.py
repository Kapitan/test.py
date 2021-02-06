# apt-get install python3-tk
# pip3 install PythonTurtle

import turtle, random

window = turtle.Screen()

border = turtle.Turtle()
border.speed(0)
border.up()
border.hideturtle()
border.pensize(3)
border.color("green")
border.goto(300, 300)
border.down()
border.goto(300, -300)
border.goto(-300, -300)
border.goto(-300, 300)
border.goto(300, 300)

ball = turtle.Turtle()
ball.hideturtle()
#ball.up()
ball.shape("circle")
fx = random.randint(-200, 200)
fy = random.randint(-200, 200)

ball.goto(fx, fy)
ball.showturtle()
dx = 4
dy = 2

while True:
    x, y = ball.position()
    if x + dx >= 300 or x + dx <= -300:
        dx = -dx
    if y + dy >= 300 or y + dy <= -300:
        dy = -dy

    ball.goto(x + dx, y + dy)

window.mainloop()
