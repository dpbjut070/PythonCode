#第四题
'''

'''

n = input("请输出一个大于1的数字:")
assert int(n) > 1
n = int(n)
m = n**2

a = []

b = []

for i in range(1,m+1):
    b.append(i)
for i in range(0,m,n):
    a.append(b[i:i+n])
print(a)

for i in range(n):
    for j in range(i):
        a[i][j],a[j][i] = a[j][i],a[i][j]

for number in a:
    print(number)
