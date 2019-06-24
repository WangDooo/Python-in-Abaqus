# coding:UTF-8

# 搜索当前视口输出数据库文件中的最大Mises应力
# 要求：视口中必须打开某个输出数据库文件，否则异常

from abaqus import *
from abaqusConstants import *
import visualization
import displayGroupOdbToolset as dgo

# 对当前视口中的输出数据库进行操作
vp = session.viewports[session.currentViewportName]
odb = vp.displayedObject
if type(odb) != visualization.OdbType:
	ex = Exception('current Viewport must show odb file')
	raise ex

# 搜索最大Mises应力
maxValue = None
stressOutputExists = False
for step in odb.steps.values():
	print('Searching the step:', step.name)
	for frame in step.frames:
		try:
			stress = frame.fieldOutputs['S']
			stressOutputExists = True
		except KeyError:	# 跳过不包含应力输出的帧
			continue
		for stressValue in stress.values:
			if (not maxValue or stressValue.mises>maxValue.mises):
				maxValue = stressValue
				maxStep, maxFrame = step, frame

# 如果odb文件中没有输出应力结果，则抛出异常
if not stressOutputExists:
	ex = Exception('No S result in the odb file')
	raise ex

# 输出最大Mises应力的详细信息
print('The max Mises:',maxValue.mises)
print('Step:', maxStep.name)
print('Frame:', maxFrame.frameId)
print('InstanceName:', maxValue.instance.name)
print('ElementLabel:', maxValue.elementLabel)
print('SectionPoint:', maxValue.sectionPoint)
print('IntegrationPoint:', maxValue.integrationPoint)

# 对最大Mises应力所在单元设置红色进行高亮显示
leaf = dgo.Leaf(ALL_SURFACES)
vp.odbDisplay.displayGroup.remove(leaf)
leaf = dgo.LeafFromElementLabels(partInstanceName=maxValue.instance.name, elementLabels=(maxValue.elementLabel,))
vp.setColor(leaf=leaf, fillColor='Red')
vp.odbDisplay.commonOptions.setValues(renderStyle=FILLED, elementShrink=ON, elementShrinkFactor=0.15)
vp.odbDisplay.display.setValues(plotState=(UNDEFORMED,))
