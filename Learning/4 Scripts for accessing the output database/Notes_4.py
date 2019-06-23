------------------------------------------
第四章 编写脚本访问输出数据库
------------------------------------------
4.1 简介
------------------------------------------
4.1.1 三组概念
(1) model	model database	output database
(2) model data 		result data
(3) field output 	histoty output
1. 模型 model 
包含任意多个部件及其相关属性
每个模型中只能包含1个装配件
同一模型数据库中的不同模型各自相互独立
2. 模型数据库 model database
拓展名.cae 建议每个模型数据库中只包含1个模型
3. 输出数据库 output database
拓展名 .odb 节点场输出和单元历史场输出
4. 模型数据和结果数据
模型数据：部件、材料、边界条件、物理常数
结果模型：分析步step和帧frame有关
5. 场输出和历史输出
4.1.2 使用对象模型编写脚本
odb.steps['10 hz vibration'].frames[3].fieldOutputs['U'].values[47]
对象模型实质上是Abaqus脚本接口命令的结构层次关系

------------------------------------------
4.2 输出数据库对象模型
------------------------------------------
包括 1.model data 2. results data
4.2.1 模型数据
parts 
root assembly 每个输出数据库对象模型中只能包含1个根装配
part instances
regions
materials
sections
section assignments
section categories
调用prettyPrint方法可以查看输出数据库的状态和对象模型的层次结构关系
from odbAccess import *
from textRepr import *
odb = openOdb('newbeam3d.odb')
prettyPrint(odb, 2)
4.2.2 结果模型
1. 分析步 steps
crushStep = odb.steps['Crush']
2. 帧 frames
crushFrame = crushStep.frames[-1]
3. 场输出 field output
场输出可以输出某个计算结果的所有分量，数据信息量非常大
stress = crushFrame.fieldOutputs['S']
4. 历史输出 histoty output
为某个点或模型的小部分区域定义结果输出，可以输出分析结果的某个单独变量
u2Deflection = endPoint.histotyOutputs['U2']
HistoryRegion对象可以定义为：节点、积分点、某个区域、材料点、整个模型
endPoint = crushStep.histotyRegions['end point']
给定历史输出对象u2Deflection后，提取结果的命令
for time, value in u2Deflection.data:
	print('Time:',time,'U2 deflection:',value)

------------------------------------------
4.3 从（向）输出数据库读取（写入）数据
------------------------------------------
4.3.1 打开（创建）输出数据库
打开 openOdb()
from odbAccess import *
odb = openOdb(path='new_viewer_tutorial.odb')
创建 构造函数Odb
odb = Odb(name='myData', analysisTitle='derived data', description='test problem', path='testWrite.odb')
odb.save()

4.3.2 读取（写入）模型数据
4.3.2.1 读取模型数据
1. 根装配	每个输出数据库对象模型中只能包含1个根装配
myAssembly = odb.rootAssembly
2. 部件实例
for instanceName in odb.rootAssembly.instances.keys():
	print(instanceName)
3. 区域
print('Node sets=', odb.rootAssembly.nodeSets.keys())
print('Node sets=', odb.rootAssembly.instances['PART-1-1'].nodeSets.keys())
print('Element sets=', odb.rootAssembly.instances['PART-1-1'].elementSets.keys())
topNodeSet = odb.rootAssembly.instances['PART-1-1'].nodeSets['TOP']
4. 材料
allMaterials = odb.materials
for materialName in allMaterials.keys():
	print('Material Name:', materialName)
输出所有material对象的各向同性弹性材料
for material in allMaterials.values():
	if hasattr(material,'elastic'):
		elastic = material.elastic
		if elastic.type == 'ISOTROPIC':
			print('isotropic elastic behavior, type=', elastic.moduli)
		title1 = 'Young modulus Poisson ratio'
		title2 = ''
		if elastic.temperatureDependency == ON:
			title2 = 'Temperature'
		dep = elastic.dependencies
		title3 = ''
		for x in range(dep):
			title3 += 'field#'+str(x)
		print(title1,title2,title3)
		for dataline in elastic.table:
			print(dataline)
	else:
		print('NO elastic')
输出超性材料
if hasattr(material, 'hyperelastic'):
	hyperelastic = material.hyperelastic
	testData = hyperelastic.testData
	if testData == 'ON':
		if hasattr(hyperelastic, 'biaxiaTestData'):
			biaxiaTestData = hyperelastic.biaxiaTestData
			print('smoothing type:', biaxiaTestData.smoothing)
