**Installation**
Things you need to have before you start:
* blender
* OpenCV

**Generating your own haar cascade**
***download "bad" images***
All the bad images are downloaded from image-net database. Assuming that the
application will be tested in room, only corresonding images of room were used.

***generate "good" images***
In "scenes/" directory you can find .blend file, where you can find a 3D cup we
will look for. It is a blender file with the camera and object(cup) in the
scene. Tweak this model so that it will look like a real object you want to
track.

In "scripts/" directory you can find a gen_obj.py script which will rotate the
object called "cup" and rotate it over x,y and z axes. But this script may be
tricky to run.

There is a script "gen_images.sh" in root directory. It creates rotated images
and maps them to a "bad" images, which are supposed to be downloaded to 
"images/neg/" directory.

**Running program**
