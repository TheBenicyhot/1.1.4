import turtle as trtl

painter = trtl.Turtle()

# Add a loop with a zero-iteration condition
Favorite_Icecream_Flavor = "Vanila" 

while (Favorite_Icecream_Flavor == "Choclate"):
  painter.right(200)
  painter.forward(300)
  print(",Favorite_Icecream_Flavor," "that sucks ")

# Add an infinite loop
Favorite_Color = "blue"
painter.color("blue")
while( Favorite_Color == "blue" ):
 painter.right(20)
 painter.forward(50)
 painter.begin_fill()
 painter.left(70)
 painter.end_fill()
 print(" Unless your favorite color is blue then it sucks ")


wn = trtl.Screen()
wn.mainloop()