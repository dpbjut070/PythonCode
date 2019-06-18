#列表方法
'''
    1.append:拼接
    2.clear:清空列表
    3.copy:复制
    4.count:统计元素的个数
    5.extend:两个列表的拼接
    6.index:用于从列表中找出某个值第一次出现的位置
    7.insert:插入
    8.pop:移除列表的最后一个元素，并返回移除后的列表
    9.remove:移除某个值第一次匹配项
    10.reverse:用于列表的反向存放
    11.sort:列表的排序改变原列表
'''

#append
numbers = [1,2,3,4,5,6]
numbers.append(20)
print(numbers)
#clear
#深拷贝
numbers1 = numbers.copy()
numbers2 = numbers[:]
#浅拷贝
numbers3 = numbers
numbers.clear()
print(numbers,numbers1,numbers2,numbers3)

#count;未找到返回0

search = ['jjj','he','kkk','mmm','he','eee','he','he',[1,2,3]]

print(search.count('he'))
print(search.count([1,2,3]))

#extend
a = [1,2,3]
b = [4,5,6]

a.extend(b)

print(a)

#index

x = [1,3,4,3,5,3]

print(x.index(3))
# print(x.index(6))

#insert

r = [1,2,3,4,5,6]
r.insert(3,'kkk')
# r[3:3]='kkk'
print(r)

#pop
p = [1,2,3]

# print(p.pop())
print(p.pop(1))

#remove

m = [1,2,3,2,4]

m.remove(2)

print(m)

#reverse

s = [1,2,3,4,5]

s.reverse()

print(s)

s.reverse()

print(s)

#sort:改变原来的列表

t = [1,4,6,2,11,22,33,88,21]
t1 = t.copy()
t1.sort()

print(t,t1)

#sorted:不改变原来的列表

d = [3,2,66,22,33,21,42,21]

d1 = sorted(d)

print(d,d1)