5. 截面
allSections = odb.sections
for sectionName in allSections.keys():
	print('Section Name:', sectionName)

for mySection in allSections.values():
	temp_s = str(type(mySection)).replace("<type '",'').replace("'>",'')
	if temp_s == 'HomogeneousSolidSection':
		print('material name =', mySection.material)
		print('thickness =', mySection.thickness)
6. 截面分配
截面分配的目的是将部件实例的单元与截面属性建立联系
instances = odb.rootAssembly.instances
for instance in instances.values():
	assignments = instance.sectionAssignments
	print('Instance:', instance.name)
	for sa in assignments:
		region = sa.region
		elements = region.elements
		print('Section:', sa.sectionName)
		print('Elements associated with this section:')
		for e in elements:
			print('label:',e.label)

4.3.2.2 写入模型数据
1. 部件
创建 构造函数Odb
odb = Odb(name='myData', analysisTitle='derived data', description='test problem', path='testWrite.odb')
odb.save()

part1 = odb.Part(name='part-1', embeddedSpace=THREE_D, type=DEFORMABLE_BODY)
调用addNodes通过指定节点编号和节点坐标来添加节点信息
nodeData = ((1,1,0,0),(2,2,0,0),(3,2,1,0.1),(4,1,1,0.1),(5,2,-1,-0.1),(6,1,-1,-0.1),)
part1.addNodes(nodeData=nodeData, nodeSetName='nset-1')
创建节点和节点集后，还应该创建单元并指定单元类型 调用addElements方法向部件中添加单元
sCat = odb.SectionCategory(name='S5', description='Five-Layered Shell')
spBot = sCat.SectionPoint(number=1, description='Bottom')
spMid = sCat.SectionPoint(number=3, description='Middle')
spTop = sCat.SectionPoint(number=5, description='Top')
elementData = ((1,1,2,3,4), (2,6,5,2,1),)
part1.addElements(elementData=elementData, type='S4', elementSetName='eset-1', sectionCategory=sCat)
2.根装配
odb.
3. 部件实例
a = odb.rootAssembly
instancel = a.Instance(name='part-1-1', object=part1)
注：只能对部件添加节点和单元，而不允许对部件实例添加节点和单元
4. 区域
# 创建部件实例单元集
eLabels = [9,99]
elementSet = instancel.ElementSetFromElementLabels(name='elsetA', elementLabels=eLabels)
# 创建根装配下的节点集
nodeLabels = (5,11)
instanceName = 'part-1-1'
nodeSet = assembly.NodeSetFromNodeLabels(name='nodesetRA', ((instanceName, nodeLabels), ))
5. 材料
from abaqusConstants import *  引用这个句 才定义type
material_1 = odb.Material(name='Elastic Material')
material_1.Elastic(type=ISOTROPIC, table=((12000,0.3),))
6. 截面
创建Section对象之前必须首先创建Material对象，如果Material对象不存在，将抛出异常
sectionName = 'Homogeneous Solid Section'
materialName = 'Elastic Material'
mySection = odb.HomogeneousSolidSection(name=sectionName, material=materialName, thickness=2.0)
再例如 调用CircularProfile构造函数创建圆形梁截面
profileName = 'Circular Profile'
radius = 10.0
odb.CircularProfile(name='profileName', r=radius) 
7. 截面分配
elLabels = (1,2)
elset = instancel.ElementSetFromElementLabels(name=materialName, elementLabels=elLabels)
instancel.assignSection(region=elset, section=mySection)

4.3.3 读取（写入）结果数据
4.3.3.1 读取结果数据
1. 分析步steps
调用keys()方法可以获得结果数据的库关键字
for stepName in odb.steps.keys():
	print(stepName)

step1 = odb.steps.values()[0]
print(step1.name)
2. 帧(frames)
lastFrame = odb.steps['Step-1'].frames[-1]
print(lastFrame)
4.3.3.2 写入结果数据
1. 分析步 steps
构造函数 可以为 time domain		frequency domain	 modal domain
step1 = odb.Step(name='step-1', description='', domain=TIME, timePeriod=1.0)
2. 帧 frames
frame1 = step1.Frame(incrementNumber=1, frameValue=0.1, description='')

