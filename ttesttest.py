from graphics import *



win =  GraphWin('Computes Circle Intersection',600,300)
win.setCoords(0,0,24,12)
win.setBackground('White')

    
def buttons():
    left = Rectangle(Point(12.5,2),Point(16.3,0.5)) # points are ordered ll, ur
    quit = Rectangle(Point(18.5,2),Point(22.3,0.5))

    left.setFill("red")
    quit.setFill("green")
    text = Text(Point(20.35,1.25),'Calculate')
    text.draw(win)

    left.draw(win)
    quit.draw(win)

    return left,  quit

left, quit = buttons()



  
def inside(point, rectangle):
    """ Is point inside rectangle? """
 
    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)
 
    return ll.getX() < clickPoint.getX() < ur.getX() and ll.getY() > clickPoint.getY() > ur.getY()
 
 
centerPoint = Point(14.5,6)
text = Text(centerPoint, "dan")
text.draw(win)
 
while True:
    clickPoint = win.getMouse()
 
    if clickPoint is None:  # so we can substitute checkMouse() for getMouse()
        text.setText("none")
    elif inside(clickPoint, left):
        text.setText("Clicked" )       
    elif inside(clickPoint, quit):
        text.setText("quitleft")
        break
    else:
        text.setText("")
 
win.close()