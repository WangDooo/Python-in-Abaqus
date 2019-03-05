# -*- coding:UTF-8 -*-

# 该脚本将自动实现悬臂梁在压力荷载作用下的建模、提交分析和后处理
from abaqus import *
import testUtils
testUtils.setBackwardCompatibility()
from abaqusConstants import *

print('name = Beam it is running')
myModel = mdb.Model(name="Beam")

myViewport = session.Viewport(name='Simple Beam Example', origin=(20,20), width=150, height=120)

import part

mySketch = myModel.ConstrainedSketch(name='beamProfile', sheetSize=250)

mySketch.rectangle(point1=(-100,10), point2=(100,-10))

myBeam = myModel.Part(name='Beam', dimensionality=THREE_D, type=DEFORMABLE_BODY)

myBeam.BaseSolidExtrude(sketch=mySketch, depth=25.0)

import material

mySteel = myModel.Material(name='Steel')

elasticProperties = (209.E3, 0.3)
mySteel.Elastic(table=(elasticProperties, ))

import section

mySection = myModel.HomogeneousSolidSection(name='beamSection', material='Steel', thickness=1.0)

region = (myBeam.cells, )
myBeam.SectionAssignment(region=region, sectionName='beamSection')

import assembly

myAssembly = myModel.rootAssembly
myInstance = myAssembly.Instance(name='beamInstance', part=myBeam, dependent=OFF)

import step

myModel.StaticStep(name='beamLoad', previous='Initial', timePeriod=1.0, initialInc=0.1, description='Load the top of the beam')

import load

endFaceCenter = (-100,0,12.5)
endFace = myInstance.faces.findAt((endFaceCenter, ))

endRegion = (endFace, )
myModel.EncastreBC(name='Fixed', createStepName='beamLoad', region=endRegion)

topFaceCenter = (0,10,12.5)
topFace = myInstance.faces.findAt((topFaceCenter, ))

topSurface = ((topFace, SIDE1), )
myModel.Pressure(name='Pressure', createStepName='beamLoad', region=topSurface, magnitude=0.5)

import mesh

region = (myInstance.cells, )
elemType = mesh.ElemType(elemCode=C3D8I, elemLibrary=STANDARD)
myAssembly.setElementType(regions=region, elemTypes=(elemType, ))

myAssembly.seedPartInstance(regions=(myInstance, ), size=10.0)

myAssembly.generateMesh(regions=(myInstance, ))

myViewport.assemblyDisplay.setValues(mesh=ON)
myViewport.assemblyDisplay.meshOptions.setValues(meshTechnique=ON)
myViewport.setValues(displayedObject=myAssembly)

import job
jobName = 'beam_job'
myJob = mdb.Job(name=jobName, model='Beam', description='beam test')

myJob.submit()
myJob.waitForCompletion()
print('go to the after do')

import visualization

myOdb = visualization.openOdb(path=jobName+'.odb')
myViewport.setValues(displayedObject=myOdb)
myViewport.odbDisplay.display.setValues(plotState=CONTOURS_ON_DEF)
myViewport.odbDisplay.commonOptions.setValues(renderStyle=FILLED)

session.printToFile(fileName='Mises', format=PNG, canvasObjects=(myViewport, ))
print('Done it is over')
