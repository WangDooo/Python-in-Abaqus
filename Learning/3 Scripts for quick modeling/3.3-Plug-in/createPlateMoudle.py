from abaqus import *
from abaqusConstants import *

def createPlateFunction(partName, width, height, radius):
	s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
	g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
	s.setPrimaryObject(option=STANDALONE)
	s.rectangle(point1=(0.0, 0.0), point2=(width, height))
	s.CircleByCenterPerimeter(center=(width/2, height/2), point1=(width/2+radius, height/2))
	p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
	p = mdb.models['Model-1'].parts[partName]
	p.BaseShell(sketch=s)
	s.unsetPrimaryObject()
	p = mdb.models['Model-1'].parts[partName]
	session.viewports['Viewport: 1'].setValues(displayedObject=p)
	del mdb.models['Model-1'].sketches['__profile__']

