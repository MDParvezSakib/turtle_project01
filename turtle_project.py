import turtle
import time

# Setup screen
screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.tracer(0)

# Draw background
def draw_field_and_sky(sky_color):
    turtle.clear()
    turtle.up()
    turtle.goto(-250, 0)
    turtle.down()
    turtle.color(sky_color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(500)
        turtle.left(90)
        turtle.forward(250)
        turtle.left(90)
    turtle.end_fill()

    turtle.up()
    turtle.goto(-250, -250)
    turtle.down()
    turtle.color("green")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(500)
        turtle.left(90)
        turtle.forward(250)
        turtle.left(90)
    turtle.end_fill()

# Draw house (moved up, colored properly, door added)
def draw_house():
    # House body
    turtle.up()
    turtle.goto(-150, -50)
    turtle.color("gray")  # ash
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

    # Roof
    turtle.goto(-150, 50)
    turtle.color("orange")
    turtle.begin_fill()
    turtle.goto(-100, 100)
    turtle.goto(-50, 50)
    turtle.goto(-150, 50)
    turtle.end_fill()

    # Door
    turtle.goto(-115, -50)
    turtle.color("brown")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()

# Draw improved tree at a given position
def draw_tree(x, y):
    # Trunk
    turtle.up()
    turtle.goto(x, y)
    turtle.color("saddlebrown")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
    turtle.end_fill()

    # Leaves (3 layered circles)
    turtle.goto(x - 0, y + 40)
    turtle.color("forestgreen")
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()

    turtle.goto(x - 15, y + 65)
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    turtle.goto(x - 5, y + 85)
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

# Draw sun or moon
def draw_circle(x, y, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

# Main loop
turtle.hideturtle()
sun_x = -250
moon_x = -250

while True:
    # Day
    for sun_x in range(-250, 251, 5):
        draw_field_and_sky("skyblue")
        draw_house()
        draw_tree(100, -100)
        draw_tree(150, -100)
        draw_circle(sun_x, 150, "yellow")  # Sun
        screen.update()
        time.sleep(0.05)

    # Night
    for moon_x in range(-250, 251, 5):
        draw_field_and_sky("black")
        draw_house()
        draw_tree(100, -100)
        draw_tree(150, -100)
        draw_circle(moon_x, 150, "white")  # Moon
        screen.update()
        time.sleep(0.05)
