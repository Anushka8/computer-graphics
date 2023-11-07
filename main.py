from rit_window import *
from cgI_engine import *
from vertex import *
from shapes import *
import numpy as np


def default_action():
    # place your code here
    myEngine.win.clearFB(0, 0, 0)
    myEngine.clearModelTransform()
    myEngine.translate(400, 190, 0)
    print(myEngine.model_matrix)
    myEngine.pushTransform()
    print(myEngine.transformation_stack[-1])
    myEngine.translate(0, 0.5, 0)
    myEngine.scale(120, 30, 1)
    myEngine.pushTransform()
    myEngine.drawTriangleC(cube, cube_idx, 255, 0, 0)
    myEngine.popTransform()


window = RitWindow(800, 800)
myEngine = CGIengine(window, default_action)


def main():
    window.run(myEngine)


if __name__ == "__main__":
    main()
