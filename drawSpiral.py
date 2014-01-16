import turtle
def drawSpiral(myTurtle, len):
    if len < 100:
        myTurtle.forword(len)
        drawSpiral(myTurtle, len+10)
