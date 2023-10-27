from rit_window import *
import numpy as np
import glm
import math
from vertex import *


class CGIengine:
    def __init__(self, myWindow, defaction):
        self.w_width = myWindow.width
        self.w_height = myWindow.height
        self.win = myWindow
        self.keypressed = 1
        self.default_action = defaction
        self.model_matrix = glm.mat3(1.0)
        self.normalization_matrix = glm.mat3(1.0)
        self.view_matrix = glm.mat3(1.0)

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
            self.default_action()

        if (self.keypressed == 2):
            # add you own unique scene here
            self.win.clearFB(0, 0, 0)

            # push the window's framebuffer to the window
        self.win.applyFB()

    # Assignment 2 - Rasterize Line
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
            # initialize x and y for plotting
            x, y = xstart, ystart
            # if slope is between 0 and 1
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
            # if slope is greater than 1
            elif dy / dx > 1:
                d = (2 * dx) - dy
                for y_cod in range(ystart, yend):
                    self.win.set_pixel(x, y_cod, r, g, b)
                    if d <= 0:
                        d -= (2 * dx)
                    else:
                        x += 1
                        d -= (2 * (dx - dy))
        # when slope is negative
        else:
            x, y = x0, y0
            # if slope is between -1 and 0
            if 0 > dy / dx >= -1:
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

    # Assignment 3 - Triangle
    def drawTriangles(self, vertex_data, color_data, index_data):
        for ind in range(0, len(index_data), 3):
            vertices = []
            for i in index_data[ind: ind + 3]:
                x, y = vertex_data[2 * i], vertex_data[2 * i + 1]
                r, g, b = color_data[3 * i], color_data[3 * i + 1], color_data[3 * i + 2]
                vertices.append(Vertex(x, y, r, g, b))

            for i in range(len(vertices)):
                original_vertex = glm.vec3(vertices[i].x, vertices[i].y, 1)
                transformed_vertex = self.view_matrix * self.normalization_matrix * \
                                     self.model_matrix * original_vertex
                vertices[i].x = int(transformed_vertex.x)
                vertices[i].y = int(transformed_vertex.y)

            self.rasterizeTriangle(vertices[0], vertices[1], vertices[2])

    def rasterizeTriangle(self, P0, P1, P2):
        # get minimum and max of x and y-axis
        x_min = min(P0.x, P1.x, P2.x)
        x_max = max(P0.x, P1.x, P2.x)
        y_min = min(P0.y, P1.y, P2.y)
        y_max = max(P0.y, P1.y, P2.y)

        for y in range(y_min, y_max + 1):
            for x in range(x_min, x_max + 1):
                # get edge functions for all edges
                E01 = self.edgeFunction(P0, P1, x, y)
                E12 = self.edgeFunction(P1, P2, x, y)
                E20 = self.edgeFunction(P2, P0, x, y)

                if (E01 >= 0 and E12 >= 0 and E20 >= 0) or (E01 < 0 and E12 < 0 and E20 < 0):
                    area = abs(0.5 * self.edgeFunction(P1, P2, P0.x, P0.y))
                    if area == 0.0:
                        area = 1
                    # get barycentric coordinates
                    lambda0 = E12 / (2 * area)
                    lambda1 = E20 / (2 * area)
                    lambda2 = E01 / (2 * area)

                    # perform interpolation
                    C0 = lambda0 * P0.r + lambda1 * P1.r + lambda2 * P2.r
                    C1 = lambda0 * P0.g + lambda1 * P1.g + lambda2 * P2.g
                    C2 = lambda0 * P0.b + lambda1 * P1.b + lambda2 * P2.b

                    self.win.set_pixel(x, y, C0, C1, C2)

    def edgeFunction(self, P0, P1, x, y):
        return (x - P0.x) * (P1.y - P0.y) - (y - P0.y) * (P1.x - P0.x)

    def keyboard(self, key):
        if (key == '1'):
            self.keypressed = 1
            self.go()
        if (key == '2'):
            self.keypressed = 2
            self.go()

    # Assignment 5 - The Transformer
    # set model transform matrix to identity
    def clearModelTransform(self):
        self.model_matrix = glm.mat3(1.0)

    # multiply translate matrix to current model transform
    def translate(self, x, y):
        self.model_matrix[2][0] += x
        self.model_matrix[2][1] += y

    # multiply scale matrix to current model transform
    def scale(self, x, y):
        self.model_matrix[0][0] *= x
        self.model_matrix[1][1] *= y

    # multiply rotate matrix to current model transform
    def rotate(self, angle):
        self.model_matrix[0][0] *= np.cos(np.deg2rad(angle))
        self.model_matrix[0][1] += np.sin(np.deg2rad(angle))
        self.model_matrix[1][0] += -np.sin(np.deg2rad(angle))
        self.model_matrix[1][1] *= np.cos(np.deg2rad(angle))

    def defineClipWindow(self, t, b, r, l):
        self.normalization_matrix[0][0] = (2 / (r - l))
        self.normalization_matrix[1][1] = (2 / (t - b))
        self.normalization_matrix[2][0] = ((-2 * l) / (r - l)) - 1
        self.normalization_matrix[2][1] = ((-2 * b) / (t - b)) - 1

    def defineViewWindow(self, t, b, r, l):
        self.view_matrix[0][0] = ((r - l) / 2)
        self.view_matrix[1][1] = ((t - b) / 2)
        self.view_matrix[2][0] = ((r + l) / 2)
        self.view_matrix[2][1] = ((t + b) / 2)
