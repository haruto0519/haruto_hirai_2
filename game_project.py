
#-----import statements-----
import random as rand
import turtle as trtl
spot = trtl.Turtle()
score_writer = trtl.Turtle()
font_setup = ("Helvetica", 20, "normal")
font_setup2 = ("Helvetica", 30, "normal")
score_writer.speed(0)
score_writer.hideturtle()
counter = trtl.Turtle()
counter.speed(0)
counter.hideturtle()
counter.pencolor("white")
score_writer.pencolor("white")
wn = trtl.Screen()
wn.bgcolor("black")

spot.showturtle()
spot.shape("circle")
spot.shapesize(2)
spot.color("red")
spot.speed(0)
score = 0


def clicked(x, y):
    global score
    score += 1
    new_xpo = rand.randint(-380,380)
    new_ypo = rand.randint(-280,280)
    spot.penup()
    spot.goto(new_xpo, new_ypo) 
    #update_score
    score_writer.clear()
    score_writer.penup()
    score_writer.goto(-300,200)
    score_writer.write("Score: ", font=font_setup)
    score_writer.goto(-200, 200)
    score_writer.write(score, font = font_setup)
    
spot.onclick(clicked)


timer = 5
counter_interval = 1000   
timer_up = False
counter.penup()
counter.goto(250,200)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    spot.clear()
    timer_up = True
    wn.clear()
    wn.bgcolor("black")
    score_writer.goto(-210,-50)
    counter.goto(-120, 0)
    score_writer.write("Your score is ...", font = font_setup2)
    score_writer.goto(100,-50)
    score_writer.write(score, font = font_setup2)
    counter.write("Times' Up!!!", font = font_setup2)
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)


counter.getscreen().ontimer(countdown, counter_interval)
wn.mainloop()