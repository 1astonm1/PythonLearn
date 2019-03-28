import numpy as np

##################################################################
# 读取txt文件
##################################################################
def read_simple():  # 简单读取，直接写入字符串
    file = open("test.txt", "r")    # 设置文件对象
    mystr = file.read()     # 将读出内容写入字符串
    file.close()    # 关闭文件
    print(mystr)


def read_by_line_method1():
    mystr = []
    f = open("test.txt", "r")  # 设置文件对象
    line = f.readline()
    line = line[:-1]  # 去掉换行符，也可以不去
    while line:  # 直到读取完文件
        mystr.append(line)     # 写入
        line = f.readline()  # 读取一行文件，包括换行符
        line = line[:-1]  # 去掉换行符，也可以不去

    f.close()  # 关闭文件
    print(mystr)


def read_by_line_method2():
    data = []                   # open可以直接用来测试是否完成
    for line in open("test.txt", "r"):  # 设置文件对象并读取每一行文件
        data.append(line)  # 将每一行文件加入到list中
    print(data)


def read_by_line_method3():
    f = open("test.txt", "r")  # 设置文件对象
    data = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
    f.close()  # 关闭文件
    print(data)


def read_by_numpy():
    data = np.loadtxt("test.txt")
##########################################################################
# 写入txt文件
##########################################################################


def write_simple():  # 简单写入
    mystr = "hello world!"
    with open("test.txt", "w") as f:    # 设置文件对象
        f.write(mystr)      # 写入


def write_by_list_method1():    # 第一种方法，每一项用空格隔开，一个列表是一行写入文件
    data = [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
    with open("test.txt", "w") as f:
        for i in data:
            i = str(i).strip('[').strip(']').replace(',', '').replace('\'', '')+'\n'
            f.write(i)  # 将其中每一个列表规范化成字符
# ['a b c', 'a b c', 'a b c']


def write_by_list_method2():     # 第二种方法，直接将每一项都写入文件
    data = [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
    with open("test.txt", "w") as f:
        for i in data:
            f.writelines(i)  # 直接写入
# ['abcabcab']
# 注意： write 只能写字符！ 而writelines可以写字符串！
#       写入会直接抹掉之前的内容


if __name__ == '__main__':
    write_by_list_method1()
    read_by_line_method1()
