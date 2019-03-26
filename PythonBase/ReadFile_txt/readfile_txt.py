
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


if __name__ == '__main__':
    read_by_line_method1()
    read_by_line_method2()
    read_by_line_method3()
