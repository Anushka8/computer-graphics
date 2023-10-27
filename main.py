from rit_window import *
from cgI_engine import *
import numpy as np

# define co-ordinated for triangle for Batman
batman_left = np.array([0, 600, 300, 600, 175, 550, 0, 600, 175, 550, 140, 500, 140, 500, 350, 500, 140, 400,
                       140, 400, 350, 500, 330, 400, 330, 400, 375, 490, 360, 390, 360, 390, 375, 490, 400, 200,
                       375, 490, 400, 380, 400, 200, 375, 490, 400, 500, 400, 380, 380, 540, 400, 530, 400, 500,
                       380, 540, 380, 600, 400, 530, 390, 560, 400, 560, 400, 530, 175, 550, 300, 600, 320, 550,
                       320, 550, 380, 540, 375, 490, 140, 500, 175, 550, 320, 550, 375, 490, 380, 540, 400, 500,
                       140, 500, 320, 550, 375, 490, 330, 400, 350, 500, 375, 490])
idx_left = [i for i in range(51)]
batman_left_index = np.array(idx_left)
batman_left_color = np.array([0, 0, 0]*51)

batman_right = np.array([500, 600, 800, 600, 675, 550, 675, 550, 800, 600, 660, 500, 450, 500, 660, 500, 660, 400,
                         470, 400, 450, 500, 660, 400, 440, 390, 425, 490, 470, 400, 400, 200, 425, 490, 440, 390,
                         400, 380, 425, 490, 400, 200, 400, 500, 425, 490, 400, 380, 400, 530, 420, 540, 400, 500,
                         420, 600, 420, 540, 400, 530, 400, 560, 410, 560, 400, 530, 480, 550, 500, 600, 675, 550,
                         420, 540, 480, 550, 425, 490, 480, 550, 675, 550, 660, 500, 400, 500, 420, 540, 424, 490,
                         425, 490, 480, 550, 660, 500, 425, 490, 450, 500, 470, 400])
idx_right = [i for i in range(51)]
batman_right_index = np.array(idx_right)
batman_right_colour = np.array([0, 0, 0]*51)


def default_action():
    # clear the FB
    myEngine.win.clearFB(128, 128, 128)

    # draw the untransformed Batman Logo
    myEngine.drawTriangles(batman_left, batman_left_color, batman_left_index)
    myEngine.drawTriangles(batman_right, batman_right_colour, batman_right_index)


window = RitWindow(800, 800)
myEngine = CGIengine(window, default_action)


def main():
    window.run(myEngine)


if __name__ == "__main__":
    main()
