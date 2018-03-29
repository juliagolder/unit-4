#julia golder
#3/26/18
#colorChangeWindow.py


from ggame import *
from random import randint

green = Color(0x006600, 1)
lime = Color(0x00FF00, 1)

rectangle = RectangleAsset(400,400, LineStyle(1,lime),lime)

Sprite(rectangle)


App().run()
def mouseClick(event):
    lightBlue = Color(0x49fbff,1)
