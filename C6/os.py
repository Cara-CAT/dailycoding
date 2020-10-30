import os

print(os.name)#获取系统平台
#输出 nt 代表Windows系统
print(os.sep)#获取当前系统平台的路径分隔符\
print(os.getcwd())#获取当前工作目录
print(os.getcwd()+os.sep+'data'+os.sep+'test.dat')
