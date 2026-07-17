#练习1
a = int(input('输入一个数字：'))
if a % 2 == 0:
    print('偶数')
else:
    print('奇数')

#练习2
age = int (input('年龄：'))
if age < 12:
    print('儿童')
elif age < 18:
    print('青少年')
elif age < 60:
    print('成年人')
else:
    print('老年人')

#练习3
a = int(input('公里数：'))
b = 10 + (a-3)*2
if a <= 3:
    print('10元')
else:
    print(f'{b}元')

#练习4
name = "python"
key = 123
a = input('用户名：')
b = int(input('密码：'))
if a == name and b == key:
    print('登录成功')
elif a != name and b == key:
    print('用户名不存在')
else:
    print('密码错误')


