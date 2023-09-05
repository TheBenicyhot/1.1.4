import turtle as trtl
painter = trtl.Turtle()
painter.speed(100)
painter.color("red")
#  loop with a zero-iteration condition

favorite_deasert = ("choclate")

while (favorite_deasert == 'icecream'):
  painter.right(36)
  painter.forward(30)
  painter.begin_fill()
  painter.circle(0)
  painter.end_fill()

#  infinite loop
painter.color("green")
favorite_color = 'green' 

while (favorite_color == 'green'):
  
  painter.left(250)
  painter.forward(100)
  painter.left(36)
  painter.begin_fill()
  painter.circle(3,10,10)
  painter.end_fill()

wn = trtl.Screen()
wn.mainloop()
