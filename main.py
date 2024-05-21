from rit_window import *
from cgI_engine import *
from vertex import *
from clipper import *
from shapes_new import *
import numpy as np
from PIL import Image


def default_action():
    # create your scene here
    # clear the FB
    myEngine.win.clearFB(.15, .15, .45)

    # set up your camera
    myEngine.setCamera(glm.vec3([0.0,0.0,2.0]), glm.vec3([0,0,20]), glm.vec3([0,1,0]))
    myEngine.setOrtho(-3.0, 3.0, -3.0, 3.0, -3.0, 3.0)

    # wooden cone
    myEngine.clearModelTransform()
    im = Image.open("wood.jpg")
    myEngine.translate(0.46, 1.55, 1.5)
    myEngine.rotatey(30)
    myEngine.rotatex(30)
    myEngine.scale(0.5, 0.68, 0.5)
    myEngine.drawTrianglesTextures(cone_new, cone_new_idx, cone_new_uv, im)

    # main pencil body
    myEngine.clearModelTransform()
    im = Image.open("pencil.jpg")
    myEngine.translate(0.0, 0.0, 0.0)
    myEngine.rotatey(30)
    myEngine.rotatex(30)
    myEngine.scale(0.5, 2.8, 0.5)
    myEngine.drawTrianglesTextures(cylinder_new, cylinder_new_idx, cylinder_new_uv, im)

    # metal part
    myEngine.clearModelTransform()
    im = Image.open("metal.jpg")
    myEngine.translate(-0.36, -1.27, -0.62)
    myEngine.rotatey(30)
    myEngine.rotatex(30)
    myEngine.scale(0.5, 0.1, 0.5)
    myEngine.drawTrianglesTextures(cylinder_new, cylinder_new_idx, cylinder_new_uv, im)

    # eraser
    myEngine.clearModelTransform()
    im = Image.open("eraser.jpg")
    myEngine.translate(-0.4, -1.35, -0.62)
    myEngine.rotatey(30)
    myEngine.rotatex(30)
    myEngine.scale(0.5, 0.3, 0.5)
    myEngine.drawTrianglesTextures(cylinder_new, cylinder_new_idx, cylinder_new_uv, im)


window = RitWindow(800, 800)
myEngine = CGIengine(window, default_action)


def main():
    window.run(myEngine)


if __name__ == "__main__":
    main()
