
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 切片操作左闭右开

result = arr[7:10]  # 取出7~10位 ['8', '9', '10']
result = arr[-3:-1]    # 取出倒数第三位到倒数第1位 ['8', '9']
result = arr[-3:]  # 如果想包含到最后一位，直接省略后面一个就行，最前面同理。['8', '9', '10']
result = arr[:]    # 两边都省略就是包含全部的list内容

# 控制切片步长
result = arr[1:6:2]  # 1~6位每两位取出一个['2', '4', '6']
result = arr[::4]   # list所有内容中每4位取出一个 [1, 5, 9]

print(result)
