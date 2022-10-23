import turtle
import os


wn = turtle.Screen()
wn.title("Ping Pong Game!!")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


side_a = turtle.Turtle()
side_a.speed(0) #speed Animation
side_a.shape("square")
side_a.color("white")
side_a.penup()
side_a.goto(-350, 0)
side_a.shapesize(stretch_wid=5, stretch_len=0.5)


side_b = turtle.Turtle()
side_b.speed(0) #speed Animation
side_b.shape("square")
side_b.color("white")
side_b.penup()
side_b.goto(340, 0)
side_b.shapesize(stretch_wid=5, stretch_len=0.5)




ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1


score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("0   :   0", align="center", font=("comicsans", 30))


def a_up():
    y = side_a.ycor()
    y += 20
    side_a.sety(y)

def a_down():
    y = side_a.ycor()
    y -= 20
    side_a.sety(y)



def b_up():
    y = side_b.ycor()
    y += 20
    side_b.sety(y)

def b_down():
    y = side_b.ycor()
    y -= 20
    side_b.sety(y)



wn.listen()
wn.onkeypress(a_up, "w")
wn.onkeypress(a_down, "s")
wn.onkeypress(b_up, "Up")
wn.onkeypress(b_down, "Down")



score_a = 0
score_b = 0


while True:
    wn.update()
    
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border
    if ball.ycor() > 300:
        ball.sety(300)
        ball.dy *= -1     

    if ball.ycor() < -300:
        ball.sety(-300)
        ball.dy *= -1    

    if ball.xcor() > 400:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.write("{}   :   {}".format(score_a, score_b), align="center", font=("comicsans", 30))


    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write("{}   :   {}".format(score_a, score_b), align="center", font=("comicsans", 30))


    # Reflect ball

    if ball.xcor() < -330 and ball.ycor() < side_a.ycor() + 50 and ball.ycor() > side_a.ycor() - 50:
        ball.dx *= -1 
        
        

    if ball.xcor() > 330 and ball.ycor() < side_b.ycor() + 50 and ball.ycor() > side_b.ycor() - 50:
        ball.dx *= -1
        
        
