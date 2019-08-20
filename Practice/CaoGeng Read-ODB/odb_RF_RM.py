# coding:UTF-8

from odbAccess import *
import re
import sys

job_num = 15

output_file = 'RF_RM_temp.csv'

with open(output_file, "w") as f_w:
	for job_N in range(1,job_num+1):
		job_name = 'job-'+str(job_N)+'.odb'
		odb = openOdb(path=job_name)
		finial_step = odb.steps['LOAD-DISP']
		RF_point = odb.rootAssembly.nodeSets['SET-1RF']
		f_w.write('job-'+str(job_N))
		for frame in finial_step.frames:
			Reaaction_force=frame.fieldOutputs['RF']  
			RF_Re_f = Reaaction_force.getSubset(region=RF_point)    
			for fValue in RF_Re_f.values:
				f_w.write(",%s" % (fValue.data[0]/5000))
		f_w.write('\n')
		f_w.write(' ')
		for frame in finial_step.frames:
			Reaaction_Moment = frame.fieldOutputs['RM']  
			RF_Re_M = Reaaction_Moment.getSubset(region=RF_point)    
			for MValue in RF_Re_M.values:
				f_w.write(',%s' % (MValue.data[1]/50000))
		f_w.write('\n')
		print(job_name,'Done')

	