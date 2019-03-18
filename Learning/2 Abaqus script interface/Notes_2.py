------------------------------------------
使用Abaqus Command

abaqus cae script = myscript.py
abaqus cae startup = myscript.py

abaqus viewer script = myscript.py
abaqus viewer startup = myscript.py

不启动Abaqus/CAE而直接运行脚本
abaqus cae noGUI = myscript.py
abaqus viewer noGUI = myscript.py
------------------------------------------
Abaqus 脚本接口基础知识
1. 命令的排列顺序
2. 访问(access)对象
新对话session,CAE将导入所有模块
sideLoadStep = session.odb['Forming load'].steps['Side load']
lastFrame = sideLoadStep.frames[-1] # 最后一帧
stressData = lastFrame.fieldOutputs['S'] # 最后一帧的Mises应力
integrationPointData = stressData.getSubset(position = INTEGRATION_POINT) # 积分点处的Mises应力
invariantsData = stressData.validInvariants # 访问对象的不变量
3. 路径 (path)
创建对象的方法称为构造函数 (constructor)
Abaqus 脚本接口惯例: 构造函数的首字母大写，其他小写
# 调用构造函数Part创建三维变形对象Part-1
mdb.models['Model-1'].Part(name='Part-1', dimendionality=THREE_D, type=DEFORMABLE_BODY) 
# 将创建的对象Part-1放入部件库parts中
mbd.models['Model-1'].parts['Part-1']
4. 参数(arguments)
函数中尽量使用关键字参数
newViewport = session.Viewport(name='myViewport', origin=(10,10), width=100, height=50)
5. 返回值(return value)
------------------------------------------
Abaqus 脚本接口中的数据类型
1. 符号常数 symbolic constants
QUAD DEFORMABLE 3D 2D ...
符号常数的所有字母必须大写
a.setMeshControls(elemShape=QUAD) #单元形状为四边形
若使用符号常数，需使用
from abaqusConstants import *
2. 库 repositories
库指的是储存某一特定类型对象的容器
mdb.models # 包含了模型数据库中的所有模型
mdb.models['Model-1'].parts # 包含了模型Model-1中的所有部件

mdb.models['engine'].Material('steel') # 调用构造函数Material创建了对象steel
steel = mdb.models['engine'].materials['steel'] # 将名为steel的材料添加到库materials中

一般情况下，库中的关键字为字符串
可以调用 keys() 方法来访问库中的关键字
for key in session.viewports.keys():
	print(key)

调用 changeKey() 可以改变库的关键字名
mdb.models['Model-1'].parts.changeKey(fromName='housing', toName='form')
3. 数组 arrays
Abaqus中所有的节点和单元分别存在数组 MeshNodeArrays 和 MeshElementArrays 中