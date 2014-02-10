#!/bin/bash
# convert sequence of png files into an animated gif

convert -enhance -delay 5 -loop 0 *.png youpla.gif