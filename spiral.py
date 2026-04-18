import turtle 
t = turtle.Turtle()
screen = turtle.Screen()
color = ["rosybrown","pink","lavender","lightblue","lightsteelblue","paleturquoise","lightyellow",] 
screen.bgcolor("black") 
t.speed('fastest')
t.hideturtle()
while True:
  for x in range(250): 
    t.pencolor(color[x%len(color)])
    t.width(x/100 + 1)
    t.forward(x) 
    t.left(59)
  t.right(239)  
  for x in range(250, 0, -1): 
    t.pencolor('black') 
    t.width(x/100 + 7)
    t.forward(x) 
    t.right(59) 