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

def prime(a):
    if a < 2: return False
    if a == 2 or a == 3: return True # manually test 2 and 3   
    if a % 2 == 0 or a % 3 == 0: return False # exclude multiples of 2 and 3
 
    maxDivisor = a**0.5
    d, i = 5, 2
    while d <= maxDivisor:
        if a % d == 0: return False
        d += i 
        i = 6 - i # this modifies 2 into 4 and viceversa
 
    return True

def spiral(X, Y, img):
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
            if prime(n) == False:
                img.putpixel((cy,cx), tuple(WHITE)) 

        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy



if __name__ == '__main__':
    filename = sys.argv[1]    if len(sys.argv) > 1 else 'ulam.png'
    width = height = int(sys.argv[2])  if len(sys.argv) > 2 else 100
    dimension = (width,height)
    
    filename = '.'.join([filename,'png']) if '.' not in filename else filename

    # We start with a black image
    img = Image.new('RGBA',dimension,color=(BLACK))

    spiral(width, height, img)
    img.save(filename)
