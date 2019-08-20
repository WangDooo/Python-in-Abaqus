# coding:utf8

from abaqus import *
from abaqusConstants import *


import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior

# 1. Part
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=5.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, Re_pd_r))
p = mdb.models['Model-1'].Part(name='Part-pile', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-pile']
p.BaseSolidExtrude(sketch=s, depth=Re_pl)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-pile']
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['Part-pile']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#4 ]', ), )
p.Set(faces=faces, name='Set-pile-b')
p = mdb.models['Model-1'].parts['Part-pile']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#1 ]', ), )
p.Surface(side1Faces=side1Faces, name='Surf-pile-l')
p = mdb.models['Model-1'].parts['Part-pile']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#2 ]', ), )
p.Surface(side1Faces=side1Faces, name='Surf-pile-top')
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=60.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.rectangle(point1=(0.0, 0.0), point2=(Re_ss, Re_ss))
p = mdb.models['Model-1'].Part(name='Part-soil', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-soil']
p.BaseSolidExtrude(sketch=s1, depth=60.0)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-soil']
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['Part-soil']
f, e = p.faces, p.edges
t = p.MakeSketchTransform(sketchPlane=f[4], sketchUpEdge=e[7], sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(Re_s_half, Re_s_half, 60.0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=120.13, gridSpacing=3.0, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-soil']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, Re_pd_r))
p = mdb.models['Model-1'].parts['Part-soil']
f1, e1 = p.faces, p.edges
p.CutExtrude(sketchPlane=f1[4], sketchUpEdge=e1[7], sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, sketch=s, depth=Re_pl, flipExtrudeDirection=OFF)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['Part-soil']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.Set(cells=cells, name='Set-soil-all')
p = mdb.models['Model-1'].parts['Part-soil']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2 ]', ), )
p.Set(faces=faces, name='Set-soil-b')
p = mdb.models['Model-1'].parts['Part-soil']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#28 ]', ), )
p.Set(faces=faces, name='Set-soil-y')
p = mdb.models['Model-1'].parts['Part-soil']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#14 ]', ), )
p.Set(faces=faces, name='Set-soil-x')
p = mdb.models['Model-1'].parts['Part-soil']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#80 ]', ), )
p.Set(faces=faces, name='Set-soil-Bottom')
p = mdb.models['Model-1'].parts['Part-soil']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#1 ]', ), )
p.Surface(side1Faces=side1Faces, name='Surf-soil-l')
p = mdb.models['Model-1'].parts['Part-soil']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
f = p.faces
p.PartitionCellByExtendFace(extendFace=f[0], cells=pickedCells)
p = mdb.models['Model-1'].parts['Part-soil']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
v1, e, d1 = p.vertices, p.edges, p.datums
p.PartitionCellByPlaneThreePoints(cells=pickedCells, point1=p.InterestingPoint(edge=e[7], rule=MIDDLE), point2=p.InterestingPoint(edge=e[2], rule=CENTER), point3=p.InterestingPoint(edge=e[14], rule=MIDDLE))
p = mdb.models['Model-1'].parts['Part-soil']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#f ]', ), )
v2, e1, d2 = p.vertices, p.edges, p.datums
p.PartitionCellByPlaneThreePoints(cells=pickedCells, point1=p.InterestingPoint(edge=e1[28], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[22], rule=MIDDLE), point3=p.InterestingPoint(edge=e1[32], rule=MIDDLE))
p = mdb.models['Model-1'].parts['Part-pile']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
v1, e, d1 = p.vertices, p.edges, p.datums
p.PartitionCellByPlaneThreePoints(point1=v1[0], cells=pickedCells, point2=p.InterestingPoint(edge=e[0], rule=MIDDLE), point3=p.InterestingPoint(edge=e[1], rule=MIDDLE))
p = mdb.models['Model-1'].parts['Part-pile']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
v2, e1, d2 = p.vertices, p.edges, p.datums
p.PartitionCellByPlaneThreePoints(cells=pickedCells, point1=p.InterestingPoint(edge=e1[7], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[5], rule=MIDDLE), point3=p.InterestingPoint(edge=e1[6], rule=MIDDLE))
p = mdb.models['Model-1'].parts['Part-pile']
v = p.vertices
verts = v.getSequenceFromMask(mask=('[#1 ]', ), )
p.Set(vertices=verts, name='Set-TopPoint')

# 2. Material
mdb.models['Model-1'].Material(name='Material-pile')
mdb.models['Model-1'].materials['Material-pile'].Density(table=((2.5, ), ))
mdb.models['Model-1'].materials['Material-pile'].Elastic(table=((34500000.0, 0.2), ))
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-pile', material='Material-pile', thickness=None)
p = mdb.models['Model-1'].parts['Part-pile']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#f ]', ), )
region = p.Set(cells=cells, name='Set-pile')
p = mdb.models['Model-1'].parts['Part-pile']
p.SectionAssignment(region=region, sectionName='Section-pile', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].Material(name='Material-soil')
mdb.models['Model-1'].materials['Material-soil'].Depvar(n=4)
mdb.models['Model-1'].materials['Material-soil'].UserMaterial(mechanicalConstants=(100.0, 0.0, 0.3, 3.14))
p = mdb.models['Model-1'].parts['Part-soil']
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-soil', material='Material-soil', thickness=None)
p = mdb.models['Model-1'].parts['Part-soil']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#ff ]', ), )
region = p.Set(cells=cells, name='Set-soil')
p = mdb.models['Model-1'].parts['Part-soil']
p.SectionAssignment(region=region, sectionName='Section-soil', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

# 3. Assembly  
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Part-pile']
a.Instance(name='Part-pile-1', part=p, dependent=ON)
p = mdb.models['Model-1'].parts['Part-soil']
a.Instance(name='Part-soil-1', part=p, dependent=ON)
a = mdb.models['Model-1'].rootAssembly
a.translate(instanceList=('Part-pile-1', ), vector=(Re_s_half, Re_s_half, Re_trans_h))

# 4. Step
mdb.models['Model-1'].StaticStep(name='Step-dym', previous='Initial', timePeriod=2.0, maxNumInc=1000, timeIncrementationMethod=FIXED, initialInc=0.05, noStop=OFF)  
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=('U', ))
mdb.models['Model-1'].historyOutputRequests['H-Output-1'].suppress()

# 5. Interaction
a = mdb.models['Model-1'].rootAssembly
region1=a.instances['Part-pile-1'].sets['Set-pile-b']
a = mdb.models['Model-1'].rootAssembly
region2=a.instances['Part-soil-1'].sets['Set-soil-b']
mdb.models['Model-1'].Tie(name='Constraint-1', master=region1, slave=region2, positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
mdb.models['Model-1'].ContactProperty('IntProp-p-s')
mdb.models['Model-1'].interactionProperties['IntProp-p-s'].TangentialBehavior(formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, table=((0.4, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, fraction=0.005, elasticSlipStiffness=None)
mdb.models['Model-1'].interactionProperties['IntProp-p-s'].NormalBehavior(pressureOverclosure=HARD, allowSeparation=ON, constraintEnforcementMethod=DEFAULT)
a = mdb.models['Model-1'].rootAssembly
region1=a.instances['Part-pile-1'].surfaces['Surf-pile-l']
a = mdb.models['Model-1'].rootAssembly
region2=a.instances['Part-soil-1'].surfaces['Surf-soil-l']
mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-1', createStepName='Step-dym', master=region1, slave=region2, sliding=FINITE, thickness=ON, interactionProperty='IntProp-p-s', adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, clearanceRegion=None)

# 6. Load
mdb.models['Model-1'].PeriodicAmplitude(name='Amp-1', timeSpan=STEP, frequency=3.14, start=0.0, a_0=0.0, data=((0.0, 1.0), ))
e1 = a.instances['Part-soil-1'].edges
v11 = a.instances['Part-soil-1'].vertices
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Part-pile-1'].surfaces['Surf-pile-top']
mdb.models['Model-1'].SurfaceTraction(name='Load-1', createStepName='Step-dym', region=region, magnitude=2000.0, amplitude='Amp-1', directionVector=(a.instances['Part-soil-1'].InterestingPoint(edge=e1[15], rule=CENTER), v11[2]), distributionType=UNIFORM, field='', localCsys=None)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Part-soil-1'].sets['Set-soil-Bottom']
mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Step-dym', region=region, u1=0.0, u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Part-soil-1'].sets['Set-soil-x']
mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Step-dym', region=region, u1=0.0, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Part-soil-1'].sets['Set-soil-y']
mdb.models['Model-1'].DisplacementBC(name='BC-3', createStepName='Step-dym', region=region, u1=UNSET, u2=0.0, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)

# 7. Mesh
p = mdb.models['Model-1'].parts['Part-soil']
p = mdb.models['Model-1'].parts['Part-pile']   
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['Part-pile']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#f ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, elemType3))
p = mdb.models['Model-1'].parts['Part-pile']
p.seedPart(size=0.5, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-pile']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
p = mdb.models['Model-1'].parts['Part-pile']
p = mdb.models['Model-1'].parts['Part-soil']  
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['Part-soil']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#ff ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, elemType3))
p = mdb.models['Model-1'].parts['Part-soil']
p.seedPart(size=1, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-soil']
p.generateMesh()


# 8. Job
a = mdb.models['Model-1'].rootAssembly  
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()   
import job
mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
mdb.models['Model-1'].keywordBlock.replace(71, """
** ----------------------------------------------------------------
**
** STEP: Step-dym
**
*Initial conditions, type=solution
Part-soil-1.Set-soil-all, 100, 1.0, 0.1, 0""")
mdb.Job(name='Re_jobName', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='main.for', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=20, 
    numDomains=20, numGPUs=0)
mdb.jobs['Re_jobName'].submit(consistencyChecking=OFF)

import datetime
nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('log.txt','a') as f_log:
	f_log.write('Re_jobName '+nowTime+' submit \n')