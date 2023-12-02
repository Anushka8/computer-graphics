from rit_window import *
from cgI_engine import *
from vertex import *
from clipper import *
from shapes import *
import numpy as np

tri1 = [5.0, -2.0, 1.0, -1.0, 4.0, 1.0, -1.5, 3.0, 1.0]
tri2 = [5.0, 2.0, 0.0, -1.0, -3.0, 0.0, -1.5, -5.0, 0.0]
tri3 = [0.0, 5.0, 3.0, -1.0, 3.0, 3.0, 0.0, -5.0, -1.0]
tris_idx = [0, 2, 1]


def default_action():
    # clear the FB
    myEngine.win.clearFB(0, 0, 0)
    myEngine.defineClipWindow(3.0, -3.0, 3.0, -3.0)

    # set up your camera
    myEngine.setCamera([0.0, 0.0, 5.0], [0, 0, 0], [0, 1, 0])
    myEngine.setOrtho(-6.0, 6.0, -6.0, 6.0, 2.0, 10.0)

    # position
    myEngine.drawTrianglesC(tri1, tris_idx, 255, 0, 0)
    myEngine.drawTrianglesC(tri2, tris_idx, 0, 255, 0)
    myEngine.drawTrianglesC(tri3, tris_idx, 0, 0, 255)


window = RitWindow(800, 800)
myEngine = CGIengine(window, default_action)


def main():
    window.run(myEngine)


if __name__ == "__main__":
    main()
