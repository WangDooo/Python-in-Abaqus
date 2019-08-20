# coding:UTF-8

from odbAccess import *
import re

odb = openOdb(path='wy.odb')

which_side = 'zuo side'

stepNames = ['load-1-05','load-2-10','load-3-15','load-4-20','load-5-25','load-6-30','load-7-35','load-8-40','load-9-45','load-10-50']

# center point mdoel information
center_point = odb.rootAssembly.instances['PILE-1'].nodeSets['top point']
center_point_X = center_point.nodes[0].coordinates[0]

# side mdoel information
side = odb.rootAssembly.instances['PILE-1'].nodeSets[which_side]
side_num = len(side.nodes)

# model size
pile_height = 6.0
pile_diameter = 2.0

# side_area
if which_side == 'you side':
	side_area = 3.1415*pile_diameter/4*pile_height
if which_side == 'zuo side':
	side_area = 3.1415*pile_diameter/4*pile_height
if which_side == 'all side--embed':
	side_area = 3.1415*pile_diameter/2*pile_height

node_side_area = side_area / side_num

# output.csv
file_name = 'output_' + which_side + '.csv'
file_summary_name = 'summary_' + which_side + '.csv'
file_height_name = 'height_' +  which_side + '.csv'
with open(file_name, "w") as f_w:
	with open(file_summary_name, "w") as f_w_summary:
		with open(file_height_name, "w") as f_w_height:
			# f_w all information
			f_w.write('Center_point_X,'+str(center_point_X)+'\n')
			f_w.write('Side_num,'+str(side_num)+'\n')
			f_w.write('Side_area,'+str(side_area)+'\n')
			f_w.write('Node_side_area,'+str(node_side_area)+'\n')
			# f_w model node infromation
			pile_z = []
			for i in range(side_num):
				temp_z = round(side.nodes[i].coordinates[2],3)
				if temp_z not in pile_z:
					pile_z.append(temp_z)
			pile_z.sort(reverse=True)
			per_height = pile_height / len(pile_z)
			node_sameZ = []
			for z in pile_z:
				temp_list_z = []
				for i in range(side_num):
					temp_z = round(side.nodes[i].coordinates[2],3)
					if z == temp_z:
						temp_list_z.append(side.nodes[i].label)
				node_sameZ.append(temp_list_z)
			f_w.write('Floor_num,'+str(len(pile_z))+'\n')
			f_w.write('Node_floor_num,'+str(len(node_sameZ[0]))+'\n')
			f_w.write('Z,NodeLabel\n')
			for i in range(len(pile_z)):
				temp_sameZ = str(node_sameZ[i]).strip().strip('[]')
				f_w.write('%s,%s \n' % (pile_z[i],temp_sameZ))
			# file_summary
			f_w_summary.write('Center_point_X,'+str(center_point_X)+'\n')
			f_w_summary.write('Side_num,'+str(side_num)+'\n')
			f_w_summary.write('Side_area,'+str(side_area)+'\n')
			f_w_summary.write('Node_side_area,'+str(node_side_area)+'\n')
			f_w_summary.write('StepName,Sum_moment\n')
			for stepName in stepNames:
				# init Sum_moment 
				Sum_moment = 0
				# fieldOutputs
				step = odb.steps[stepName]
				lastFrame = step.frames[-1]
				cshear2 = lastFrame.fieldOutputs['CSHEAR2']
				side_cshear2 = cshear2.getSubset(region=side)
				f_w.write('Step,'+stepName+'\n')
				f_w.write('Node NO.,Node X,Arm of Force,CSHEAR2 NO.,Node CSHEAR2,Node Moment\n')
				for i in range(side_num):
					arm = abs(side.nodes[i].coordinates[0]-center_point_X)
					cshear2_data = side_cshear2.values[i].data
					cshear2_num = side_cshear2.values[i].nodeLabel
					moment = arm*cshear2_data*node_side_area
					Sum_moment += moment
					f_w.writelines("%s,%s,%s,%s,%s,%s \n" % (side.nodes[i].label,side.nodes[i].coordinates[0],arm,cshear2_num,cshear2_data,moment))
				f_w.write('Sum_Moment,'+str(Sum_moment)+'\n')
				f_w_summary.write("%s,%s \n" % (stepName,Sum_moment))
				f_w_height.write('Step,'+stepName+'\n')
				f_w_height.write('Node_height,Floor Moment,Floor Moment per m\n')
				for i in range(len(pile_z)):
					f_moment = 0.0
					f_moment_per_m = 0.0
					for j in range(len(node_sameZ[i])):
						for k in range(side_num):
							if node_sameZ[i][j] == side.nodes[k].label:
								arm = abs(side.nodes[k].coordinates[0]-center_point_X)
								cshear2_data = side_cshear2.values[k].data
								cshear2_num = side_cshear2.values[k].nodeLabel
								moment = arm*cshear2_data*node_side_area
								moment_per_m = moment / per_height
								f_moment += moment
								f_moment_per_m += moment_per_m
					f_w_height.write(str(pile_z[i])+','+str(f_moment)+','+str(f_moment_per_m)+'\n')


