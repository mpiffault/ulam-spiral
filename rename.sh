#!/bin/bash
# Rename files with numbers by adding leading zeros
# Here only for file of the form mult[0-9]{1,4}.png

# TODO more open version

for a in *[0-9]*.png
do
    b=$(echo $a | cut -d t -f2)
    mv $a `printf mult%04d.%s ${b%.*} ${b##*.}`
done