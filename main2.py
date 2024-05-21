from rit_window import *
from cgI_engine import *
from vertex import *
from clipper import *
from shapes_new import *
import numpy as np
from PIL import Image


def default_action():
    # clear the FB
    myEngine.win.clearFB(.15, .15, .45)

    # set up your camera
    myEngine.setCamera(glm.vec3([0.0, 0.0, 2.0]), glm.vec3([0, 0, 20]), glm.vec3([0, 1, 0]))
    myEngine.setOrtho(-3.0, 3.0, -3.0, 3.0, -3.0, 3.0)

    # get your texture image
    im = Image.open("1_earth_16k.jpg")

    # draw a textured cube
    myEngine.translate(1.0, 1.0, 0.0)
    myEngine.rotatey(30)
    myEngine.rotatex(30)
    myEngine.scale(1.2, 1.2, 1.2)
    myEngine.drawTrianglesMyTextures(cube_new, cube_new_idx, cube_new_uv)

    # draw a textured sphere
    myEngine.clearModelTransform()
    myEngine.translate(-1.5, 1.0, 0.0)
    myEngine.scale(1.5, 1.5, 1.5)
    myEngine.drawTrianglesMyTextures(sphere_new, sphere_new_idx, sphere_new_uv)

    # draw a textured cylinder
    myEngine.clearModelTransform()
    myEngine.translate(0.0, -1.0, 0.0)
    myEngine.rotatey(30)
    myEngine.rotatex(-30)
    myEngine.scale(1.5, 1.5, 1.5)
    myEngine.drawTrianglesMyTextures(cylinder_new, cylinder_new_idx, cylinder_new_uv)


window = RitWindow(800, 800)
myEngine = CGIengine(window, default_action)


def main():
    window.run(myEngine)


if __name__ == "__main__":
    main()
