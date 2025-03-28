import turtle
def draw_petal(turtle, size):
    for _ in range(2):
        turtle.circle(size, 90)
        turtle.left(90)
def draw_flower(turtle, colors):
    for n in range(14):
        for _ in range(8):
            draw_petal(turtle, 80 + n * 10)
            turtle.left(45)
        turtle.pencolor(colors[n % len(colors)])

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('#000000')
t.speed(40)

colors = ('#00249f', '#13746b', '#40E0D0', '#00FFFF', '#39FF14', '#E1FF00',
          '#FFFF00', '#EE82EE', '#FF69B4', '#FF00FF', '#FFa500', '#FF0000', '#b30000', '#00FF00'
          )

draw_flower(t, colors)
s.exitonclick()