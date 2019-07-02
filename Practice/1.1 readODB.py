# coding:utf8

from odbAccess import *

odb = openOdb(path='Job-1.odb')

step = odb.steps['Step-1']

point = odb.rootAssembly.nodeSets['SET-PILETOPPOINT']

lastFrame = step.frames[-1]

u = lastFrame.fieldOutputs['U']

u_point = u.getSubset(region=point)


uFile = open('U2.csv','w')
uFile.write('nodeLabel,U2 \n')

for uValue in u_point.values:
    uFile.write('NO.%s, %f \n' % (uValue.nodeLabel, uValue.data[1]))