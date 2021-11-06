import colorgram


# extract colors from image and return a list of rgb tuples
def get_colors():
    image = "image.jpg"
    colors = []
    for color in colorgram.extract(image, len(image)):
        colors.append((color.rgb.r, color.rgb.b, color.rgb.g))
    return colors


print(get_colors())
