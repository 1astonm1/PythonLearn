
name = "astonm"
age = 22
number = "20145850"
outputfloat = 1.1254

 #  方法1：直接用逗号分隔
print("name:", name,", age:", age, ", number:",number,", outputf:",outputfloat)


#   方法2：用.format函数
print("name: {0} , age: {1} , number: {2} , outputf: {3} ".format(name, age, number, outputfloat))

#   方法3：用%（已过时）
print("age:%d"%age)
print("name:%s,age: %%d"%name, age)