4.3.4 读取（写入）场输出数据
4.3.4.1 读取场输出数据 
场输出数据存储在OdbFrame对象的场输出库fieldOutputs中
for fieldName in lastFrame.fieldOutputs.keys():
	print(fieldName)
提示：从输出数据库中读取场输出数据时可以定义不同的读取频率。因此，每一帧中并非都包含所有的场输出变量。
# 输出最后一帧中场输出变量的名称、描述、成员类型
for f in lastFrame.fieldOutputs.values():
	print(f.name,f.description)
	print('Type:',f.type)
	# 对于每个计算量，输出其位置
	for loc in f.locations:
		print('Position:', loc.position)

# 读取场输出变量中各个数据值
displacement = lastFrame.fieldOutputs['U']
fieldValues = displacement.values
# 对于每个位移值，输出节点编号和节点坐标值
for v in fieldValues:
	print('Node=%d U[x]=%6.4f , U[y]=%6.4f' %(v.nodeLabel, v.data[0], v.data[1]))

还可以使用区域参数读取场输出数据的子集
使用模型数据创建OdbSet对象后，就可以调用getSubset方法读取区域上的场输出数据。通常情况下读入节点集或单元集数据。
center = odb.rootAssembly.instances['PART-1-1'].nodeSets['PUNCH']
centerDisplacement = displacement.getSubset(region=center)
centerValues = centerDisplacement.values
for v in centerValues:
	print(v.nodeLabel, v.data)

4.3.4.2 写入场输出数据 【没啥用，就先不看了】

4.3.5 读取（写入）历史输出数据
4.3.5.1 读取历史输出数据
历史输出区域可以是1个节点、1个积分点、某个区域或1个材料点，而不允许对多个点进行历史输出
场输出与帧有关，而历史输出则与分析步有关。
历史输出数据储存在OdbStep对象的historyRegions库中。
对于 时域分析(domain=MODAL)、频域分析(domain=FREQUENCY)、模态域分析(domain=MODAL)
序列分别是由 (stepTime, value)       (frequency, value)            (mdoel, value) 组成的元组

# 例：将第二个分析步的历史输出数据U2写入文件
from odbAccess import *
odb = openOdb(path='new_viewer_tutorial.odb')
step2 = odb.steps['Step-2']
region = step2.historyRegions['Node PART-1-1.1000']
u2Data = region.historyOutputs['U2'].data
dispFile = open('disp.dat','w')
for time, u2Disp in u2Data:
	dispFile.write('%10.4E %10.4E \n' % (time, u2Disp))
dispFile.close()

4.3.5.2 写入历史输出数据【没啥用，就先不看了】

4.3.6 设置默认的显示变量
默认的显示变量设置适用于分析步的所有帧。
# 例：选择位移U作为某个分析步场变量和变形后场变量的默认设置
field = odb.steps['impact'].frames[1].fieldOutputs['U']
odb.steps['impact'].setDefaultField(field)
odb.steps['impact'].setDefaultDeformField(field)
------------------------------------------

------------------------------------------
4.4 计算Abaqus得到的分析结果
------------------------------------------
4.4.1 数学运算规则

4.4.2 有效的数学运算

4.4.3 粗略计算
提供两个粗略计算命令
maxEnvelope()	minEnvelope()
(env, lcIndex) = maxEnvelope([field1, field2,...])
(env, lcIndex) = minEnvelope([field1, field2,...])

(env, lcIndex) = maxEnvelope([field1, field2,...], invariant)
(env, lcIndex) = minEnvelope([field1, field2,...], invariant)

(env, lcIndex) = maxEnvelope([field1, field2,...], componentLabel)
(env, lcIndex) = minEnvelope([field1, field2,...], componentLabel)

Envelope命令返回env和lcIndex两个FieldOutput对象
env:表示搜索到的极值
lcIndex:表示与搜索到极值对应的场变量索引号
invariant和componentLabel为可选参数 
若从向量和张量中搜索极值，必须使用符号常数

4.4.4 结果转换 【暂时用不到】
如果场变量为向量或张量，Abaqus脚本接口支持在直角坐标系、柱坐标系和球坐标系之间进行结果转换。
------------------------------------------

------------------------------------------
4.5 实例
------------------------------------------
4.5.4 读取节点信息和单元信息
节点和单元信息属于模型数据，因此需要访问根装配对象rootAssembly
odb_Node_Element_Information.py 
------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------