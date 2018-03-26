#julia golder
#3/26/18
#colorChangeWindow.py


ROWS = 2
COLS = 2
CELL_SIZE = 20

rectangle = RectangleAsset(CELL_SIZE*COLS, CELL_SIZE*ROWS, LineStyle(1,green),green)

mouseClick(event)

App().listenMouseEvent(‘click’, mouseClick)
App().run()
