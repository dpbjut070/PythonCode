line = input("请输入行数(必须是奇数)")
line = int(line)

if line % 2 != 0:
    spaceNum = line //2
    i = 1
else:
    print("输入行数必须为奇数！！")