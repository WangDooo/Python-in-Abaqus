# coding: UTF-8

from odbAccess import *

# 提取场变量
odb = openOdb(path='new_seal.odb')
fixSet = odb.rootAssembly.elementSets['FIX1']
field = odb.steps.values()[-1].frames[-1].fieldOutputs['S']
subField = field.getSubset(region=fixSet)

# 求总应力
sum_val = 0
for val in subField.values:
	sum_val += val
ave = sum_val/len(subField.values)

print('components of stress,	total stress,	mean stress')
labels = field.componentLabels

for i in range(len(labels)):
	print('%s    			%5.3e	 %6.3e' % (labels[i], sum_val.data[i], ave.data[i]))