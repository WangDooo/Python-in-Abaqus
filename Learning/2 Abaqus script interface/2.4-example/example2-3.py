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
myOdb = visualization.openOdb(path='D:\\Coding\\Github\\Python-in-Abaqus\\Learning\\2 Abaqus script interface\\2.4-example\\viewer_tutorial.odb') # path 应该给出文件的绝对路径
myViewport.setValues(displayedObject=myOdb)

# 5. 获取Step1和Step2结束时刻的位移增量和应力增量
firstStep = myOdb.steps['Step-1']
secondStep = myOdb.steps['Step-2']

frame1 = firstStep.frames[-1]
frame2 = secondStep.frames[-1]

displacement1 = frame1.fieldOutputs['U']
displacement2 = frame2.fieldOutputs['U']
stress1 = frame1.fieldOutputs['S']
stress2 = frame2.fieldOutputs['S']

deltaDisplacement = displacement2 - displacement1
deltaStress = stress2 - stress1

# 6. 在新视口中显示deltaDisplacement
myViewport.odbDisplay.setDeformedVariable(deltaDisplacement)

# 7. 在新视口中显示deltaStress
myViewport.odbDisplay.setPrimaryVariable(field=deltaStress, outputPositio=INTEGRATION_POINT, refinement=(INVARIANT, 'Mises'))
myViewport.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))