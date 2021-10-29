#-----import statements-----
import random as rand
import turtle as trtl
spot = trtl.Turtle()


wn = trtl.Screen()
wn.addshape('halloween_picture.gif')
trtl.shape('halloween_picture.gif')



spot.speed(8)
score = 0


wn.addshape('bats.last.gif')
wn.addshape('ghost.gif')
spot.shape('bats.last.gif')

shape_list = ['ghost.gif','ghost.gif','ghost.gif','ghost.gif','ghost.gif','bats.last.gif']

def clicked(x, y):
    '''angles = rand.randint(0, 360)'''
    new_xpo = rand.randint(-250,250)
    new_ypo = rand.randint(-140,200)
    '''spot.left(angles)'''
    spot.penup()
    spot.goto(new_xpo, new_ypo) 
    spot.pendown()
    '''spot.shape('bats.last.gif')'''
    '''spot.shape('ghost.gif')'''
    random_shape = rand.randint(0, 5)
    
    spot.shape(shape_list[random_shape])
    


spot.onclick(clicked)


wn.mainloop()


