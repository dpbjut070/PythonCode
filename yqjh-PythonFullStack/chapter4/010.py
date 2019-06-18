'''
练习题
'''
#第一题
numbers = []

while True:
    numStr = input('请输入一个整数')
    if numStr == ":exit":
        break
    num = int(numStr)
    numbers.append(num)
numbers.sort(reverse=True)
print(numbers)