# stuff we're going to need from PIL
from PIL import Image, ImageDraw, ImageFont

# creating the image in specified color and shape
img = Image.new('RGB', (500, 300), color=(157, 25, 225))

# drawing a polygon and a circle
draw = ImageDraw.Draw(img)
draw.polygon(((131, 55), (444, 55), (300, 234)), fill=(255, 255, 255), outline=(255, 255, 255))
draw.ellipse(((247, 75, 333, 161)), fill=(0, 0, 255), outline=(0, 0, 255))

# adding Arial.Ttf and requesting user input
fnt = ImageFont.truetype('C:/Users/anton/PycharmProjects/P3kurssi/Arial.Ttf', 10)
d = ImageDraw.Draw(img)
query = input("Anna teksti:\n")
# adding the text
d.text((30, 250), query, font=fnt, fill=(251, 110, 0))

# saving the image
img.save('fancypic.png')
