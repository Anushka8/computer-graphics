from rit_window import *
from cgI_engine import *
from vertex import *
from shapes import *
import numpy as np


def default_action():
    # # place your code here
    myEngine.win.clearFB(0, 0, 0)
    myEngine.clearModelTransform()
    myEngine.translate(400, 190, 0)
    myEngine.pushTransform()
    myEngine.translate(0, 0.5, 0)
    myEngine.scale(120, 30, 1)
    myEngine.pushTransform()
    myEngine.drawTriangleC(cube, cube_idx, 255, 90, 0)
    myEngine.popTransform()

    # myEngine.translate(100,0, 0)
    myEngine.clearModelTransform()
    myEngine.translate(0, 130, 0)
    myEngine.pushTransform()
    # myEngine.translate(50, 50, 0)
    myEngine.scale(80, 200, 1)
    myEngine.pushTransform()
    myEngine.drawTriangleC(cylinder, cylinder_idx, 255, 30, 0)
    myEngine.popTransform()

    myEngine.clearModelTransform()
    myEngine.translate(0, 100, 0)
    myEngine.pushTransform()
    myEngine.translate(0, 0.5, 0)
    myEngine.scale(120, 30, 1)
    myEngine.pushTransform()
    myEngine.drawTriangleC(cube, cube_idx, 255, 20, 0)
    myEngine.popTransform()

    myEngine.clearModelTransform()
    myEngine.translate(0, 80, 0)
    myEngine.pushTransform()
    myEngine.rotate_x(20)
    myEngine.rotate_y(85)
    myEngine.rotate_z(75)
    myEngine.translate(0, 0.5, 0)
    myEngine.scale(80, 60, 1)
    # myEngine.rotate_y(80)
    # myEngine.rotate_x(120)
    myEngine.pushTransform()
    myEngine.drawTriangleC(cube, cube_idx, 255, 20, 0)
    myEngine.popTransform()


window = RitWindow(800, 800)
myEngine = CGIengine(window, default_action)


def main():
    window.run(myEngine)


if __name__ == "__main__":
    main()
