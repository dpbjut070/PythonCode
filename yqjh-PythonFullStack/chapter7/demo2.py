def fibs(n):
    result = [0,1]
    for i in range(int(n)):
        result.append(result[-1]+result[-2])
    return result

while True:
    n = input("请输入一个整数:")
    if n == 'exit':
        break
    print(fibs(n))