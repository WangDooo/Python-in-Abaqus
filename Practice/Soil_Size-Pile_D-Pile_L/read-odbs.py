# coding:utf8
# from odbAccess import *
import re

file = 'jobNames.csv'
with open(file,"r", encoding="utf-8") as f:
	lines = f.readlines()

uFile = open('output.csv','a')
for line in lines:
	line = line.strip('\n')
	job = line
	line = re.sub('p','.',line)
	Re_pl = line.split('-')[0]
	Re_pd = line.split('-')[1]
	Re_ss = line.split('-')[2]
	Re_times_d = float(Re_ss)/float(Re_pd)
	jobName = job+'.odb'
	
	odb = openOdb(path=jobName)

	step = odb.steps['Step-dym']

	top_point = odb.rootAssembly.instances['PART-PILE-1'].nodeSets['SET-TOPPOINT']
	max_u1 = -9999

	for frame in step.frames:
		u = frame.fieldOutputs['U']
		point_u = u.getSubset(region=top_point)
		for v in point_u.values:
			if abs(v.data[0]) > max_u1:
				max_u1 = abs(v.data[0]) 

	uFile.write('%s,%s,%s,%s,%s \n' % (Re_pl,Re_pd,Re_times_d,Re_ss,max_u1))

uFile.close()