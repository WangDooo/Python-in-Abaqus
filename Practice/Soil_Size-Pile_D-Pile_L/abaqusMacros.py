# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro1():
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
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=5.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, 0.5))
    p = mdb.models['Model-1'].Part(name='Part-pile', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-pile']
    p.BaseSolidExtrude(sketch=s, depth=10.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-pile']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=16.9615, 
        farPlane=28.2215, width=10.2067, height=4.27665, cameraPosition=(
        4.44343, -11.072, 24.1865), cameraUpVector=(-0.249635, 0.94468, 
        0.21275), cameraTarget=(-0.175891, -0.261892, 5.43779))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=19.2778, 
        farPlane=26.2338, width=11.6006, height=4.86068, cameraPosition=(
        -9.99569, -18.5793, 13.5308), cameraUpVector=(0.128405, 0.672343, 
        0.729018), cameraTarget=(-0.471253, -0.415458, 5.21982))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=19.8346, 
        farPlane=25.4997, width=11.9356, height=5.00108, cameraPosition=(
        -1.39653, -21.9291, 10.5681), cameraUpVector=(0.0269587, 0.553828, 
        0.832194), cameraTarget=(-0.234548, -0.507668, 5.13827))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.0511, 
        farPlane=28.283, width=42.3373, height=17.7395, viewOffsetX=-0.59723, 
        viewOffsetY=-0.705665)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=15.2873, 
        farPlane=29.3489, width=37.9577, height=15.9044, cameraPosition=(
        0.421199, -19.0288, 16.656), cameraUpVector=(0.0122136, 0.775403, 
        0.631349), cameraTarget=(-0.17934, -0.136406, 5.14818), 
        viewOffsetX=-0.535449, viewOffsetY=-0.632667)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=16.4536, 
        farPlane=28.1827, width=28.1836, height=11.809, viewOffsetX=-0.24604, 
        viewOffsetY=-0.290711)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=15.4993, 
        farPlane=29.8718, width=26.549, height=11.1241, cameraPosition=(
        -1.82724, -12.7435, -13.6858), cameraUpVector=(-0.137452, -0.589679, 
        0.795855), cameraTarget=(-0.279297, -0.670413, 4.79549), 
        viewOffsetX=-0.23177, viewOffsetY=-0.27385)
    p = mdb.models['Model-1'].parts['Part-pile']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#4 ]', ), )
    p.Set(faces=faces, name='Set-pile-b')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.9764, 
        farPlane=25.9871, width=32.505, height=13.6197, cameraPosition=(
        8.17525, -20.8749, 6.72006), cameraUpVector=(0.0678539, 0.444301, 
        0.893304), cameraTarget=(0.0867234, -0.320931, 5.36903), 
        viewOffsetX=-0.283765, viewOffsetY=-0.335286)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=16.4773, 
        farPlane=28.6074, width=28.2242, height=11.826, cameraPosition=(
        5.07978, -18.57, 16.7324), cameraUpVector=(-0.0972957, 0.763332, 
        0.638637), cameraTarget=(-0.027733, -0.183089, 5.52753), 
        viewOffsetX=-0.246394, viewOffsetY=-0.29113)
    p = mdb.models['Model-1'].parts['Part-pile']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#1 ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-pile-l')
    p = mdb.models['Model-1'].parts['Part-pile']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#2 ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-pile-top')
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=60.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.rectangle(point1=(0.0, 0.0), point2=(2.0, 2.0))
    p = mdb.models['Model-1'].Part(name='Part-soil', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-soil']
    p.BaseSolidExtrude(sketch=s1, depth=60.0)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-soil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=103.614, 
        farPlane=163.505, width=53.4969, height=22.4154, cameraPosition=(
        20.9802, -77.2865, 136.363), cameraUpVector=(-0.219884, 0.924993, 
        0.309901), cameraTarget=(-0.197392, -0.370552, 32.5679))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=99.8226, 
        farPlane=167.35, width=51.5394, height=21.5952, cameraPosition=(
        29.4068, -33.4378, 155.918), cameraUpVector=(-0.346178, 0.938077, 
        -0.0131069), cameraTarget=(-0.0303522, 0.498662, 32.9555))
    p = mdb.models['Model-1'].parts['Part-soil']
    f, e = p.faces, p.edges
    t = p.MakeSketchTransform(sketchPlane=f[4], sketchUpEdge=e[7], 
        sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(1.0, 1.0, 
        60.0))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=120.13, gridSpacing=3.0, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Part-soil']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, 0.5))
    p = mdb.models['Model-1'].parts['Part-soil']
    f1, e1 = p.faces, p.edges
    p.CutExtrude(sketchPlane=f1[4], sketchUpEdge=e1[7], sketchPlaneSide=SIDE1, 
        sketchOrientation=RIGHT, sketch=s, depth=10.0, 
        flipExtrudeDirection=OFF)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Part-soil']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    p.Set(cells=cells, name='Set-soil-all')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=99.077, 
        farPlane=168.924, width=51.1545, height=21.4339, cameraPosition=(
        1.80546, 1.29336, 164.008), cameraUpVector=(-0.412055, 0.850646, 
        -0.326514), cameraTarget=(-0.582912, 1.19396, 33.1175))
    p = mdb.models['Model-1'].parts['Part-soil']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#2 ]', ), )
    p.Set(faces=faces, name='Set-soil-b')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=102.25, 
        farPlane=165.093, width=52.793, height=22.1204, cameraPosition=(20.886, 
        -62.767, 145.797), cameraUpVector=(-0.339574, 0.921879, 0.186623), 
        cameraTarget=(-0.14317, -0.282414, 32.6978))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=102.104, 
        farPlane=165.238, width=52.7178, height=22.0889, cameraPosition=(
        20.886, -62.767, 145.797), cameraUpVector=(-0.176078, 0.967511, 
        0.181434), cameraTarget=(-0.14317, -0.282414, 32.6978))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=101.844, 
        farPlane=165.603, width=52.5837, height=22.0328, cameraPosition=(
        16.8415, -61.1001, 147.376), cameraUpVector=(-0.182374, 0.969903, 
        0.161333), cameraTarget=(-0.226656, -0.248006, 32.7304))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=101.349, 
        farPlane=165.831, width=52.3283, height=21.9257, cameraPosition=(
        28.5721, -53.3024, 148.911), cameraUpVector=(-0.234706, 0.964156, 
        0.123762), cameraTarget=(0.0199605, -0.0840716, 32.7627))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=101.432, 
        farPlane=165.26, width=52.3714, height=21.9438, cameraPosition=(
        49.0045, -40.4514, 147.308), cameraUpVector=(-0.372738, 0.922078, 
        0.104102), cameraTarget=(0.429569, 0.173553, 32.7306))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=100.861, 
        farPlane=165.668, width=52.0765, height=21.8202, cameraPosition=(
        54.3855, 24.161, 149.898), cameraUpVector=(-0.626756, 0.744685, 
        -0.229392), cameraTarget=(0.527818, 1.35327, 32.7779))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=100.275, 
        farPlane=166.532, width=51.7738, height=21.6934, cameraPosition=(
        45.0982, -23.5075, 153.506), cameraUpVector=(-0.444397, 0.895637, 
        -0.0186063), cameraTarget=(0.363869, 0.511776, 32.8416))
    p = mdb.models['Model-1'].parts['Part-soil']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#28 ]', ), )
    p.Set(faces=faces, name='Set-soil-y')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=99.9991, 
        farPlane=167.432, width=51.6313, height=21.6337, cameraPosition=(
        18.565, -38.1841, 156.643), cameraUpVector=(-0.320888, 0.947063, 
        -0.0101022), cameraTarget=(-0.131649, 0.237685, 32.9002))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=101.554, 
        farPlane=166.586, width=52.4341, height=21.9701, cameraPosition=(
        -13.9222, -54.8149, 150.992), cameraUpVector=(-0.144436, 0.986924, 
        0.0715476), cameraTarget=(-0.812773, -0.110995, 32.7817))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=101.482, 
        farPlane=166.658, width=52.397, height=21.9545, cameraPosition=(
        -13.9222, -54.8149, 150.992), cameraUpVector=(-0.182289, 0.981116, 
        0.0646621), cameraTarget=(-0.812773, -0.110995, 32.7817))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=102.78, 
        farPlane=166.041, width=53.0671, height=22.2353, cameraPosition=(
        -43.609, -50.5092, 145.867), cameraUpVector=(-0.0287213, 0.998375, 
        0.0492109), cameraTarget=(-1.51195, -0.00958768, 32.661))
    p = mdb.models['Model-1'].parts['Part-soil']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#14 ]', ), )
    p.Set(faces=faces, name='Set-soil-x')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=111.644, 
        farPlane=157.067, width=57.6436, height=24.1529, cameraPosition=(
        -40.2062, -103.314, 103.987), cameraUpVector=(-0.237959, 0.851113, 
        0.467956), cameraTarget=(-1.42338, -1.38395, 31.571))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=100.521, 
        farPlane=168.189, width=189.998, height=79.6096, viewOffsetX=6.40463, 
        viewOffsetY=13.0406)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=100.719, 
        farPlane=144.027, width=190.372, height=79.7667, cameraPosition=(
        -38.4998, -113.888, 14.3757), cameraUpVector=(-0.355771, 0.38544, 
        0.851388), cameraTarget=(1.34116, 10.2643, 26.0727), 
        viewOffsetX=6.41727, viewOffsetY=13.0663)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=65.2984, 
        farPlane=156.896, width=123.423, height=51.7146, cameraPosition=(
        -13.6882, -32.4481, -75.6291), cameraUpVector=(-0.520232, -0.531124, 
        0.668779), cameraTarget=(1.64326, 20.1083, 43.2855), 
        viewOffsetX=4.16046, viewOffsetY=8.47118)
    p = mdb.models['Model-1'].parts['Part-soil']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#80 ]', ), )
    p.Set(faces=faces, name='Set-soil-Bottom')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=89.0238, 
        farPlane=139.251, width=168.267, height=70.5046, cameraPosition=(
        -23.3473, -97.3368, -24.1335), cameraUpVector=(-0.47131, 0.114051, 
        0.874562), cameraTarget=(2.99491, 21.3234, 24.4849), 
        viewOffsetX=5.67212, viewOffsetY=11.5491)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=86.1148, 
        farPlane=146.135, width=162.769, height=68.2007, cameraPosition=(
        1.29721, -108.564, 70.8665), cameraUpVector=(-0.503352, 0.651441, 
        0.567681), cameraTarget=(-1.85881, 7.93968, 11.2446), 
        viewOffsetX=5.48677, viewOffsetY=11.1717)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=73.136, 
        farPlane=163.354, width=138.237, height=57.9219, cameraPosition=(
        13.3155, -33.882, 143.245), cameraUpVector=(-0.628467, 0.766167, 
        -0.134231), cameraTarget=(-0.978942, -11.0977, 15.1269), 
        viewOffsetX=4.65983, viewOffsetY=9.48796)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=85.8781, 
        farPlane=150.611, width=26.9826, height=11.3058, viewOffsetX=9.32986, 
        viewOffsetY=15.5642)
    p = mdb.models['Model-1'].parts['Part-soil']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#1 ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-soil-l')
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    p = mdb.models['Model-1'].parts['Part-soil']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    f = p.faces
    p.PartitionCellByExtendFace(extendFace=f[0], cells=pickedCells)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=82.9051, 
        farPlane=153.584, width=63.5158, height=26.6133, viewOffsetX=17.34, 
        viewOffsetY=18.9438)
    session.viewports['Viewport: 1'].setColor(globalTranslucency=True)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=72.6236, 
        farPlane=163.866, width=174.921, height=73.2926, viewOffsetX=45.2594, 
        viewOffsetY=39.6131)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=72.122, 
        farPlane=164.367, width=173.713, height=72.7864, cameraPosition=(
        30.0121, -34.9174, 141.198), cameraUpVector=(-0.744257, 0.652736, 
        -0.141484), cameraTarget=(15.7177, -12.1331, 13.0799), 
        viewOffsetX=44.9468, viewOffsetY=39.3396)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=87.5089, 
        farPlane=148.981, width=10.8132, height=4.53077, viewOffsetX=2.16617, 
        viewOffsetY=11.555)
    p = mdb.models['Model-1'].parts['Part-soil']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    v1, e, d1 = p.vertices, p.edges, p.datums
    p.PartitionCellByPlaneThreePoints(cells=pickedCells, point1=p.InterestingPoint(
        edge=e[7], rule=MIDDLE), point2=p.InterestingPoint(edge=e[2], 
        rule=CENTER), point3=p.InterestingPoint(edge=e[14], rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=87.2885, 
        farPlane=149.201, width=12.9955, height=5.44515, viewOffsetX=3.58975, 
        viewOffsetY=11.7277)
    p = mdb.models['Model-1'].parts['Part-soil']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#f ]', ), )
    v2, e1, d2 = p.vertices, p.edges, p.datums
    p.PartitionCellByPlaneThreePoints(cells=pickedCells, point1=p.InterestingPoint(
        edge=e1[28], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[22], 
        rule=MIDDLE), point3=p.InterestingPoint(edge=e1[32], rule=MIDDLE))
    p = mdb.models['Model-1'].parts['Part-pile']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['Part-pile']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    v1, e, d1 = p.vertices, p.edges, p.datums
    p.PartitionCellByPlaneThreePoints(point1=v1[0], cells=pickedCells, 
        point2=p.InterestingPoint(edge=e[0], rule=MIDDLE), 
        point3=p.InterestingPoint(edge=e[1], rule=MIDDLE))
    p = mdb.models['Model-1'].parts['Part-pile']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    v2, e1, d2 = p.vertices, p.edges, p.datums
    p.PartitionCellByPlaneThreePoints(cells=pickedCells, point1=p.InterestingPoint(
        edge=e1[7], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[5], 
        rule=MIDDLE), point3=p.InterestingPoint(edge=e1[6], rule=MIDDLE))
    p = mdb.models['Model-1'].parts['Part-pile']
    v = p.vertices
    verts = v.getSequenceFromMask(mask=('[#1 ]', ), )
    p.Set(vertices=verts, name='Set-TopPoint')
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['Model-1'].parts['Part-pile']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    mdb.models['Model-1'].Material(name='Material-pile')
    mdb.models['Model-1'].materials['Material-pile'].Density(table=((2.5, ), ))
    mdb.models['Model-1'].materials['Material-pile'].Elastic(table=((34500000.0, 
        0.2), ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-pile', 
        material='Material-pile', thickness=None)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=16.3036, 
        farPlane=27.2126, width=26.5569, height=11.1274, viewOffsetX=0.417103, 
        viewOffsetY=0.907245)
    p = mdb.models['Model-1'].parts['Part-pile']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#f ]', ), )
    region = p.Set(cells=cells, name='Set-pile')
    p = mdb.models['Model-1'].parts['Part-pile']
    p.SectionAssignment(region=region, sectionName='Section-pile', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].Material(name='Material-soil')
    mdb.models['Model-1'].materials['Material-soil'].Depvar(n=4)
    mdb.models['Model-1'].materials['Material-soil'].UserMaterial(
        mechanicalConstants=(100.0, 0.0, 0.3, 3.14))
    p = mdb.models['Model-1'].parts['Part-soil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-soil', 
        material='Material-soil', thickness=None)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=88.2443, 
        farPlane=155.368, width=43.7382, height=18.3265, viewOffsetX=3.27777, 
        viewOffsetY=1.15015)
    p = mdb.models['Model-1'].parts['Part-soil']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#ff ]', ), )
    region = p.Set(cells=cells, name='Set-soil')
    p = mdb.models['Model-1'].parts['Part-soil']
    p.SectionAssignment(region=region, sectionName='Section-soil', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Part-pile']
    a.Instance(name='Part-pile-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['Part-soil']
    a.Instance(name='Part-soil-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=105.497, 
        farPlane=160.088, width=55.6284, height=23.3085, cameraPosition=(
        75.8125, -58.5371, 122.15), cameraUpVector=(-0.534271, 0.724656, 
        0.435233))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=105.137, 
        farPlane=161.18, width=55.4387, height=23.229, cameraPosition=(59.5778, 
        -69.6459, 126.55), cameraUpVector=(-0.409367, 0.820594, 0.398803), 
        cameraTarget=(-0.637403, -0.788456, 32.6336))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=106.128, 
        farPlane=160.189, width=48.1081, height=20.1575, viewOffsetX=6.63897, 
        viewOffsetY=-9.71649)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=101.643, 
        farPlane=161.481, width=46.0749, height=19.3055, cameraPosition=(
        68.7283, -30.2109, 138.36), cameraUpVector=(-0.635762, 0.742168, 
        0.212118), cameraTarget=(-1.77033, -1.23416, 31.6931), 
        viewOffsetX=6.35838, viewOffsetY=-9.30584)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=101.283, 
        farPlane=160.004, width=45.9115, height=19.2371, cameraPosition=(
        75.2213, 5.52624, 137.374), cameraUpVector=(-0.833507, 0.531854, 
        0.149656), cameraTarget=(-2.01925, -3.66262, 31.8424), 
        viewOffsetX=6.33583, viewOffsetY=-9.27284)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=101.305, 
        farPlane=159.982, width=45.9214, height=19.2412, cameraPosition=(
        76.9361, -1.83026, 136.759), cameraUpVector=(-0.957201, 0.0725585, 
        0.280182), cameraTarget=(-0.304395, -11.0191, 31.2278), 
        viewOffsetX=6.33719, viewOffsetY=-9.27483)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=100.786, 
        farPlane=161.362, width=45.686, height=19.1426, cameraPosition=(
        54.4177, -54.5701, 136.613), cameraUpVector=(-0.94326, 0.262722, 
        0.20307), cameraTarget=(-2.86292, -9.6225, 27.5896), 
        viewOffsetX=6.30471, viewOffsetY=-9.22729)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=103.965, 
        farPlane=158.54, width=47.1271, height=19.7464, cameraPosition=(
        24.9439, -89.8873, 122.174), cameraUpVector=(-0.777734, 0.562465, 
        0.280649), cameraTarget=(-4.29667, -4.97091, 26.6666), 
        viewOffsetX=6.50358, viewOffsetY=-9.51834)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=106.568, 
        farPlane=155.043, width=48.3072, height=20.2409, cameraPosition=(
        -0.165675, -103.481, 109.235), cameraUpVector=(-0.567316, 0.722734, 
        0.394724), cameraTarget=(-3.93383, -1.21815, 27.2871), 
        viewOffsetX=6.66643, viewOffsetY=-9.75668)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=109.751, 
        farPlane=151.859, width=14.4329, height=6.04743, viewOffsetX=-3.07047, 
        viewOffsetY=-12.982)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=119.037, 
        farPlane=150.355, width=15.6539, height=6.55905, cameraPosition=(
        -5.19815, -121.364, 86.7027), cameraUpVector=(-0.500479, 0.655919, 
        0.565059), cameraTarget=(-2.93699, -3.53633, 29.2676), 
        viewOffsetX=-3.33024, viewOffsetY=-14.0803)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=137.896, 
        farPlane=146.044, width=18.134, height=7.59821, cameraPosition=(
        4.31427, -141.08, 35.611), cameraUpVector=(-0.420489, 0.353311, 
        0.835679), cameraTarget=(-0.846074, -10.2023, 29.9739), 
        viewOffsetX=-3.85786, viewOffsetY=-16.3111)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=137.184, 
        farPlane=146.757, width=21.7718, height=9.12247, viewOffsetX=-8.63693, 
        viewOffsetY=-26.18)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=113.059, 
        farPlane=146.786, width=17.9431, height=7.51821, cameraPosition=(
        1.43195, -113.85, 91.2507), cameraUpVector=(-0.363991, 0.690839, 
        0.624701), cameraTarget=(0.344859, 2.84714, 31.5182), 
        viewOffsetX=-7.11806, viewOffsetY=-21.576)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=106.711, 
        farPlane=153.133, width=93.3886, height=39.1302, viewOffsetX=4.74072, 
        viewOffsetY=-2.35916)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=93.2612, 
        farPlane=169.229, width=81.618, height=34.1982, cameraPosition=(
        0.384949, -34.7688, 156.355), cameraUpVector=(-0.40985, 0.908522, 
        -0.081305), cameraTarget=(0.339336, 2.05013, 30.5309), 
        viewOffsetX=4.14321, viewOffsetY=-2.06181)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=100.709, 
        farPlane=161.78, width=13.7718, height=5.77042, viewOffsetX=4.21561, 
        viewOffsetY=4.91784)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=101.415, 
        farPlane=163.8, width=13.8683, height=5.81088, cameraPosition=(1.45734, 
        -16.844, 161.443), cameraUpVector=(-0.385265, 0.900275, -0.202671), 
        cameraTarget=(0.0755022, 1.89622, 31.6957), viewOffsetX=4.24518, 
        viewOffsetY=4.95232)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=97.6215, 
        farPlane=167.595, width=65.0848, height=27.2707, viewOffsetX=9.91841, 
        viewOffsetY=6.74454)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=96.6076, 
        farPlane=168.609, width=64.4088, height=26.9875, cameraPosition=(
        0.692304, -16.3438, 161.523), cameraUpVector=(-0.336132, 0.920268, 
        -0.200307), cameraTarget=(-0.689532, 2.39647, 31.7761), 
        viewOffsetX=9.8154, viewOffsetY=6.67449)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=98.2292, 
        farPlane=170.533, width=65.49, height=27.4405, cameraPosition=(
        -0.0979452, -0.574835, 164.397), cameraUpVector=(-0.317242, 0.896474, 
        -0.309342), cameraTarget=(-0.958506, 2.64329, 33.3391), 
        viewOffsetX=9.98016, viewOffsetY=6.78653)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=102.92, 
        farPlane=165.85, width=16.1421, height=6.76361, viewOffsetX=2.76301, 
        viewOffsetY=-0.628234)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=102.782, 
        farPlane=165.679, width=16.1206, height=6.75457, cameraPosition=(
        4.26577, -13.4713, 163.436), cameraUpVector=(-0.289464, 0.933825, 
        -0.210193), cameraTarget=(-0.863966, 2.46759, 33.4097), 
        viewOffsetX=2.75931, viewOffsetY=-0.627395)
    a = mdb.models['Model-1'].rootAssembly
    a.translate(instanceList=('Part-pile-1', ), vector=(1.0, 1.0, 50.0))
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].StaticStep(name='Step-dym', previous='Initial', 
        timePeriod=5.0, maxNumInc=1000, timeIncrementationMethod=FIXED, 
        initialInc=0.02, noStop=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-dym')
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
        'U', ))
    mdb.models['Model-1'].historyOutputRequests['H-Output-1'].suppress()
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
        constraints=ON, connectors=ON, engineeringFeatures=ON, 
        adaptiveMeshConstraints=OFF)
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['Part-pile-1'].sets['Set-pile-b']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['Part-soil-1'].sets['Set-soil-b']
    mdb.models['Model-1'].Tie(name='Constraint-1', master=region1, slave=region2, 
        positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
        thickness=ON)
    mdb.models['Model-1'].ContactProperty('IntProp-p-s')
    mdb.models['Model-1'].interactionProperties['IntProp-p-s'].TangentialBehavior(
        formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
        pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
        table=((0.4, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
        fraction=0.005, elasticSlipStiffness=None)
    mdb.models['Model-1'].interactionProperties['IntProp-p-s'].NormalBehavior(
        pressureOverclosure=HARD, allowSeparation=ON, 
        constraintEnforcementMethod=DEFAULT)
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['Part-pile-1'].surfaces['Surf-pile-l']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['Part-soil-1'].surfaces['Surf-soil-l']
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-1', 
        createStepName='Step-dym', master=region1, slave=region2, 
        sliding=FINITE, thickness=ON, interactionProperty='IntProp-p-s', 
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, interactions=OFF, constraints=OFF, 
        engineeringFeatures=OFF)
    mdb.models['Model-1'].PeriodicAmplitude(name='Amp-1', timeSpan=STEP, 
        frequency=3.14, start=0.0, a_0=0.0, data=((0.0, 1.0), ))
    e1 = a.instances['Part-soil-1'].edges
    v11 = a.instances['Part-soil-1'].vertices
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['Part-pile-1'].surfaces['Surf-pile-top']
    mdb.models['Model-1'].SurfaceTraction(name='Load-1', createStepName='Step-dym', 
        region=region, magnitude=2000.0, amplitude='Amp-1', directionVector=(
        a.instances['Part-soil-1'].InterestingPoint(edge=e1[15], rule=CENTER), 
        v11[2]), distributionType=UNIFORM, field='', localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['Part-soil-1'].sets['Set-soil-Bottom']
    mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Step-dym', 
        region=region, u1=0.0, u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['Part-soil-1'].sets['Set-soil-x']
    mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Step-dym', 
        region=region, u1=0.0, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, 
        ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
        fieldName='', localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['Part-soil-1'].sets['Set-soil-y']
    mdb.models['Model-1'].DisplacementBC(name='BC-3', createStepName='Step-dym', 
        region=region, u1=UNSET, u2=0.0, u3=UNSET, ur1=UNSET, ur2=UNSET, 
        ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
        fieldName='', localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
        bcs=OFF, predefinedFields=OFF, connectors=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Part-soil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Part-pile']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, 
        secondOrderAccuracy=OFF, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['Part-pile']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#f ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    p = mdb.models['Model-1'].parts['Part-pile']
    p.seedPart(size=0.5, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Part-pile']
    p.generateMesh()
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.regenerate()
    p = mdb.models['Model-1'].parts['Part-pile']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['Part-soil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=88.456, 
        farPlane=155.156, width=41.2691, height=17.3388, viewOffsetX=1.91011, 
        viewOffsetY=-0.393541)
    elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, 
        secondOrderAccuracy=OFF, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['Part-soil']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#ff ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    p = mdb.models['Model-1'].parts['Part-soil']
    p.seedPart(size=0.5, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Part-soil']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=90.0622, 
        farPlane=153.55, width=23.4102, height=9.83558, viewOffsetX=1.6736, 
        viewOffsetY=1.5526)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.regenerate()
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    import job
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(71, """
    ** ----------------------------------------------------------------
    **
    ** STEP: Step-dym
    **
    *Initial conditions, type=solution
    Part-soil-1.Set-soil-all, 100, 1.0, 0.1, 0""")
    mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=20, 
        numDomains=20, numGPUs=0)
    mdb.jobs['Job-1'].writeInput(consistencyChecking=OFF)
    mdb.saveAs(pathName='C:/Users/123/Desktop/abaqus model size/macro/1')


