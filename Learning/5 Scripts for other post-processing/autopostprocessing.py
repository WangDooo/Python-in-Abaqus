# coding: UTF-8

import odbAccess
from abaqus import *
from abaqusConstants import *
import visualization

# 将当前视口中的ODB文件赋予变量vp
vp = session.viewports[session.currentViewportName]
odb = vp.displayedObject

# 将背景改为白色
session.graphicsOptions.setValues(backgroundColor='#FFFFFF', backgroundStyle=SOLID)
# 将最后一个分析步的最后一帧设置为当前分析步和分析帧
lastStepIndex = len(odb.steps)-1
lastFrameIndex = len(odb.steps.values()[-1].frames)-1
vp.odbDisplay.setFrame(step=lastStepIndex, frame=lastFrameIndex)
# 在变形图模式下绘制Mises应力的云图
vp.odbDisplay.setDeformedVariable('U')
vp.odbDisplay.setPrimaryVariable(variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT,'Mises'))
vp.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))
vp.view.fitView() # 将对象布满视窗
# 将默认图注替换为用户自定义图注
vp.viewportAnnotationOptions.setValues(state=OFF)
vp.plotAnnotation(mdb.Text(name='Text:1', offset=(40,12), text='Mises stress at the final configuration'))
# 保存至PNG文件
session.printOptions.setValues(rendition=COLOR, vpDecorations=OFF, vpBackground=OFF)
vp.view.setValues(nearPlane=1727, farPlane=2938, width=1460, height=683, viewOffsetX= 58, viewOffsetY=-56)
session.printToFile(fileName='finalStress', format=PNG, canvasObjects=(vp,))
