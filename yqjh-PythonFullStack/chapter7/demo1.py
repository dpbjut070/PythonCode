fibs = [0,1]
for i in range(10):
    fibs.append(fibs[-1]+fibs[-2])
print(fibs)

n = input("请输入一个整数:")
for i in range(int(n)):
    fibs.append(fibs[-1]+fibs[-2])
print(fibs)