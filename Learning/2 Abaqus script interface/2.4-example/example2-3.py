# -*- coding:UTF-8 -*-

# 1. 写注释行
"""
改脚本的功能是打开输出数据库文件，将不同分析步最后一帧的计算
结果进行求差运算，并绘制计算结果的云图
"""

# 2. 导入相应模块
from abaqus import *
from abaqusConstants import *
import visualization

# 3. 创建新视口函数
myViewport = session.Viewport(name='Superposition example', origin=(10,10), width=150, height=100)


# 4. 打开输出数据库
myOdb = visualization.openOdb(path=viewer_tutorial.odb)

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