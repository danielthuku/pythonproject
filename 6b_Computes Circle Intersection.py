#handle the case when the line does not intersect the circle. 
#You should use Python’s exception handling using try/except to catch the error and print out a customized error message.

# from graphics import *
# GraphWin Worked instead of graph
#Write a program that computes the intersection of a circle with a horizontal line and displays the information textually and graphically.
#Input: Radius of the circle and the y-intercept of the line. Prompt the user for these values.
#Output: Draw a circle centered at 0,0 with the given radius in a window with coordinates running from 10,10 to 10,10.
#Draw a horizontal line across the window with the given y-intercept.
#Draw the two points of intersection in red.
#Print out the x values of the points of intersection in the upper left-hand corner of the window.
#Formula for the intersection values of x:

from graphics import *
import math

def main():
   
      
    h = GraphWin('Computes Circle Intersection',600,300)
    h.setCoords(0,0,24,12)
    h.setBackground('White')
   
   
    # Draw a Rectangle
    chart = Rectangle(Point(0.8,11.2),Point(11.2,0.8))
    chart.setFill('grey85')
    chart.draw(h)
   
   #Y axis
    Line(Point(6,0.8),Point(6,11.2)).draw(h)
   #x axis 
    Line(Point(0.8,6),Point(11.2,6)).draw(h)
       
    # Y and X small lines 
    for i in range(2,23):
        i = i/2
        Line(Point(5.93,i),Point(6.15,i)).draw(h)
        Line(Point(i,5.93),Point(i,6.15)).draw(h)
        
        z = q = 6

    
    # Numbering y and X axis
    for i in range(0,11):
        # Positive y axis numbering
        num = Text(Point(5.65,z),i)
        num.setSize(6)
        if i != 0 :
            num.draw(h)
        
        # Negative y axis  Numbering
        num3 = Text(Point(5.65,q),i*-1)
        num3.setSize(6)
        if i != 0 :
            num3.draw(h)
          
        # Positive x axis Numbering       
        num2 = Text(Point(z,5.75),i)
        num2.setSize(6)
        if i != 0 :
            num2.draw(h)
        
        # Negative x axis Numbering
        num3 = Text(Point(q,5.75),i*-1)
        num3.setSize(6)
        if i != 0 :
            num3.draw(h)
        

        
        z = z+0.5
        q = q-0.5
        
        
        
    intro1 = Text(Point(17.40,10.75),'Program to calculate X intercept')
    intro1.setStyle('bold')
    intro1.draw(h)
    
    intro2 = Text(Point(17.40,10),'_______________________________')
    intro2.setStyle('bold')
    intro2.draw(h)
    
    
    Text(Point(14.75,8.5),'Circle radius  :').draw(h)
    Text(Point(14.75,7.8),'(value 10 to -10): ').draw(h)
    inputR = Entry(Point(20.5,8.5),10)
    inputR.setFill('grey85')
    inputR.setText('0')
    inputR.draw(h)
    
    
    Text(Point(14.3,6),' x-intercept : ').draw(h)
    Text(Point(15,5.2),'(value 10 to -10): ').draw(h)
    inputY = Entry(Point(20.5,6),10)
    inputY.setFill('grey85')
    inputY.setText('0')
    inputY.draw(h)
    
    
    
    #button Claculate   
    Fbutton = Rectangle(Point(18.5,2),Point(22.3,0.5))
    Fbutton.setFill('grey85')
    Fbutton.draw(h)
    
    FbuttonT = Text(Point(20.35,1.25),'Calculate')
    FbuttonT.draw(h)
    
    h.getMouse()
    
    # get variable
    R = eval(inputR.getText())
    Y = eval(inputY.getText())
    
    
    X = math.sqrt(R**2-Y**2)
    
    
    X = round(X,2)
    
    
    #answerX
    Text(Point(14.5,3.5),' y-intercept = : ').draw(h)
    Text(Point(18.2,3.7),'+').draw(h)
    Text(Point(18.2,3.3),'-').draw(h)
    
    answerX = Entry(Point(20.5,3.5),10)
    answerX.setFill('grey85')
    answerX.setText('?')
    answerX.draw(h)
    
    
        
    
    answerX.setText(X)
    
    
    R = R/2  
    resultC = Circle(Point(6,6),R)
    resultC.setFill("yellow")
    resultC.draw(h)
    
    
    Line(Point(6,1),Point(6,11)).draw(h)
    Line(Point(1,6),Point(11,6)).draw(h)
    
    
    Y = Y/2+6     
    lineY = Line(Point(1,Y),Point(11,Y))
    lineY.setFill('green')
    lineY.draw(h)
    
    
    X = X/2       
    Xa = X+6      
    Xb = 6-X
    
    resultPa = Circle(Point(Xa,Y),0.1)
    resultPa.setFill('red')
    resultPa.draw(h)
    
    resultPb = Circle(Point(Xb,Y),0.1)
    resultPb.setFill('red')
    resultPb.draw(h)
    
    FbuttonT.setText('Quit')
       
    #pause for exit
    h.getMouse()
    h.close()
   
main()