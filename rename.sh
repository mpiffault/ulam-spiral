for a in *[0-9]*.png
do
    b=$(echo $a | cut -d t -f2)
    mv $a `printf mult%04d.%s ${b%.*} ${b##*.}`
done