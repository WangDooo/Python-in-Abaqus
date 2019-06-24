# coding:UTF-8

from odbAccess import *

odb = openOdb(path='new_viewer_tutorial.odb')

step1 = odb.steps['Step-1']

lastFrame = step1.frames[-1]

center = odb.rootAssembly.instances['PART-1-1'].nodeSets['PUNCH']

displacement = lastFrame.fieldOutputs['U']

centerDisplacement = displacement.getSubset(region=center)

for v in centerDisplacement.values:
	print('position:', v.position)
	print('type:', v.type)
	print('NO. node:', v.nodeLabel)
	print('U_x:', v.data[0])
	print('U_y:', v.data[1])
	print('U_magnitude:', v.magnitude)

odb.close