------------------------------------------
第六章 脚本的高级处理功能
------------------------------------------

------------------------------------------
6.1 监控分析作业Job 【用不上】
------------------------------------------
分析过程中场变量达到某个值就中止分析
在monitorManager对象中写回调函数
------------------------------------------

------------------------------------------
6.2 优化分析Optimization 【也没用过这个功能，是做设计优化用的，暂时用不到】
------------------------------------------

------------------------------------------
6.3 调试脚本 【讲调试方法的，太low】
------------------------------------------

------------------------------------------
6.4 查询数据
------------------------------------------
1. 查询专有属性
odb.__members__
odb.__methods__
2. 使用print
prettyPrint() 属于textRepr模块
from textRepr import * 
textRepr模块中包括
(1) getPaths()		返回所有子对象的路径
(2) getTypes()		返回所有对象的类型
(3) printPaths()	输出对象及其成员的路径
(4) printTypes()	输出对象中所有成员的类型
------------------------------------------
