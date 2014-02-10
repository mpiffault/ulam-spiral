#!/usr/bin/env python2.7
# coding: utf-8
# draw an ulam spiral
# Author : Martin Piffault
# Spiral path algorithm from :
# http://stackoverflow.com/questions/398299/looping-in-a-spiral

# First parameter gives output file name, default: ulam.png
# Second parameter gives external side of the spiral in pixels, default: 100

import sys
from PIL import Image
import math

WHITE = (0xff, 0xff, 0xff, 0xff)
BLACK = (0x00, 0x00, 0x00, 0xff)

def spiral(X, Y, img, mult):
    nb_num = X*Y
    nb_tenth = nb_num / 10
    x = y = 0
    dx = 0
    dy = -1
    n = 0
    ok = 0
    for i in range(max(X, Y)**2):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            n += 1
            cx = (X/2)-x
            cy = (Y/2)-y
            if n % nb_tenth == 0:
                print (n/nb_tenth)*10, '%'


            
            n % mult == 0 and img.putpixel((cy,cx), tuple(WHITE))

        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy

if __name__ == '__main__':
    filename = sys.argv[1]    if len(sys.argv) > 1 else 'mult'
    width = height = int(sys.argv[2])  if len(sys.argv) > 2 else 100
    nb_mult = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    dimension = (width,height)

    for i in range(1, nb_mult):
        filenamef = filename + str(i) + ".png"

    # We start with a black image
        img = Image.new('RGBA',dimension,color=(BLACK))

        spiral(width, height, img, i)

        img.save(filenamef)
