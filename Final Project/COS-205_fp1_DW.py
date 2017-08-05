from graphics import *
from collections import Counter
import os.path
 
# This function will  request filename input from the user e.g file.txt
def getFileName():
    goodinput = False
    while not goodinput:
        
        try:

            fname = input("Enter filename: ")
            fileDir = os.path.dirname(os.path.realpath('__file__'))
            fname = os.path.abspath(fname) 
            if os.path.exists(fname):
                goodinput = True
                return fname
            else:
                print("Error: file not found Please Enter correct file name:!")
                print ("")
        except FileNotFoundError:
             print("Error: file not found Please Enter correct file name:!")
             print ("")
           

# This function will get the  Count highest integer in List 
def getMaxScoreCount(scores):
     
    maxC = max(scores)

    return maxC


# Main Function 
def main():
    print("This Program will draw a quiz score histogram")
    print("") 
    #read file from disk
    infile = open(getFileName(),'r') #open('file passed from function','r')
     
    #create 11 items in List for scores 0-10
    scores = [0,0,0,0,0,0,0,0,0,0,0]
     
         
    # Variable for counting total students
    students = 0
    notCounted = 0 
    #loop through each line and use list index as counter for
    #each scores number
    
    for i in infile:
        try: 
            if (int(i) >= 0 and (int(i) < 11)):
                scores[int(i)] = scores[int(i)]+1
                students = students+1
            else:
                notCounted = notCounted + 1   
        except ValueError:
            notCounted = notCounted + 1
    print("")
    print("%s grade not were not counted Because; \nEither Empty or Wrong type or Grater than 10 or Less than 0. Please check your input file!" % str(notCounted))
    

     
         
    # Window Co-ordinates height and width of GUI
    win = GraphWin('Program to Draw a Quiz Score Histogram',600,310)
    win.setCoords(0,0,35,27)       
    win.setBackground('White')
         
         
    #draw black bottom background part
    bottomBG = Rectangle(Point(0,0),Point(36,2.5))
    bottomBG.setFill('dimgray')
    bottomBG.draw(win)
         
     
    #Draw QUIT button (fake button)
    buttonShadow = Rectangle(Point(27,0.2),Point(34.6,2.4))
    buttonShadow.setFill(color_rgb(64,63,63))
    buttonShadow.draw(win)
     
    buttonBox = Rectangle(Point(27.25,0.25),Point(34.25,2.25))
    buttonBox.setFill(color_rgb(155,155,155))
    buttonBox.draw(win) 
     
    buttonText = Text(Point(30.75,1.3),'Quit')
    buttonText.setFill('White')
    buttonText.draw(win)   
     
    #Display total students
    students = 'Total Number of Students:    '+str(students)
     

    totalStudent = Text(Point(9,1),students)
    totalStudent.setFill('white')
    totalStudent.draw(win)
     
    #x Axis Label
    xLabel = Text(Point(15.6,3.5), "score (0 to 10)")
    xLabel.setFill('Black')
    xLabel.setSize(6)
    xLabel.draw(win)
    
    #y Axis Label
    num = Text(Point(0.5,20),"C")
    num.setSize(6)
    num.draw(win) 
    num = Text(Point(0.5,19),"o")
    num.setSize(6)
    num.draw(win)
    num = Text(Point(0.5,18),"u")
    num.setSize(6)
    num.draw(win)
    num = Text(Point(0.5,17),"n")
    num.setSize(6)
    num.draw(win)
    num = Text(Point(0.5,16),"t")
    num.setSize(6)
    num.draw(win)    
      
    #y Axis Label y  
    num = Text(Point(2,26.5),"y")
    num.setSize(7)
    num.draw(win) 
    
    #x Axis Label x  
    num = Text(Point(34.7,5),"x")
    num.setSize(8)
    num.draw(win)                 
        
    # horizon Line
    Line(Point(2,5),Point(34.5,5)).draw(win)
     
    # vertical Line
    Line(Point(2,5),Point(2,26)).draw(win)
     
    #Y axis small indicator(1-20)
    for i in range(6,26):
        Line(Point(1.9,i),Point(2.3,i)).draw(win)
     
    #Y Axis longer indicator (5,10,15,20)
    for i in range(5,26,5):
        Line(Point(1.9,i),Point(2.6,i)).draw(win)
   
       
    # Setting yMax, My Ymax has a Max of 20 so all count has to change ratios to fit to fit 20; 
    maxRecCount = getMaxScoreCount(scores)
    if maxRecCount > 20:
        if maxRecCount % 20 == 0:
             yMax = ((maxRecCount // 20) * 20)  + 1
        elif maxRecCount % 20 != 0:
             yMax = ((maxRecCount // 20) * 20) + 20 + 1    
        skip = ((yMax-1)//20)
        notSkip = ((yMax-1)//20)
    elif ((maxRecCount > 10 ) and (maxRecCount < 21)):
        yMax = 20 + 1
        skip = 1
        notSkip = 1
    else:    
        yMax = 20 + 1
        skip = 2
        notSkip = 2

    #Auto Numbering y axis Depending on Input Data      
    for i in range(0,yMax):
        if notSkip == i:
            if maxRecCount > 20:
                notSkip = i + skip 
                num = Text(Point(1.5,i+5),i * skip)
                num.setSize(6)
                if i != 0 :
                    num.draw(win)  
            elif ((maxRecCount > 10 ) and (maxRecCount < 21)):
                notSkip = i + skip 
                num = Text(Point(1.5,i+5),i * skip)
                num.setSize(6)
                if i != 0 :
                    num.draw(win)                                       
            else:    
                notSkip = i + skip 
                num = Text(Point(1.5,i+5),i//skip)
                num.setSize(6)
                if i != 0 :
                    num.draw(win)

             
    #create bar chart using List index
    pos = 2
    for i in range(11):
        if ((type(i) == int) and (1 > -1 and i < 11 )):
            if maxRecCount > 20:
                bar = Rectangle(Point(pos,5),Point(pos+2,((scores[i] * 20/yMax) )+5))
                bar.setFill('green')
                bar.draw(win)
            else:
                bar = Rectangle(Point(pos,5),Point(pos+2,(scores[i] * skip)+5))
                bar.setFill('green')
                bar.draw(win)    
             
            pos = pos+3
         
    #Numbering X Axis 0-10
    position = 3
    for i in range(11):
        xNum = Text(Point(position,4.2),i)
        xNum.draw(win)
        xNum.setSize(8)
        position = position+3
     
    win.getMouse()
    win.close()
     
main()