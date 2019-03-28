# -*- coding:UTF-8 -*-
# 1. 导入相应模块，创建新模型
from abaqus import *
from abaqusConstants import *
from caeModules import *
Mdb() # 创建模型数据库对象

# 2. 绘制二维草图
myModel = mdb.Model(name='Model A')
mySketch = myModel.ConstrainedSketch(name='Sketch A', sheetSize=200.0)
xyCoordsInner = ((-5,20), (5,20), (15,0), (-15,0), (-5,20))
xyCoordsOuter = ((-10,30), (10,30), (40,-30), (30,-30), (20,-10), (-20,-10), (-30,-30), (-40,-30), (-10,30))
for i in range(len(xyCoordsInner)-1):
	mySketch.Line(point1=xyCoordsInner[i], point2=xyCoordsInner[i+1])
for i in range(len(xyCoordsOuter)-1):
	mySketch.Line(point1=xyCoordsOuter[i], point2=xyCoordsOuter[i+1])

# 3.创建部件并对草图增加拉伸特性
myPart = myModel.Part(name='Part A', dimensionality=THREE_D, type=DEFORMABLE_BODY)
myPart.BaseSolidExtrude(sketch=mySketch, depth=20.0) 

# 4.创建部件实例
myAssembly = mdb.models['Model A'].rootAssembly
myInstance = myAssembly.Instance(name='Part A-1', part=myPart, dependent=OFF)

# 5.布置网格种子 创建新视口 显示划分网格后的部件实例
partInstances = (myInstance,)
myAssembly.seedPartInstance(regions=partInstances, size=5.0)
myAssembly.generateMesh(regions=partInstances)
myViewport = session.Viewport(name='Viewport for Model A', origin=(20,20), width=150, height=100)
myViewport.assemblyDisplay.setValues(renderStyle=SHADED, mesh=ON)
myViewport.setValues(displayedObject=myAssembly)