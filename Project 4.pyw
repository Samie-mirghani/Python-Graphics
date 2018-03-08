#Project 4.pyw
#Shamsadean Mirghani
#This program will ask the user two draw two triangles and colors the
#the larger one red and will display the area under the triangles
#Where ever they are plotted

from graphics import *
import math
# Function to find the distance between two points
def distance(p1,p2):
    x1= p1.getX()
    x2= p2.getX()
    y1= p1.getY()
    y2= p2.getY()
    x= x2-x1
    y= y2-y1
    d= math.sqrt(x**2 + y**2)
    return d
# Function to find the area of the triangle
def area(s1, s2, s3):
    s= (s1 + s2 + s3)/2
    a= math.sqrt((s)*(s-s1)*(s-s2)*(s-s3))
    return a
    
    

def main():
    # Creates Graphic window to house other objects
    win= GraphWin("Triangles", 600, 600)
    # Set color to black  
    win.setBackground("pink")
    # Sets coordinate system of window
    win.setCoords(0, 0, 6, 6)
    # Prompts the user to click three points 
    prompt= Text(Point(3, 0.5),
                 "Click the opposite edges to create a triangle")
    # Draws the prompt in the window
    prompt.draw(win)
    # Accepts and draws the different points and then draws triangle 1
    # in the window
    p1= win.getMouse()
    p1.draw(win)
    p2= win.getMouse()
    p2.draw(win)
    p3= win.getMouse()
    T1= Polygon(p1, p2, p3)
    T1.setFill("cornflower blue")
    T1.draw(win)
    # Reuses the prompt and asks the user to click three more places
    prompt.setText("Click the opposite"
                              " edges to create another triangle")
    # Accepts and draws the different prompts and then draws another
    # triangle in the window 
    p_1= win.getMouse()
    p_1.draw(win)
    p_2= win.getMouse()
    p_2.draw(win)
    p_3= win.getMouse()
    T2= Polygon(p_1, p_2, p_3)
    T2.setFill("cornflower blue")
    T2.draw(win)
    # Calling distance function for traingle 1 
    side_1= distance(p1,p2)
    side_2= distance(p2, p3)
    side_3= distance(p3, p1)
    # Calling distance function for triangle 2 
    side_4= distance(p_1, p_2)
    side_5= distance(p_2, p_3)
    side_6= distance(p_3, p_1)
    # Calls the area function twice for each area
    area_1= area(side_1, side_2, side_3)
    area_2= area(side_4, side_5, side_6)
    # Reuses the prompt to ask the user to click to color the larger
    # triangle red
    
    prompt.setText("Click to change the color of the larger"
                            " one to red")
    
    
    win.getMouse()
    # If statements to determine which one should be colored red
    if area_1 > area_2:
        T1.setFill("red")
    
    else:
        T2.setFill("red")
    # Saves the coordinates as variables
    x1= p1.getX()
    y1= p1.getY()
    x2= p2.getX()
    y2= p2.getY()
    x3= p3.getX()
    y3= p3.getY()
    
    # To find left-most point
    if x1<x2 and x1<x3:
        leftx = x1
    elif x2<x1 and x2<3:
        leftx = x2
    elif x3<x1 and x3<x2:
        leftx = x3
    # To find the right-most point
    if x1>x2 and x1>x3:
        rightx = x1
    elif x2>x1 and x2>x3:
        rightx = x2
    elif x3>x1 and x3>x2:
        rightx = x3
    # Find the center of the triangle
    X1 = (leftx + rightx)/2

    # To find the bottom of the triangle
    if y1<y2 and y1<y3:
        bottom = y1
    elif y2<y1 and y2<y3:
        bottom = y2
    elif y3<y1 and y3<y2:
        bottom = y3
    Y1 = bottom - 0.5
    # Saves all the coordinates as variables
    x4= p_1.getX()
    y4= p_1.getY()
    x5= p_2.getX()
    y5= p_2.getY()
    x6= p_3.getX()
    y6= p_3.getY()

     # To find left-most point
    if x4<x5 and x4<x6:
        leftx = x4
    elif x5<x4 and x5<6:
        leftx = x5
    elif x6<x4 and x6<x5:
        leftx = x6
    # To find the right-most point
    if x4>x5 and x4>x6:
        rightx = x4
    elif x5>x4 and x5>x6:
        rightx = x5
    elif x6>x4 and x6>x5:
        rightx = x6
    # Find the center of the triangle
    X2 = (leftx + rightx)/2

    # To find the bottom of the triangle
    if y4<y5 and y4<y6:
        bottom = y4
    elif y5<y4 and y5<y6:
        bottom = y5
    elif y6<y4 and y6<y5:
        bottom = y6
    Y2 = bottom - 0.5
    # Creates two new prompts and displays the area of both triangles
    prompt2= Text(Point(X1, Y1), 'The area of this triangle is: '
                  '{0:0.2f} units'.format(area_1))
    prompt2.draw(win)
    prompt3= Text(Point(X2, Y2), 'The area of this triangle is: '
                  '{0:0.2f} units'.format(area_2))
    prompt3.draw(win)
    # If statements used to color the text of the larger triangle
    if area_1 > area_2:
        prompt2.setTextColor("red")
    
    else:
        prompt3.setTextColor("red")
    

    
    # Undraws the previous prompt and reuses another prompt and changes
    # the color of the text 
    prompt.undraw()
    prompt.setText("Click in the window to exit program")
    prompt.setTextColor("red")
    prompt.setStyle("bold")
    prompt.draw(win)

    
    
    
    # Closes the window and exits the program
    win.getMouse()
    win.close()
    
main()
    


