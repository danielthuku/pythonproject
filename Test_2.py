''' pqt_drawtext_rotated.py
draw rotated text on the PyQt paint canvas via ...
paint.translate(dx, dy)
paint.rotate(degrees)
paint.drawText(x, y, QString text)

Pen and Brush set drawing and fill colors
a color can be selected via ...
red = Qt.red
or r,g,b values 0 - 255
red = QColor(255, 0, 0)
or some colors have names, try it
navy = (QColor("navy"))

used the Anaconda package (comes with PyQt4) on OS X
(dns)
'''

# simply use star import, since PyQt already uses a 'Q' prefix
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DrawText(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(70, 150, 350, 220)
        self.setWindowTitle('Draw Text on a canvas')

    def paintEvent(self, event):
        """
        paintEvent is a preset event method of self
        """
        # form the canvas to draw on
        paint = QPainter()
        # begin drawing
        paint.begin(self)

        # to set the canvas to a color use the Brush and
        # create a rectangle that fills the whole canvas
        paint.setBrush(QColor("navy"))
        paint.drawRect(event.rect())

        # this will be the text color (default is black)
        paint.setPen(QColor("orange"))
        # check the fonts available on your computer
        # for instance in C:\WINDOWS\Fonts
        paint.setFont(QFont('Comic Sans MS', 32))

        # dx, dy are offsets to drawText llc x, y coordinates
        # experiment with dx, dy values to get the hang of it
        dx = 90
        dy = 50
        # adjust to rotate
        paint.translate(dx, dy)
        # rotate degrees clockwise from horizontal
        degrees = 45
        paint.rotate(degrees)
        # drawText(x, y, text) lower left corner coordinates x, y
        paint.drawText(0, 0, "Hello World")

        # end drawing
        paint.end()


app = QApplication([])
dt = DrawText()
dt.show()
app.exec_()