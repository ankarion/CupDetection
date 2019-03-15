import bpy
import mathutils
from math import radians

scene = bpy.context.scene
cup = scene.objects["Cup"]

i=0
steps = 10
delta = 360./10
for dz in range(steps):
	for dy in range(steps):
		for dx in range(steps):
			cup.rotation_euler = (radians(dx*delta),radians(dy*delta),radians(dz*delta))
			i+=1
			imageName = ""+str(i)
			bpy.context.scene.render.filepath = 'images/pos/renderedCup-' + imageName
			bpy.context.scene.render.filepath += ".png"
			bpy.ops.render.render(write_still=True)
