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

------------------------------------------

------------------------------------------
4.4
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

------------------------------------------

------------------------------------------

------------------------------------------

------------------------------------------