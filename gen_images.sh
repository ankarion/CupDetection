#!/bin/bash

blender scenes/cup_scene.blend --python scripts/gen_obj.py -b
echo 'finished rendering'
python scripts/gen_description.py
cd images

for f in $(ls pos/ | head -1)
do
	echo $f
	opencv_createsamples -img pos/$f -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 600 -w 50 -h 50
	((id+=1))
done

echo 'all images generated'

opencv_createsamples -info info/info.lst -num 600 -w 50 -h 50 -vec positives.vec
