import os

path_base = os.getcwd()  # 查看当前工作路径
print(path_base)

os.mkdir(path=path_base+"/name")  # 创建文件夹   在windows上可省略第二个创建参数
print(os.listdir(path_base))     # 显示当前路径下所有的文件夹
os.rename(path_base+"/name", path_base+"/hello")      # 更改文件夹命名
os.chdir(path=path_base+'/hello')    # 更换当前文件夹（类似于 cd c:/aaa）

path = os.getcwd()
print(path)
os.chdir(path_base)  # 换回主目录

os.rmdir(path=path_base+"/hello")   # 删除文件夹

os.system("c:")     # 执行系统指令

print(os.cpu_count())   # 输出cpu信息
print(os.getlogin())    # 输出登录信息

