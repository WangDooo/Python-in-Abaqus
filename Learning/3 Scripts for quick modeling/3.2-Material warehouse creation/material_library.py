# coding:UTF8
from abaqus import *
from abaqusConstants import *

def add_SI_Materials():
    """
    Add Steel, Copper, Aluminum in SI units
    """
    
    import material
    
    name = getInput('Enter model name', mdb.models.keys()[-1]) # 模型名指模型库的最后一个模型名
    if not name in mdb.models.keys():
        raise ValueError,'mdb.models[%s] not found' %repr(name)

    m = mdb.models[name].Material('Steel')
    m.Elastic(table=((200000000000.0, 0.3), ))
    m.Density(table=((7800.0, ), ))
    m.Plastic(table=((400000000.0, 0.0), (400000000.0, 0.0), (420000000.0, 0.02), (500000000.0, 0.2), (600000000.0, 0.5)))
    
    m = mdb.models[name].Material('Copper')
    m.Density(table=((8970.0, ), ))
    m.Elastic(table=((110000000000.0, 0.3), ))
    m.Plastic(table=((314000000.0, 0.0), ))
    
    m = mdb.models[name].Material('Aluminum')
    m.Density(table=((2700.0, ), ))
    m.Elastic(table=((70000000000.0, 0.35), ))
    m.Plastic(temperatureDependency=ON, table=((270000000.0, 0.0, 0.0), (300000000.0, 1.0, 0.0), (243000000.0, 0.0, 300.0), (270000000.0, 1.0, 300.0)))


add_SI_Materials()