# -*- coding:UTF-8 -*-

# 创建Section对象
mySection = mdb.models['Model-1'].HomogeneousSolidSection(name='solidSteel', material='Steel', thickness=1.0)
# 使用type()函数来显示对象的类型
print('Section type = ', type(mySection))
# 列出对象的所有成员
print('Members of the section are: ', mySection.__members__)
# 列出对象的所有方法
print('Methods of the section are: ', mySection.__methods__)
# 输出每个成员的值
for member in mySection.__members__:
	print('mySection.%s = %s'  % (member, getattr(mySection,member)))