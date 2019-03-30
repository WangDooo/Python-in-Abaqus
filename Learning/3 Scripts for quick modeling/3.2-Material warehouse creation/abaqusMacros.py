# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def add_SI_Materials():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='Steel')
    mdb.models['Model-1'].materials['Steel'].Density(table=((7800.0, ), ))
    mdb.models['Model-1'].materials['Steel'].Elastic(table=((200000000000.0, 0.3), 
        ))
    mdb.models['Model-1'].materials['Steel'].Plastic(table=((400000000.0, 0.0), 
        ))
    mdb.models['Model-1'].materials['Steel'].plastic.setValues(table=((400000000.0, 
        0.0), (420000000.0, 0.02), (500000000.0, 0.2), (600000000.0, 0.5)))
    mdb.models['Model-1'].Material(name='Copper')
    mdb.models['Model-1'].materials['Copper'].Density(table=((8970.0, ), ))
    mdb.models['Model-1'].materials['Copper'].Elastic(table=((110000000000.0, 0.3), 
        ))
    mdb.models['Model-1'].materials['Copper'].Plastic(table=((314000000.0, 
        0.0), ))
    mdb.models['Model-1'].Material(name='Aluminum')
    mdb.models['Model-1'].materials['Aluminum'].Density(table=((2700.0, ), ))
    mdb.models['Model-1'].materials['Aluminum'].Elastic(table=((70000000000.0, 
        0.35), ))
    mdb.models['Model-1'].materials['Aluminum'].Plastic(temperatureDependency=ON, 
        table=((270000000.0, 0.0, 0.0), (300000000.0, 1.0, 0.0), (243000000.0, 
        0.0, 300.0), (270000000.0, 1.0, 300.0)))


