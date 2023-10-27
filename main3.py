from rit_window import *
from cgI_engine import *
from vertex import *
from clipper import *
import numpy as np

# co-ordinates for batman logo
batman_left = np.array([0, 600, 300, 600, 175, 550, 0, 600, 175, 550, 140, 500, 140, 500, 350, 500, 140, 400,
                        140, 400, 350, 500, 330, 400, 330, 400, 375, 490, 360, 390, 360, 390, 375, 490, 400, 200,
                        375, 490, 400, 380, 400, 200, 375, 490, 400, 500, 400, 380, 380, 540, 400, 530, 400, 500,
                        380, 540, 380, 600, 400, 530, 390, 560, 400, 560, 400, 530, 175, 550, 300, 600, 320, 550,
                        320, 550, 380, 540, 375, 490, 140, 500, 175, 550, 320, 550, 375, 490, 380, 540, 400, 500,
                        140, 500, 320, 550, 375, 490, 330, 400, 350, 500, 375, 490,
                        500, 600, 800, 600, 675, 550, 675, 550, 800, 600, 660, 500, 450, 500, 660, 500, 660, 400,
                        470, 400, 450, 500, 660, 400, 440, 390, 425, 490, 470, 400, 400, 200, 425, 490, 440, 390,
                        400, 380, 425, 490, 400, 200, 400, 500, 425, 490, 400, 380, 400, 530, 420, 540, 400, 500,
                        420, 600, 420, 540, 400, 530, 400, 560, 410, 560, 400, 530, 480, 550, 500, 600, 675, 550,
                        420, 540, 480, 550, 425, 490, 480, 550, 675, 550, 660, 500, 400, 500, 420, 540, 424, 490,
                        425, 490, 480, 550, 660, 500, 425, 490, 450, 500, 470, 400
                        ])
idx_left = [i for i in range(102)]
batman_left_index = np.array(idx_left)
batman_left_color = np.array([0, 0, 0] * 102)


def drawClippedPoly(vertices, translation):
    nverts = vertices.size
    if nverts < 3:
        return
    # chose your pivot vertex to be the first
    endV = 2
    while endV < nverts:
        P0 = Vertex(round(vertices[0].x + translation.x), round(vertices[0].y + translation.y),
                    vertices[0].r, vertices[0].g, vertices[0].b)
        P1 = Vertex(round(vertices[endV - 1].x + translation.x), round(vertices[endV - 1].y + translation.y),
                    vertices[endV - 1].r, vertices[endV - 1].g, vertices[endV - 1].b)
        P2 = Vertex(round(vertices[endV].x + translation.x), round(vertices[endV].y + translation.y),
                    vertices[endV].r, vertices[endV].g, vertices[endV].b)
        myEngine.rasterizeTriangle(P0, P1, P2)
        endV = endV + 1


def default_action():
    myEngine.win.clearFB(128, 128, 128)
    for ind in range(0, len(batman_left_index), 3):
        vertices = []
        for i in batman_left_index[ind: ind + 3]:
            x, y = batman_left[2 * i], batman_left[2 * i + 1]
            r, g, b = batman_left_color[3 * i], batman_left_color[3 * i + 1], batman_left_color[3 * i + 2]
            vertices.append(Vertex(x, y, r, g, b))
            cP = clipPoly(vertices, 700, 350, 400, 0)
            if cP.any():
                x = glm.vec3(400, -300, 0)
                drawClippedPoly(cP, x)


window = RitWindow(800, 800)
myEngine = CGIengine(window, default_action)


def main():
    window.run(myEngine)


if __name__ == "__main__":
    main()
