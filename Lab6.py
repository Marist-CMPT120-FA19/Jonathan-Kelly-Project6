#jonathan Kelly, 10/14/19,Jonathan.kelly2@marist.edu,  create stop light using functions

from graphics import *

win = GraphWin('traffic_light',200,200)


def draw_lamp(x,y,radius,color):
    light=Circle (Point (x,y), radius)
    light.setFill(color)
    light.setOutline ("black")
    
    light.draw(win)
    
def draw_light_body(x, y, length, width):
    rect= Rectangle (Point(x,y), Point(length,width))
    rect.setOutline("black")
    rect.setFill("white")
    
    rect.draw(win)
    

def draw_traffic_light(x,y):
    draw_light_body(x, y, 100, 160)
    draw_lamp(65, 40, 20, "red")
    draw_lamp(65, 85, 20, "yellow")
    draw_lamp(65, 130, 20, "green")
    
    win.getMouse()
    
def main():
    
    draw_traffic_light(30, 10)

main()