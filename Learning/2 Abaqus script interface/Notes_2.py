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
2.2 Abaqus 脚本接口基础知识
------------------------------------------
使用《Abaqus Scripting Reference Manual》
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
4. 布尔类型 Booleans
5. 序列 sequences
Abaqus脚本接口中定义了由相同类型对象组成的专门序列
1） 由几何对象（顶点、边等）组成的GeomSequence序列
2） 由节点或单元组成的MeshSequence序列
3） 由表面组成的SurfSequence序列
成员edges faces vertices cells ips 均由GeomSequence对象派生而来

创建名为Switch的三维变形体部件
from abaqusConstants import *
mdb.Model('Body')
mySketch = mdb.models['Body'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mySketch.rectangle(point1=(0.0,0.0), point2=(70.0,70.0))
switch = mdb.models['Body'].Part(name='Switch', dimensionality=THREE_D, type=DEFORMABLE_BODY)
switch.BaseSolidExtrude(sketch=mySketch, depth=20.0)
------------------------------------------
面向对象编程与Abaqus脚本接口
1. 脚本接口中的方法
print(mdb.models['Model-1'].parts['Part-1'].vertices[0].pointOn) # 输入Part-1第1个顶点的坐标
2. 脚本接口中的成员
Abaqus对象的成员具有只读属性，因此，不允许使用赋值语句指定成员的值
可以调用 setValues() 方法来改变成员值

脚本接口中构造函数、方法和成员的使用方法实例
见 constructor_method_member.py
------------------------------------------
异常和异常处理
1. 标准Abaqus脚本接口异常
（1）InvalidNameError 脚本中定义了无效的名字
（2）RangeError 数据值超出定义范围
（3）AbaqusError 建模过程中的操作与前后设置的相关性
（4）AbaqusException 同上
2. 其他Abaqus脚本接口异常
3. 错误处理 error handling
try:
	session.Viewport(name='tiny', width=1, height=1)
except RangeError, message:
	print('Viewport is too small:', message)
print('Script continues running and prints this line')
------------------------------------------
2.3 在CAE中使用脚本接口
------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------