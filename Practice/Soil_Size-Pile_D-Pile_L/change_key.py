import re
from decimal import *

# 打开Keywords的模板py文件 
with open('odb-in-keywords.py', "r", encoding="utf-8") as f:
	# readlines以列表的形式将文件读出
	lines = f.readlines()

# 设定循环范围 保存为数字列表
pile_length = [i for i in range(10,11)]			 # 测试 1组 桩长
pile_diameter = [i*0.1 for i in range(10,15,2)]  # 6组
soil_size_TimesOfDiameter = [10,5,3]
# soil_size_TimesOfDiameter = [20,10,9,8,7,6,5,4,3,2]

# 循环改变 以上变量
for p_l in pile_length:
	for p_d in pile_diameter:
		for soil_s_t in soil_size_TimesOfDiameter:
			soil_size = p_d*soil_s_t
			# 定义change的字典
			r_pd = round(p_d,2)
			r_pd_radius = round(r_pd/2,2)
			r_pl = round(p_l,2)
			r_ss = round(soil_size,2)
			r_ss_half = round(r_ss/2,2)
			r_trans_height = round(60.0-r_pl,2)
			r_times_d = round(soil_s_t,2)
			jobName = str(r_pl).replace('.','p')+'-'+str(r_pd).replace('.','p')+'-'+str(r_ss).replace('.','p')
			re_dict = { 'Re_pd_r':str(r_pd_radius), 
						'Re_pd':str(r_pd), 
						'Re_pl':str(r_pl),
						'Re_ss':str(r_ss), 
						'Re_s_half':str(r_ss_half),
						'Re_trans_h':str(r_trans_height),
						'Re_times_d':str(r_times_d),
						'Re_jobName':jobName}
			# 为保存的文件命名 
			# ！！！Abaqus的Job名中不能有标点符号
			file_name = str(r_pl)+'-'+str(r_pd)+'-'+str(r_ss)+'.py'

			# 替换部分
			with open(file_name, "w", encoding="utf-8") as f_w:
				for line in lines:
					re_line = line
					for v in re_dict:
						re_line = re.sub(v, re_dict[v], re_line)
					f_w.writelines(re_line)
			# 根据Script.py名称 生成bat
			with open('runPy_NoGUI.bat', "a", encoding="utf-8") as bat_w:
				str_bat = "call abaqus cae noGUI="+file_name+"\n"
				bat_w.write(str_bat)

			with open('jobNames.csv','a',encoding='utf-8') as f_jobNames:
				f_jobNames.write(jobName+'\n')

with open('output.csv','a',encoding='utf-8') as f_output:
	f_output.write('Pile Length,Pile Diameter,Soil dimension multiple,Soil Size,Max U1 \n')



