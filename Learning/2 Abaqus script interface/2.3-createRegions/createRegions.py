# -*- coding:UTF-8 -*-
# 导入脚本中使用的各个模块
from abaqus import *
from abaqusConstants import *
from caeModules import *
# 创建新模型
myModel = mdb.models['Model-1']
# 使用构造函数Viewport创建新的视口
myViewport = session.Viewport(name='Region syntax', origin=(20,20), width=200, height=100)
mySketch = myModel.Sketch(name='Sketch A', sheetSize=200.0)
mySketch.rectangle(point1=(-40.0,30.0), point2=(-10.0,0.0))
mySketch.rectangle(point1=(10.0,30.0), point2=(40.0,0.0))
# 对创建的矩形进行拉伸操作，生成三维部件
door = myModel.Part(name='Door', dimensionality=THREE_D, type=DEFORMABLE_BODY)
door.BaseSolidExtrude(sketch=mySketch, depth=20.0)
# 创建部件实例
myAssembly = myModel.rootAssembly
doorInstance = myAssembly.Instance(name='Door-1', part=door, dependent=OFF)
# 选择两个顶点
pillarVertices = doorInstance.vertices.findAt(((-40,30,0),),((40,0,0),))
# 创建静力分析步static
myModel.StaticStep(name='impact', previous='Initial', initialInc=1, timePeriod=1)
# 在选择的顶点上施加集中力
myPillarLoad = myModel.ConcentratedForce(name='pillarForce', createStepName='impact', region=(pillarVertices,), cf1=12.5E4)
# 选择两个面
topFace = doorInstance.faces.findAt(((-25,30,10),))
bottomFace = doorInstance.faces.findAt(((-25,0,10),))
# 在选择的面上施加压力 pressure
# 同一部件实例相同类型的实体，可以使用+号
myFenderLoad = myModel.Pressure(name='pillarPressure', createStepName='impact', region=((topFace+bottomFace, SIDE1),), magnitude=10E4)
# 在同一部件实例上选择两条边
myEdge1 = doorInstance.edges.findAt(((10,15,20),))
myEdge2 = doorInstance.edges.findAt(((10,15,0),))
# 对一个面、两条边和两个顶点施加边界条件
myDisplacementBC = myModel.DisplacementBC(name='xBC', createStepName='impact', region=(pillarVertices, myEdge1+myEdge2, topFace), u1=5.0)
# 使用面上的任意点选择两个面
faceRegion = doorInstance.faces.findAt(((-30,15,20),),((30,15,20),))
# 创建包含两个面的表面surface
mySurface = myModel.rootAssembly.Surface(name='exterior', side1Faces=faceRegion)
# 使用这个表面来创建弹性地基(elastic foundation)
myFoundation = myModel.ElasticFoundation(name='elasticFloor', createStepName='Initial', surface=mySurface, stiffness=1500)
# 显示施加荷载和边界条件后的装配件
myViewport.setValues(displayedObject = myAssembly)
myViewport.assemblyDisplay.setValues(step='impact', loads=ON, bcs=ON, predefinedFields=ON)
