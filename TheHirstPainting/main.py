import colorgram
import turtle as turtle_module
import random


# extract colors from image and return a list of rgb tuples
# def get_colors():
#     image = "image.jpg"
#     colors = []
#     for color in colorgram.extract(image, len(image)):
#         colors.append((color.rgb.r, color.rgb.b, color.rgb.g))
#     return colors


# print(get_colors())

color_list = [(235, 231, 234), (234, 231, 229), (236, 108, 35), (222, 237, 231),
              (145, 65, 28), (239, 34, 74), (6, 93, 148), (231, 234, 238), (232, 40, 168)]

turtle_module.colormode(255)
hirst = turtle_module.Turtle()


def draw(space, x):
    for _ in range(x):
        for _ in range(x):
            # random.choice(color_list)
            hirst.dot(5, random.choice(color_list))
            hirst.forward(space)  # distance for another dot
        hirst.backward(space*x)  # go back to the start of the row

        # direction
        hirst.right(90)
        hirst.forward(space)
        hirst.left(90)


# Main Section
hirst.penup()
draw(50, 10)

# hide the turtle
hirst.hideturtle()


screen = turtle_module.Screen()
# close the turtle window on click  #
screen.exitonclick()
