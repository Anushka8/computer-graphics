from rit_window import *
from cgI_engine import *
from vertex import *
from shapes import *
import numpy as np

def drawPedistal():

    # draw a single pedestal with the cube on top...
    # you can replace with your own if you like.

    # pole
    myEngine.pushTransform()
    myEngine.scale (0.6, 2.0, 0.6)
    myEngine.drawTrianglesC (cylinder, cylinder_idx, 255, 255, 0, 255, 0, 0)
    myEngine.popTransform()
    
    #top
    myEngine.pushTransform()
    myEngine.translate (0.0, 1.0, 0.0)
    myEngine.pushTransform()
    myEngine.scale (0.9, 0.1, 0.9)
    myEngine.drawTrianglesC (cube, cube_idx, 255, 255, 0, 255, 0, 0)
    myEngine.popTransform()

    # showcaae cube
    myEngine.pushTransform()
    myEngine.translate (0.0, 0.45, 0.0)
    myEngine.pushTransform()
    myEngine.scale (0.4, 0.4, 0.4)
    myEngine.rotatex (45.0)
    myEngine.rotatey (45.0)
    myEngine.drawTrianglesC (cube, cube_idx, 0, 255, 0, 0, 0, 0)
    myEngine.popTransform()
    myEngine.popTransform()
    myEngine.popTransform()

    #bottom
    myEngine.pushTransform()
    myEngine.translate (0.0, -1.0, 0.0)
    myEngine.pushTransform()
    myEngine.scale (0.9, 0.1, 0.9)
    myEngine.drawTrianglesC (cube, cube_idx, 255, 255, 0, 255, 0, 0)
    myEngine.popTransform()
    myEngine.popTransform()

def default_action ():
    # clear the FB
    myEngine.win.clearFB (0, 0, 0)
    
    # set up your camera to use orthographic projection here.
    
    # position
    myEngine.pushTransform()
    myEngine.translate (-1, 0, -3.0)
    drawPedistal()
    
    myEngine.pushTransform()
    myEngine.translate (1, 0, -5.0)
    drawPedistal()
    
    
    
 
    
 
    
window = RitWindow(800, 800)
myEngine = CGIengine (window, default_action)

def main():
    window.run (myEngine)
    



if __name__ == "__main__":
    main()
