# coding:UTF-8

from odbAccess import *
import re

odb = openOdb(path='wy.odb')

which_side = 'bottom pile-you'

stepNames = ['load-1-05','load-2-10','load-3-15','load-4-20','load-5-25','load-6-30','load-7-35','load-8-40','load-9-45','load-10-50']

# center point mdoel information
center_point = odb.rootAssembly.instances['PILE-1'].nodeSets['top point']
center_point_X = center_point.nodes[0].coordinates[0]
center_point_Y = center_point.nodes[0].coordinates[1]

# side mdoel information
side = odb.rootAssembly.instances['PILE-1'].nodeSets[which_side]
side_num = len(side.nodes)

# model size
pile_height = 6.0
pile_diameter = 2.0

# side_area
side_area = 3.1415*1*1/4
node_side_area = side_area / side_num

# how much node on the side
num_NodeOnSide = 0
for i in range(side_num):
	r = (side.nodes[i].coordinates[0]-center_point_X)**2 + (side.nodes[i].coordinates[1]-center_point_Y)**2
	print(abs(r - (pile_diameter/2)**2))
	if ( abs(r - (pile_diameter/2)**2) ) < 0.0001:
		num_NodeOnSide += 1

#  CPRESS in load-v
step_v = odb.steps['load-v']
lastFrame_v = step_v.frames[-1]
cpress_v = lastFrame_v.fieldOutputs['CPRESS']
side_cpress_v = cpress_v.getSubset(region=side)

# output.csv
file_name = 'output_' + which_side + '.csv'
file_summary_name = 'summary_' + which_side + '.csv'
with open(file_name, "w") as f_w:
	with open(file_summary_name, "w") as f_w_summary:
		# f_w detail information
		f_w.write('Center_point_X,'+str(center_point_X)+'\n')
		f_w.write('Side_num,'+str(side_num)+'\n')
		f_w.write('Side_area,'+str(side_area)+'\n')
		f_w.write('Node_side_area,'+str(node_side_area)+'\n')
		
		# file_summary
		f_w_summary.write('Center_point_X,'+str(center_point_X)+'\n')
		f_w_summary.write('Side_num,'+str(side_num)+'\n')
		f_w_summary.write('Side_area,'+str(side_area)+'\n')
		f_w_summary.write('Node_side_area,'+str(node_side_area)+'\n')
		f_w_summary.write('StepName,Sum_Cpress,Sum_Moment\n')
		for stepName in stepNames:
			# init Sum_moment 
			Sum_Moment = 0.0
			Sum_CShear1 = 0.0
			# fieldOutputs
			step = odb.steps[stepName]
			lastFrame = step.frames[-1]
			cshear1 = lastFrame.fieldOutputs['CSHEAR1']
			side_cshear1 = cshear1.getSubset(region=side)
			cpress = lastFrame.fieldOutputs['CPRESS']
			side_cpress = cpress.getSubset(region=side)

			f_w.write('Step,'+stepName+'\n')
			f_w.write('Node NO.,Node X,Arm of Force,CSHEAR1 NO.,Node CSHEAR1 data,CSHEAR1*area,CPRESS NO.,Node CPRESS data,CPRESS_Delta,CPRESS_Delta*area,Node Moment\n')
			for j in range(side_num):
				i = j+num_NodeOnSide
				arm = abs(side.nodes[j].coordinates[0]-center_point_X)
				# cshear1
				cshear1_num = side_cshear1.values[i].nodeLabel
				cshear1_data = side_cshear1.values[i].data
				cshear1_area = cshear1_data*node_side_area
				Sum_CShear1 += cshear1_area
				# cpress
				cpress_num = side_cpress.values[i].nodeLabel
				cpress_data = side_cpress.values[i].data
				cpress_data_delta = side_cpress.values[i].data - side_cpress_v.values[i].data
				cpress_area = cpress_data_delta*node_side_area
				cpress_moment = arm*cpress_area		
				Sum_Moment += cpress_moment

				f_w.writelines("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s \n" % 
								(side.nodes[j].label,
								side.nodes[j].coordinates[0],
								arm,
								cshear1_num,
								cshear1_data,
								cshear1_area,
								cpress_num,
								cpress_data,
								cpress_data_delta,
								cpress_area,
								cpress_moment))
			f_w.write('Sum_CShear1,'+str(Sum_CShear1)+'\n')
			f_w.write('Sum_Moment,'+str(Sum_Moment)+'\n')
			f_w_summary.write("%s,%s,%s \n" % (stepName,Sum_CShear1,Sum_Moment))
			


