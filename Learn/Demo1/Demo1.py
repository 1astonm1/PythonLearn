# -*- coding:utf-8 -*-



class Person:
    def __init__(self, name, age, num):
        self.name = name
        self.age = age
        self.num = num

    def run(self):
        print("running fast")

    def eat(self):
        print("have dinner")

    def getname(self):
        return self.name
    def setname(self, name):
        self.name = name
    def getage(self):
        return self.age
    def setage(self, age):
        self.age = age



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

    def getname(self):
        return self.name
    def setname(self, name):
        self.name = name
    def getage(self):
        return self.age
    def setage(self, age):
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
    stu = Student("a",10,1)
    tea = Teacher("b",30,2)
    stu.run()
    stu.eat()
    stu.homework()
    tea.eat()
    tea.run()
    tea.perpclass()
    temp = tea.getname()
    print(temp)

