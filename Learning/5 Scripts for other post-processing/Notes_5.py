------------------------------------------
第四章 编写脚本进行其他后处理
两种情况需要进行后处理
(1) 读入外部数据文件来绘制X-Y图
(2) 将其他软件的分析结果写入到ODB文件，并在Visualization模块中进行后处理
------------------------------------------
5.1 自动后处理
------------------------------------------
5.1.1
导入odbAccess模块可以访问输出数据库
导入Visualization模块可以实现各种后处理
1. 可视化命令
(1) 在视口中显示odb
odb = session.openOdb('new_viewer_tutorial.odb')
vp = session.viewports['Viewport: 1']
vp.setValues(displayedObject=odb)
(2) 绘制Mises应力S的变形云图
# vp.odbDisplay中包含输出数据库的显示设置信息
od = vp.odbDisplay
od.setPrimaryVariable(variableLabel='S', outputPosition=INTEGRATION_POINT)
od.display.setValues(plotState=(CONTOURS_ON_DEF,))
2. 注释命令
(1) 设置图注命令
vp.plotAnnotation(mdb.Text(name='autoprocessing example', offset=(70,110), text='example Run#618'))
(2) 输出命令
File菜单下的Print
session.pngOptions.setValues(imageSize=(3750,2000))
session.printOptions.setValues(rendition=COLOR, vpDecorations=OFF, vpBackground=OFF)
session.printToFile(fileName='stress', format=PNG, canvasObjects=(vp,))

5.1.2 实例
1. 获取odb中最后一帧的Mises应力图，并将其保存为PNG格式文件【很丑，用不上】
autopostprocessing.py

------------------------------------------
5.2 外部数据的后处理 【没什么用，反倒麻烦】
------------------------------------------

------------------------------------------
