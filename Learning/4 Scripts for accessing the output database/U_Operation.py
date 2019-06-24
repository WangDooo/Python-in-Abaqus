# coding:UTF-8


from odbAccess import *

odb = openOdb(path='new_fieldOperation.odb')

field1 = odb.steps['LC1'].frames[1].fieldOutputs['U']
field2 = odb.steps['LC2'].frames[1].fieldOutputs['U']

deltaDisp = field2 - field1

# 保存为新的场变量，并创建对应的分析步和帧
newStep = odb.Step(name='user2', description='user defined results', domain=TIME, timePeriod=0)
newFrame = newStep.Frame(incrementNumber=0, frameValue=0.0)
newField = newFrame.FieldOutput(name='U', description='delta displacements', type=VECTOR)
newField.addData(field=deltaDisp)

odb.save()