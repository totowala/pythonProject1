import turtle
import winsound

wn=turtle.Screen()
wn.title("Pone")
wn.bgcolor("black")
wn.setup(height=600,width=800)
wn.tracer(1)

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1,stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1,stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write(f"Player A score {score_a} Player B score {score_b}",align="center",font=("Arial",8,"normal"))

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

ball.dx = 2
ball.dy = 2

wn.listen()
wn.onkeypress(paddle_a_up,"u")
wn.onkeypress(paddle_a_down,"d")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")




while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
        score_b += 1
        winsound.PlaySound("Windows_Background.wav",winsound.SND_ASYNC)
        pen.clear()
        pen.write(f"Player A score {score_a} Player B score {score_b}",align="center",font=("Arial",12,"normal"))


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("Windows_Background.wav",winsound.SND_ASYNC)
        score_a += 1
        pen.clear()
        pen.write(f"Player A score {score_a} Player B score {score_b}",align="center",font=("Arial",12,"normal"))




