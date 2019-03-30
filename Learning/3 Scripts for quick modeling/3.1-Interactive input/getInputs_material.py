# coding: UTF-8
from abaqus import *

fields = (('E:','2.08E11'),('u:','0.3'),('Density:','7800')) # 3个元组中的元素均为字符串类型
E,u,den = getInputs(fields=fields, label='Define Material Property')
E = float(E)
print(E)
u = float(u)
print(u)
den = float(den)
print(den)