# Assignment4: The Clipper
import numpy as np
from bitarray import bitarray
from vertex import *


def clipLine(P0, P1, top, bottom, right, left):
    def recompute_outcodes(p):
        code = bitarray([False] * 4)
        if p.x < left:
            code[3] = 1
        elif p.x > right:
            code[2] = 1
        if p.y < bottom:
            code[1] = 1
        elif p.y > top:
            code[0] = 1
        return code

    # get slope
    m = (P0.y - P1.y) / (P0.x - P1.x)
    B = P0.y - (m * P0.x)
    while True:
        # recompute outcodes
        code_p0 = recompute_outcodes(P0)
        code_p1 = recompute_outcodes(P1)
        # check if trivial accept
        if (code_p0 | code_p1) == bitarray('0000'):
            return np.asarray([P0, P1])
        # check if trivial reject
        if (code_p0 & code_p1) != bitarray('0000'):
            return np.asarray([])
        # check if P0 is outside
        if P0.x < left or P0.x > right or P0.y < bottom or P0.y > top:
            if P0.x < left:
                # clip against left edge
                P0.x, P0.y = left, (m * left) + B
            elif P0.x > right:
                # clip against right edge
                P0.x, P0.y = right, P0.y = (m * right) + B
            elif P0.y < bottom:
                # clip against bottom edge
                P0.y, P0.x = bottom, (m * bottom) + B
            elif P0.y > top:
                # clip against top edge
                P0.y, P0.x = top, (m * top) + B
        # check if P1 is outside
        if P1.x < left or P1.x > right or P1.y < bottom or P1.y > top:
            if P1.x < left:
                # clip against left edge
                P1.x, P1.y = left, (m * left) + B
            elif P1.x > right:
                # clip against right edge
                P1.x, P1.y = right, (m * right) + B
            elif P1.y < bottom:
                # clip against bottom edge
                P1.y, P1.x = bottom, (m * bottom) + B
            elif P1.y > top:
                # clip against top edge
                P1.y, P1.x = top, (m * top) + B
        return np.asarray([P0, P1])


def clipPoly(vertices, top, bottom, right, left):
    def inside(p, e):
        if e == 'right':
            return p.x <= right
        elif e == 'top':
            return p.y <= top
        elif e == 'left':
            return p.x >= left
        elif e == 'bottom':
            return p.y >= bottom

    def computeIntersection(s, p, e):
        A = Vertex(0, 0, s.r, s.g, s.b)
        if s.x == p.x:
            m = float('inf')
        else:
            m = (p.y - s.y) / (p.x - s.x)

        if e == 'right':
            A.x = right
            A.y = s.y + (A.x - s.x) * m
        elif e == 'top':
            A.y = top
            A.x = s.x + (A.y - s.y) / m
        elif e == 'left':
            A.x = left
            A.y = s.y + (A.x - s.x) * m
        elif e == 'bottom':
            A.y = bottom
            A.x = s.x + (A.y - s.y) / m
        return A

    def output(p):
        outputList.append(p)

    outputList = vertices
    for edge in ['right', 'top', 'left', 'bottom']:
        inputList = outputList
        if len(inputList) == 0:
            return np.array([])
        outputList = []
        S = inputList[-1]
        for P in inputList:
            if inside(P, edge):
                if not inside(S, edge):
                    output(computeIntersection(S, P, edge))
                output(P)
            else:
                if inside(S, edge):
                    output(computeIntersection(P, S, edge))
            S = P
    return np.asarray(outputList)

