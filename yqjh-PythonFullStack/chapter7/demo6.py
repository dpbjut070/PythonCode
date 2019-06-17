data = {}
data['d']={}
data['name']=[]
print('请输入字典数据，key和value之间用逗号分隔')
dictStr = input(':')
list = dictStr.split(',')
keys=[]
values=[]
for i in range(len(list)):
    if i % 2 == 0:
        keys.append(list[i])
    else:
        values.append(list[i])
data['d'].update(dict(zip(keys,values)))

print('请输入姓名，多个姓名之间用逗号分隔')
nameStr = input(':')
names = nameStr.split(',')
data['name'].extend(names)
print(data)

def init(data):
    data['d']={}
    data['name']=[]

