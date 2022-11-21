import image

img = image.Image("libro\luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
        newpixel = image.Pixel(0, p.getGreen(), p.getBlue())
        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()