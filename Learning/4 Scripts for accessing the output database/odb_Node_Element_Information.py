# coding:UTF-8

from odbAccess import *

odb = openOdb(path='new_viewer_tutorial.odb')

assembly = odb.rootAssembly

numNodes = 0
numElements = 0

for name, instance in assembly.instances.items():
	n = len(instance.nodes)
	print('Number of Nodes %s : %d' % (name,n))
	numNodes += n
	print('Coordinate of Nodes:')

	# 对部件实例中的每个节点，输出节点编号和节点坐标
	# 对于三维部件，节点坐标为XYZ; 二维部件只有XY
	if instance.embeddedSpace == THREE_D:
		print('X Y Z')
		for node in instance.nodes:
			print(node.coordinates)
	else:
		print('X Y')
		for node in instance.nodes:
			print(node.label, node.coordinates)

	# 对每个部件实例中的单元，输出单元编号、单元类型、节点数、单元连接
	m = len(instance.elements)
	print('Element of Part', name,':',m)
	numElements += m
	print('Connection of elements')
	print('Number	Type	Connection')
	for element in instance.elements:
		print('%5d %8s' % (element.label, element.type))
		for nodeNum in element.connectivity:
			print('%4d' % nodeNum)
			print('\n')

print('Number of Instances', len(assembly.instances))
print('Number of elements', numElements)
print('Number of Nodes', numNodes)
odb.close