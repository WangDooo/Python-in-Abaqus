# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__



def Macro1():
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
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=100.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.Line(point1=(-0.25, 0.0), point2=(-25.0, 0.0))
    s.HorizontalConstraint(entity=g[2], addUndoState=False)
    s.Line(point1=(-25.0, 0.0), point2=(-25.0, 50.0))
    s.VerticalConstraint(entity=g[3], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
    s.Line(point1=(-25.0, 50.0), point2=(-0.25, 50.0))
    s.HorizontalConstraint(entity=g[4], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    s.Line(point1=(-0.25, 50.0), point2=(-0.25, 40.0))
    s.VerticalConstraint(entity=g[5], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
    s.Line(point1=(-0.25, 40.0), point2=(0.25, 40.0))
    s.HorizontalConstraint(entity=g[6], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    s.Line(point1=(0.25, 40.0), point2=(0.25, 50.0))
    s.VerticalConstraint(entity=g[7], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
    s.Line(point1=(0.25, 50.0), point2=(25.0, 50.0))
    s.HorizontalConstraint(entity=g[8], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
    s.Line(point1=(25.0, 50.0), point2=(25.0, 0.0))
    s.VerticalConstraint(entity=g[9], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
    s.Line(point1=(25.0, 0.0), point2=(0.25, 0.0))
    s.HorizontalConstraint(entity=g[10], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
    s.Line(point1=(0.25, 0.0), point2=(-0.25, 0.0))
    s.HorizontalConstraint(entity=g[11], addUndoState=False)
    s.ParallelConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=80.193, 
        farPlane=108.369, width=143.172, height=67.1388, cameraPosition=(
        2.39696, 19.8524, 94.2809), cameraTarget=(2.39696, 19.8524, 0))
    p = mdb.models['Model-1'].Part(name='Part-Soil', dimensionality=TWO_D_PLANAR, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-Soil']
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-Soil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Part-Soil']
    f, e, d1 = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f[0], sketchPlaneSide=SIDE1, origin=(0.0, 
        24.95992, 0.0))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=141.42, gridSpacing=3.53, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Part-Soil']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    s1.Line(point1=(-0.25, 15.04008), point2=(-0.25, -24.95992))
    s1.VerticalConstraint(entity=g[12], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[7], entity2=g[12], addUndoState=False)
    s1.Line(point1=(0.25, 15.04008), point2=(0.25, -24.95992))
    s1.VerticalConstraint(entity=g[13], addUndoState=False)
    s1.ParallelConstraint(entity1=g[6], entity2=g[13], addUndoState=False)
    p = mdb.models['Model-1'].parts['Part-Soil']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    e1, d2 = p.edges, p.datums
    p.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=100.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.0, 0.0), point2=(0.5, 10.0))
    p = mdb.models['Model-1'].Part(name='Part-Pile', dimensionality=TWO_D_PLANAR, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-Pile']
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-Pile']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='Material-Soil')
    mdb.models['Model-1'].materials['Material-Soil'].Density(table=((1900.0, ), ))
    mdb.models['Model-1'].materials['Material-Soil'].Elastic(table=((15000000.0, 
        0.4), ))
    mdb.models['Model-1'].Material(name='Material-Pile')
    mdb.models['Model-1'].materials['Material-Pile'].Density(table=((2500.0, ), ))
    mdb.models['Model-1'].materials['Material-Pile'].Elastic(table=((34500000000.0, 
        0.2), ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-Soil', 
        material='Material-Soil', thickness=None)
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-Pile', 
        material='Material-Pile', thickness=None)
    p = mdb.models['Model-1'].parts['Part-Pile']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(faces=faces, name='Set-Pile')
    p = mdb.models['Model-1'].parts['Part-Pile']
    p.SectionAssignment(region=region, sectionName='Section-Pile', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['Model-1'].parts['Part-Soil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['Part-Soil']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
    region = p.Set(faces=faces, name='Set-Soil')
    p = mdb.models['Model-1'].parts['Part-Soil']
    p.SectionAssignment(region=region, sectionName='Section-Soil', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Part-Pile']
    a.Instance(name='Part-Pile-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['Part-Soil']
    a.Instance(name='Part-Soil-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=131.284, 
        farPlane=151.559, width=115.617, height=52.0851, viewOffsetX=20.1429, 
        viewOffsetY=22.6829)
    a = mdb.models['Model-1'].rootAssembly
    a.translate(instanceList=('Part-Pile-1', ), vector=(-0.25, 40.0, 0.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=125.363, 
        farPlane=157.48, width=180.762, height=81.4325, viewOffsetX=28.4706, 
        viewOffsetY=37.0013)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=124.79, 
        farPlane=158.053, width=179.936, height=81.0606, viewOffsetX=25.6143, 
        viewOffsetY=4.95319)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=130.216, 
        farPlane=152.627, width=114.452, height=51.5604, viewOffsetX=16.4121, 
        viewOffsetY=2.47917)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
        maxNumInc=100000)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
        'S', 'U'))
    mdb.models['Model-1'].historyOutputRequests['H-Output-1'].suppress()
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
        constraints=ON, connectors=ON, engineeringFeatures=ON, 
        adaptiveMeshConstraints=OFF)
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
        leaf=leaf)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Part-Soil-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#7 ]', ), )
    leaf = dgm.LeafFromGeometry(faceSeq=faces1)
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=135.844, 
        farPlane=146.999, width=56.8245, height=25.5992, viewOffsetX=8.17634, 
        viewOffsetY=11.4975)
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-Pile-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
    a.Set(edges=edges1, name='Set-Pile-b')
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Part-Pile-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#a ]', ), )
    a.Surface(side1Edges=side1Edges1, name='Surf-Pile-l')
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
        leaf=leaf)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Part-Pile-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
    leaf = dgm.LeafFromGeometry(faceSeq=faces1)
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-Soil-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#800 ]', ), )
    a.Set(edges=edges1, name='Set-Soil-b')
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Part-Soil-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#50 ]', ), )
    a.Surface(side1Edges=side1Edges1, name='Surf-Soil-l')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=136.379, 
        farPlane=146.464, width=51.36, height=23.1375, viewOffsetX=10.5937, 
        viewOffsetY=-16.924)
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-Soil-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#602 ]', ), )
    a.Set(edges=edges1, name='Set-Soil-Bottom')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=127.581, 
        farPlane=155.262, width=158.244, height=71.2883, viewOffsetX=51.155, 
        viewOffsetY=5.70192)
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-Soil-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#104 ]', ), )
    a.Set(edges=edges1, name='Set-Soil-side')
    a = mdb.models['Model-1'].rootAssembly
    region1=a.sets['Set-Pile-b']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.sets['Set-Soil-b']
    mdb.models['Model-1'].Tie(name='Constraint-P-S', master=region1, slave=region2, 
        positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
        thickness=ON)
    mdb.models['Model-1'].ContactProperty('IntProp-P-S')
    mdb.models['Model-1'].interactionProperties['IntProp-P-S'].NormalBehavior(
        pressureOverclosure=HARD, allowSeparation=ON, 
        constraintEnforcementMethod=DEFAULT)
    mdb.models['Model-1'].interactionProperties['IntProp-P-S'].TangentialBehavior(
        formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
        pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
        table=((0.4, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
        fraction=0.005, elasticSlipStiffness=None)
    a = mdb.models['Model-1'].rootAssembly
    region1=a.surfaces['Surf-Pile-l']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.surfaces['Surf-Soil-l']
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-P-S', 
        createStepName='Step-1', master=region1, slave=region2, sliding=FINITE, 
        thickness=ON, interactionProperty='IntProp-P-S', adjustMethod=NONE, 
        initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, interactions=OFF, constraints=OFF, 
        engineeringFeatures=OFF)
    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['Set-Soil-side']
    mdb.models['Model-1'].DisplacementBC(name='BC-side', createStepName='Step-1', 
        region=region, u1=0.0, u2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
        distributionType=UNIFORM, fieldName='', localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['Set-Soil-Bottom']
    mdb.models['Model-1'].DisplacementBC(name='BC-bottom', createStepName='Step-1', 
        region=region, u1=0.0, u2=0.0, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
        distributionType=UNIFORM, fieldName='', localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, interactions=ON, constraints=ON, 
        engineeringFeatures=ON)
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
        leaf=leaf)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=137.388, 
        farPlane=145.454, width=41.0611, height=18.4979, viewOffsetX=12.996, 
        viewOffsetY=18.4343)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Part-Soil-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#7 ]', ), )
    leaf = dgm.LeafFromGeometry(faceSeq=faces1)
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=140.07, 
        farPlane=142.773, width=13.7444, height=6.19182, viewOffsetX=4.42574, 
        viewOffsetY=22.7823)
    a = mdb.models['Model-1'].rootAssembly
    v1 = a.instances['Part-Pile-1'].vertices
    verts1 = v1.getSequenceFromMask(mask=('[#4 ]', ), )
    a.Set(vertices=verts1, name='Set-PIleTopPoint')
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-Pile-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#4 ]', ), )
    a.Set(edges=edges1, name='Set-Pile-top')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, interactions=OFF, constraints=OFF, 
        engineeringFeatures=OFF)
    leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
        leaf=leaf)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Part-Pile-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
    region = a.Surface(side1Edges=side1Edges1, name='Surf-Pile-t')
    mdb.models['Model-1'].Pressure(name='Load-pile', createStepName='Step-1', 
        region=region, distributionType=UNIFORM, field='', magnitude=-1000.0, 
        amplitude=UNSET)
    mdb.models['Model-1'].loads['Load-pile'].setValues(magnitude=1000.0)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
        bcs=OFF, predefinedFields=OFF, connectors=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Part-Soil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Part-Soil']
    p.seedPart(size=2.5, deviationFactor=0.1, minSizeFactor=0.1)
    elemType1 = mesh.ElemType(elemCode=CPE4, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=CPE3, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['Part-Soil']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#7 ]', ), )
    pickedRegions =(faces, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
    p = mdb.models['Model-1'].parts['Part-Soil']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['Part-Pile']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['Part-Pile']
    p.seedPart(size=0.5, deviationFactor=0.1, minSizeFactor=0.1)
    elemType1 = mesh.ElemType(elemCode=CPE4, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=CPE3, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['Part-Pile']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(faces, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
    p = mdb.models['Model-1'].parts['Part-Pile']
    p.generateMesh()
    a1 = mdb.models['Model-1'].rootAssembly
    a1.regenerate()
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=20, 
        numDomains=20, numGPUs=0)
    mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
    session.mdbData.summary()
    o3 = session.openOdb(name='E:/WangBochen/Abaqus/2019-07-01/test/Job-1.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))


Macro1()

from odbAccess import *

odb = openOdb(path='Job-1.odb')

step = odb.steps['Step-1']

point = odb.rootAssembly.nodeSets['SET-PILETOPPOINT']

lastFrame = step.frames[-1]

u = lastFrame.fieldOutputs['U']

u_point = u.getSubset(region=point)


uFile = open('U2.csv','w')
uFile.write('nodeLabel,U2 \n')

for uValue in u_point.values:
    uFile.write('NO.%s, %f \n' % (uValue.nodeLabel, uValue.data[1]))