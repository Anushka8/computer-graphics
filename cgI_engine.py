import math

from rit_window import *


class CGIengine:
    def __init__(self, myWindow):
        self.w_width = myWindow.width
        self.w_height = myWindow.height;
        self.win = myWindow
        self.keypressed = 1

    def set_dot(self, x_co, y_co, R, G, B):
        for x in range(5):
            for y in range(5):
                self.win.set_pixel(x + x_co, y + y_co, R, G, B)

    def draw_line(self, x0, x1, y0, y1, R, G, B):
        dx = x1 - x0
        dy = y1 - y0
        self.set_dot(x0, y0, R, G, B)
        if dx != 0:
            m = dy / dx
            b = y0 - m * x0
            if x1 >= x0:
                dx = 1
            else:
                dx = -1
            while x0 != x1:
                x0 += dx
                y0 = math.ceil(m * x0 + b)
                self.set_dot(x0, y0, R, G, B)

    # go is called on every update of the window display loop
    # have your engine draw stuff in the window.
    def go(self):
        if (self.keypressed == 1):
            # default scene
            self.win.clearFB(0, 0, 0)
            self.rasterizeLine(100, 100, 500, 500, 255, 0, 0)   #red  +
            self.rasterizeLine(100, 200, 500, 400, 0, 255, 0)   #green +
            self.rasterizeLine(100, 300, 500, 300, 0, 0, 255)   #blue horizontal
            self.rasterizeLine(100, 400, 500, 200, 255, 255, 0) #yellow -
            self.rasterizeLine(100, 500, 500, 100, 0, 255, 255) #teal -
            self.rasterizeLine(200, 500, 400, 100, 255, 0, 255) #pink - WRONG
            self.rasterizeLine(300, 500, 300, 100, 255, 255, 255) #not working  white horizontal
            self.rasterizeLine(400, 500, 200, 100, 128, 255, 255) #not working teal +
            self.rasterizeLine(500, 450, 100, 150, 34, 200, 10) #not working
            self.rasterizeLine(450, 100, 150, 500, 34, 200, 140)    #olive --

        if (self.keypressed == 2):
            # add you own unique scene here
            self.win.clearFB(0, 0, 0)
            self.draw_line(60, 100, 60, 150, 255, 0, 0)
            self.draw_line(60, 100, 100, 190, 0, 255, 0)
            self.draw_line(60, 100, 140, 230, 0, 0, 255)
            self.draw_line(140, 100, 60, 150, 255, 0, 0)
            self.draw_line(140, 100, 100, 190, 0, 255, 0)
            self.draw_line(140, 100, 140, 230, 0, 0, 255)
            for x in range(5):
                for y in range(230, 530):
                    self.win.set_pixel(100 + x, y, 192, 192, 192)
            self.draw_line(60, 100, 440, 530, 192, 192, 192)
            self.draw_line(140, 100, 440, 530, 192, 192, 192)

        # push the window's framebuffer to the window
        self.win.applyFB()

    def rasterizeLine(self, x0, y0, x1, y1, r, g, b):
        dy = y1 - y0
        dx = x1 - x0
        # when slope is 0
        if dy == 0:
            x, y = x0, y0
            for x_cod in range(x0, x1):
                self.win.set_pixel(x_cod, y, r, g, b)
        # when slope is infinite
        elif dx == 0:
            x, y = x0, y0
            for y_cod in range(y1, y0):
                self.win.set_pixel(x, y_cod, r, g, b)
        # when slope is positive
        elif dy > 0 and dx > 0 or dy < 0 and dx < 0:
            # change start and end points for x and y-axis
            if y0 > y1:
                ystart, yend = y1, y0
            else:
                ystart, yend = y0, y1

            if x0 > x1:
                xstart, xend = x1, x0
            else:
                xstart, xend = x0, x1
            # initiliaze x and y for plotting
            x, y = xstart, ystart
            if 0 < dy / dx <= 1:
                d = (2 * dy) - dx
                for x_cod in range(xstart, xend):
                    self.win.set_pixel(x_cod, y, r, g, b)
                    if d <= 0:
                        if y0 < y1 and x0 < x1:
                            d += (2 * dy)
                        else:
                            d -= (2 * dy)
                    else:
                        y += 1
                        if y0 < y1 and x0 < x1:
                            d += (2 * (dy - dx))
                        else:
                            d -= (2 * (dy - dx))
            elif dy / dx > 1:
                d = (2 * dx) - dy
                for y_cod in range(ystart, yend):
                    self.win.set_pixel(x, y_cod, r, g, b)
                    if d <= 0:
                        d -= (2 * dx)
                    else:
                        x += 1
                        d -= (2 * (dx - dy))
        else:
            x, y = x0, y0
            if 0 > dy/dx >= -1:
                d = (2 * dy) + dx
                for x_cod in range(x0, x1):
                    self.win.set_pixel(x_cod, y, r, g, b)
                    if d <= 0:
                        y -= 1
                        d += (2 * (dy + dx))
                    else:
                        d += (2 * dy)
            else:
                d = (2 * dx) + dy
                if y1 > y0:
                    ystart, yend = y0, y1
                else:
                    ystart, yend = y1, y0
                if x1 > x0:
                    x = x1
                else:
                    x = x0
                for y_cod in range(ystart, yend):
                    self.win.set_pixel(x, y_cod, r, g, b)
                    if d <= 0:
                        x -= 1
                        if y0 < y1:
                            d += (2 * (dy + dx))
                        else:
                            d -= (2 * (dy + dx))
                    else:
                        if y0 < y1:
                            d += (2 * dx)
                        else:
                            d -= (2 * dx)

    def keyboard(self, key):
        if (key == '1'):
            self.keypressed = 1
            self.go()
        if (key == '2'):
            self.keypressed = 2
            self.go()
