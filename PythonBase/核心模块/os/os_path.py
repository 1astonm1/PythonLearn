import os

path = os.getcwd()
os.mkdir(path=path+"/test")

os.path.exists(path)    # 判断当前path对应文件或者目录是否存在，返回Tru或者False
os.path.isfile(path)    # 判断path是否是已经存在的文件
os.path.isdir(path)     # 判断path是否是已经存在的目录
os.path.getatime(path)  # 返回path对应文件或目录上一次的访问时间

os.path.getmtime(path)  # 返回path对应文件或目录上一次的修改时间
os.path.getctime(path)  # 返回path对应文件或目录的创建时间

os.path.getsize(path)   # 返回path对应文件的大小，以字节为单位

# 批量处理文件：
os.path.split(path)  # 把路径分割成 dirname 和 basename，返回一个元组
os.path.splitdrive(path)  # 一般用在 windows 下，返回驱动器名和路径组成的元组
os.path.splitext(path)  # 分割路径，返回路径名和扩展名




