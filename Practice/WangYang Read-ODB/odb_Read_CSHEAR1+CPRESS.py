# coding:UTF-8

from odbAccess import *
import re

odb = openOdb(path='wy.odb')

which_side = 'you side'

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
if which_side == 'you side':
	side_area = 3.1415*pile_diameter/4*pile_height
if which_side == 'zuo side':
	side_area = 3.1415*pile_diameter/4*pile_height
if which_side == 'all side--embed':
	side_area = 3.1415*pile_diameter/2*pile_height

#
node_side_area = side_area / side_num



# input node_coordinate(x,y) output cos,sin projection
def project(x,y):
	dx = abs(x-center_point_X)
	dy = abs(y-center_point_Y)
	c = (dx**2 + dy**2)**0.5
	return [dx/c, dy/c]

# output_P.csv
file_name = 'output_' + which_side + '_P.csv'
file_summary_name = 'summary_' + which_side + '_P.csv'
file_height_name = 'height_' +  which_side + '_P.csv'
with open(file_name, "w") as f_w:
	with open(file_summary_name, "w") as f_w_summary:
		with open(file_height_name, "w") as f_w_height:
			# f_w all information
			f_w.write('Center_point_X,'+str(center_point_X)+'\n')
			f_w.write('Center_point_Y,'+str(center_point_Y)+'\n')
			f_w.write('Side_num,'+str(side_num)+'\n')
			f_w.write('Side_area,'+str(side_area)+'\n')
			f_w.write('Node_side_area,'+str(node_side_area)+'\n')
			# f_w model node infromation 
			pile_z = [] # pile node height(z)
			for i in range(side_num):
				temp_z = round(side.nodes[i].coordinates[2],3)
				if temp_z not in pile_z:
					pile_z.append(temp_z)
			pile_z.sort(reverse=True) # [12->6] up to down
			# per_height 
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
			f_w_summary.write('Center_point_Y,'+str(center_point_Y)+'\n')
			f_w_summary.write('Side_num,'+str(side_num)+'\n')
			f_w_summary.write('Side_area,'+str(side_area)+'\n')
			f_w_summary.write('Node_side_area,'+str(node_side_area)+'\n')
			f_w_summary.write('StepName,Sum_P\n')
			for stepName in stepNames:
				# init Sum_moment 
				Sum_P = 0
				# fieldOutputs
				step = odb.steps[stepName]
				lastFrame = step.frames[-1]
				cshear1 = lastFrame.fieldOutputs['CSHEAR1']
				cpress = lastFrame.fieldOutputs['CPRESS']
				side_cshear1 = cshear1.getSubset(region=side)
				side_cpress = cpress.getSubset(region=side)
				# f_w detail
				f_w.write('Step,'+stepName+'\n')
				f_w.write('Node NO.,Node X,Node Y,CPRESS NO.,CPRESS,CPRESS_x,CSHEAR1,CSHEAR1_x,CPRESS_x+CSHEAR1_x\n')
				for i in range(side_num):
					node_x = side.nodes[i].coordinates[0]
					node_y = side.nodes[i].coordinates[1]
					cpress_num = side_cpress.values[i].nodeLabel
					cpress_data = side_cpress.values[i].data*node_side_area
					cpress_x = cpress_data*project(node_x,node_y)[0]
					cshear1_data = side_cshear1.values[i].data*node_side_area
					cshear1_x = cshear1_data*project(node_x,node_y)[1]
					p_x = cpress_x+cshear1_x
					Sum_P += p_x
					f_w.writelines("%s,%s,%s,%s,%s,%s,%s,%s,%s \n" % 
						(side.nodes[i].label,
						node_x,
						node_y,
						cpress_num,
						cpress_data,
						cpress_x,
						cshear1_data,
						cshear1_x,
						p_x))
				f_w.write('Sum_P,'+str(Sum_P)+'\n')
				# f_w_summary
				f_w_summary.write("%s,%s \n" % (stepName,Sum_P))
				# f_w_height
				f_w_height.write('Step,'+stepName+'\n')
				f_w_height.write('Node_height,Floor CPRESS,Floor CPRESS per m,Floor CSHEAR1,Floor CSHEAR1 per m,Floor P,Floor P per m\n')
				for i in range(len(pile_z)):
					f_p = 0.0
					f_cpress = 0.0
					f_cshera1 = 0.0
					for j in range(len(node_sameZ[i])):
						for k in range(side_num):
							if node_sameZ[i][j] == side.nodes[k].label:
								node_x = side.nodes[k].coordinates[0]
								node_y = side.nodes[k].coordinates[1]
								cpress_num = side_cpress.values[k].nodeLabel
								cpress_data = side_cpress.values[k].data*node_side_area
								cpress_x = cpress_data*project(node_x,node_y)[0]
								cshear1_data = side_cshear1.values[k].data*node_side_area
								cshear1_x = cshear1_data*project(node_x,node_y)[1]
								p_x = cpress_x+cshear1_x
								f_cpress += cpress_x
								f_cshera1 += cshear1_x
								f_p += p_x
					f_cpress_per_m = f_cpress / per_height
					f_cshera1_per_m = f_cshera1 / per_height
					f_f_p_per_m = f_p / per_height
					f_w_height.write("%s,%s,%s,%s,%s,%s,%s \n" % 
										(pile_z[i],
										f_cpress,
										f_cpress_per_m,
										f_cshera1,
										f_cshera1_per_m,
										f_p,
										f_f_p_per_m))


