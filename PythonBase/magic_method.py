
class Car:

    # 内部变量
    name = ""
    color = ""

    # 用传入的参数来初始化实例
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # 析构函数 ！！！！一旦定义后在该实例所有任务执行完毕后会自行调用
    def __del__(self):
        print("i am dying")

    # 定义输出的格式
    def __repr__(self):
        return "name:"+self.name+" color:"+self.color

    #
    def __getattr__(self, name):
        return self.name


if __name__ == '__main__':
    car = Car("bmw", "black")   # 调用__init__方法
    print("color:"+car.color)
    print(car)  # 利用__perp__输出


