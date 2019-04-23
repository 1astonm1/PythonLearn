# -*- coding:utf-8 -*-
class Person:
    classname = "Person"   # 定义类内部变量

    def __init__(self, name, age, num):
        self.name = name
        self.age = age
        self.num = num

    def run(self):
        print("running fast")

    def eat(self):
        print("have dinner")

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def out_put_classname(self):
        print(self.classname)   # 使用内部变量进行输出


class Student(Person):
    def __init__(self, name, age, num):
        self.name = name
        self.age = age
        self.num = num

    def run(self):
        print("Student running fast")

    def eat(self):
        print("Student have dinner")

    def homework(self):
        print("doing homework")

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


class Teacher(Person):
    def __init__(self, name, age, num):
        self.name = name
        self.age = age
        self.num = num

    def run(self):
        print("Teacher running fast")

    def eat(self):
        print("Teacher have dinner")

    def perpclass(self):
        print("have class")

    def getname(self):
        return self.name

    def setname(self, name):
        self.name = name

    def getage(self):
        return self.age

    def setage(self, age):
        self.age = age


if __name__ == '__main__':
    stu = Student("a", 10, 1)
    tea = Teacher("b", 30, 2)
    stu.run()
    stu.eat()
    stu.homework()
    tea.eat()
    tea.run()
    tea.perpclass()
    temp = tea.getage()
    print(temp)
    temp = tea.getname()
    print(temp)

