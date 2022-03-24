from tkinter import * # Import tkinter
import math
#import gift_wrapping

def add(event):
    points.append([event.x, event.y])
    repaint()

def remove(event):
    for [x, y] in points:
        if distance(x, y, event.x, event.y) <= 10:
            points.remove([x, y])
    repaint()

def distance(x, y, x1, y1):
    return ((x - x1) * (x - x1) + (y - y1) * (y - y1)) ** 0.5

def repaint():
    canvas.delete("point")
    if len(points) > 2:
        
        
        
        H = getConvexHull(points) # call GiftWrapping getConvexHull
        
        
        
        canvas.create_polygon(H, fill = "gray", tags = "point")

    for [x, y] in points:
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, tags = "point")
    
def displayInstructions():
    instructions = ["INSTRUCTIONS", "Add:", "Left Click", "Remove:", "Right Click"]
    x = 20
    y = 20
    canvas.create_rectangle(x, y, x + 160, y + 80)
    canvas.create_text(x + 10 + 40, y + 20, text = instructions[0], justify = CENTER)
    for i in range(1, len(instructions), 2):
        canvas.create_text(x + 10 + 40, y + 20 + (i + 1) * 10, text = instructions[i], justify = RIGHT)
        canvas.create_text(x + 80 + 40, y + 20 + (i + 1) * 10, text = instructions[i + 1], justify = RIGHT)

def getConvexHull(points):
    # create a list for storing the final result, currently at max height and width of field.
    convexHull = [[width, height]]
    
    # copies over the points into a new array to manipulate
    working_points = points.copy()
    #runs a for loop to decide which of the points has the lowest y value or if same then highest x value (right most)
    for i in points:
        if i[1] < convexHull[0][1]:
            convexHull[0] = i.copy()
            
        elif i[1] == convexHull[0][1] and i[0] > convexHull[0][0] :
            convexHull[0] = i.copy()
            
    #variables for temporary storing of points, currently program is set to run when minimum of 3 values are in.
    p0 = convexHull[0]
    p1 = working_points[0]
    p2 = working_points[1]
    
    #The first while loop keeps running until p1 becomes the convexHull, p2 is used as a "testing" point.
    while True:
        # for loop runs through all the points.
        for i in working_points:
            p2 = i
            
            if point_position(p0, p1, p2) < 0:
                p1 = p2

            elif point_position(p0, p1, p2) == 0:
                #in case 2 positions are on a line, the distance of both points from p0 is calculated and the closes point is discarded.
                if distance(p0[0], p0[1], p2[0], p2[1]) > distance(p0[0], p0[1], p1[0], p1[1]):
                    p1 = p2
        
        if p1 == convexHull[0]:
            break
        #following the for loop p1 should be the next point in the convexhull and is therefore added to the list and becomes the next p0
        convexHull.append(p1)
        p0 = p1

    return convexHull


def point_position(p0, p1, p2):
    #standard formula for finding out whether a point is to the left right or on line with 2 other points.
    return (p1[0]- p0[0])*(p2[1]-p0[1])-(p2[0]-p0[0])*(p1[1]-p0[1])
        
window = Tk() # Create a window
window.title("Convex Hull") # Set title

width = 500
height = 150
radius = 2
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

# Create a 2-D list for storing points
points = []

displayInstructions()

canvas.bind("<Button-1>", add)
canvas.bind("<Button-3>", remove)


window.mainloop() # Create an event loop
