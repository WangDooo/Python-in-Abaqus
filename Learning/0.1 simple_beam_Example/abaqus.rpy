# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2017 replay file
# Internal Version: 2016_09_28-05.54.59 126836
# Run by WangDoo on Sun Mar 10 21:03:23 2019
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=267.826568603516, 
    height=74.3351821899414)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o2 = session.openOdb(name='beam_job.odb')
#: Model: D:/Coding/Github/Python-in-Abaqus/Learning/0.1 simple_beam_Example/beam_job.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       1
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
execfile(
    'D:/Coding/Github/Python-in-Abaqus/Learning/2 Abaqus script interface/2.1-rotateview/rotateview.py', 
    __main__.__dict__)
execfile(
    'D:/Coding/Github/Python-in-Abaqus/Learning/2 Abaqus script interface/2.1-rotateview/rotateview.py', 
    __main__.__dict__)
execfile(
    'D:/Coding/Github/Python-in-Abaqus/Learning/2 Abaqus script interface/2.1-rotateview/rotateview.py', 
    __main__.__dict__)
