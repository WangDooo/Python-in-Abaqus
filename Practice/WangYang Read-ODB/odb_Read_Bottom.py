# coding:UTF-8

from odbAccess import *
import re

odb = openOdb(path='wy.odb')

which_side = 'em pile-yb'

stepNames = ['load-1-88','load-2-177','load-3-354','load-4-707','load-5-1061','load-6-1500','load-7-2000','load-8-2500']

# center point mdoel information
center_point = odb.rootAssembly.instances['PILE-1'].nodeSets['top point']
center_point_X = center_point.nodes[0].coordinates[0]
center_point_Y = center_point.nodes[0].coordinates[1]

# side mdoel information
side = odb.rootAssembly.instances['PILE-1'].nodeSets[which_side]
side_num = len(side.nodes)

# model size
pile_height = 31.0
pile_diameter = 6.0
side_x_num = 7

length_element = pile_diameter/2.0/(side_x_num-1)

# side_area
side_area = 3.1415*pile_diameter*pile_diameter/4.0/4.0
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

# sort node by x
pile_x = []
for i in range(side_x_num):
	pile_x.append(center_point_X+i*length_element)
node_sameX = []
for x in pile_x:
	temp_list_x = []
	for i in range(side_num):
		temp_x = round(side.nodes[i].coordinates[0],3)
		if (temp_x >= x-(length_element/2)) and (temp_x < x+(length_element/2)):
			temp_list_x.append(side.nodes[i].label)
	node_sameX.append(temp_list_x)
# output.csv
file_name = 'output_' + which_side + '.csv'
file_summary_name = 'summary_' + which_side + '.csv'
file_x_name = 'x_' + which_side + '.csv'
with open(file_name, "w") as f_w:
	with open(file_summary_name, "w") as f_w_summary:
		with open(file_x_name, "w") as f_w_x:
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
				# f_w
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

				# f_w_x
				f_w_x.write('Step,'+stepName+'\n')
				f_w_x.write('Node X,Node label,X_CSHEAR1*area,X_CPRESS_Delta*area\n')
				for i in range(len(pile_x)):
					x_cshear1 = 0.0
					x_cpress = 0.0
					temp_list = [str(tl) for tl in node_sameX[i]]
					node_label = "-".join(temp_list)
					for j in range(len(node_sameX[i])):
						for k in range(side_num):
							# 
							if node_sameX[i][j] == side.nodes[k].label:
								kk = k + num_NodeOnSide
								# cshear1
								cshear1_data_x = side_cshear1.values[kk].data
								cshear1_area_x = cshear1_data_x*node_side_area
								x_cshear1 += cshear1_area_x
								# cpress
								cpress_data_x = side_cpress.values[kk].data
								cpress_data_delta_x = side_cpress.values[kk].data - side_cpress_v.values[kk].data
								cpress_area_x = cpress_data_delta_x*node_side_area
								x_cpress += cpress_area_x
					f_w_x.write("%s,%s,%s,%s \n" %  (pile_x[i],node_label,x_cshear1,x_cpress))

			


