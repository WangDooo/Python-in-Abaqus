import re
from decimal import *

# 打开Keywords的模板py文件 
with open('odb-in-keywords.py', "r", encoding="utf-8") as f:
	# readlines以列表的形式将文件读出
	lines = f.readlines()

# 设定循环范围 保存为数字列表
pile_length = [i for i in range(10,13)]
pile_width = [i*0.1 for i in range(5,8)]
soil_E = [i for i in range(15000000,18000000,1000000)]

# 循环改变 以上变量
for p_l in pile_length:
	for p_w in pile_width:
		for s_E in soil_E:
			# 定义change的字典
			r_p1 = round(p_w/2,2)
			r_p2 = round(50-p_l,2)
			r_p3 = round(50/2-p_l)
			r_pl = round(p_l,2)
			r_pw = round(p_w,2)
			r_sE = round(s_E,2)
			re_dict = { 'Re_p1':str(r_p1), 
						'Re_p2':str(r_p2), 
						'Re_p3':str(r_p3),
						'Re_pl':str(r_pl),
						'Re_pw':str(r_pw),
						'Re_sE':str(r_sE),
						'Re_fileName':str(r_pl)+'-'+str(r_pw)+'-'+str(r_sE)}
			# 为保存的文件命名
			file_name = str(r_pl)+'-'+str(r_pw)+'-'+str(r_sE)+'.py'


			with open(file_name, "w", encoding="utf-8") as f_w:
				for line in lines:
					re_line = line
					for v in re_dict:
						re_line = re.sub(v, re_dict[v], re_line)
					f_w.writelines(re_line)

			with open('runPy_NoGUI.bat', "a", encoding="utf-8") as bat_w:
				str_bat = "call abaqus cae noGUI="+file_name+"\n"
				bat_w.write(str_bat)

