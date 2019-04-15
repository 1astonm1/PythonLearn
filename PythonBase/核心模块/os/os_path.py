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


