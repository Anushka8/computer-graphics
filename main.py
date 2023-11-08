from rit_window import *
from cgI_engine import *
from vertex import *
from shapes import *
import numpy as np


def default_action():

    # lower base
    myEngine.pushTransform()
    myEngine.translate(400.0, 100.0, 0.0)
    myEngine.scale(200.0, 50.0, 0.0)
    myEngine.drawTrianglesC(cube, cube_idx, 255, 255, 0)
    myEngine.drawTrianglesWireframe(cube, cube_idx, 165, 42, 42)
    myEngine.popTransform()

    # pole
    myEngine.pushTransform()
    myEngine.translate(0.0, 120.0, 0.0)
    myEngine.pushTransform()
    myEngine.scale(0.4, 4.0, 0.0)
    myEngine.drawTrianglesC(cylinder, cylinder_idx, 255, 255, 0)
    myEngine.drawTrianglesWireframe(cylinder, cylinder_idx, 165, 42, 42)
    myEngine.popTransform()
    myEngine.popTransform()

    # forming upper base
    myEngine.pushTransform()
    myEngine.translate(0.0, 115, 0.0)
    myEngine.pushTransform()
    myEngine.scale(2.5, 0.25, 0)
    myEngine.drawTrianglesC(cube, cube_idx, 255, 255, 0)
    myEngine.drawTrianglesWireframe(cube, cube_idx, 165, 42, 42)
    myEngine.popTransform()

    # cube at the top
    myEngine.pushTransform()
    myEngine.translate(0.0, 108.0, 0.0)
    myEngine.pushTransform()
    myEngine.scale(0.4, 1.9, 0.0)
    myEngine.rotate_x(45.0)
    myEngine.rotate_y(45.0)
    myEngine.drawTrianglesC(cube, cube_idx, 0, 255, 0)
    myEngine.drawTrianglesWireframe(cube, cube_idx, 0, 0, 0)
    myEngine.popTransform()
    myEngine.popTransform()
    myEngine.popTransform()
    myEngine.popTransform()


window = RitWindow(800, 800)
myEngine = CGIengine(window, default_action)


def main():
    window.run(myEngine)


if __name__ == "__main__":
    main()
