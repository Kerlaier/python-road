# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("=" * 40)
print("  第4课练习")
print("=" * 40)

# ========== 练习1：判断奇偶 ==========

num = int(input("请输入一个数字："))
if num % 2 == 0:
    print("偶数")
else:
    print("奇数")


# ========== 练习2：年龄分类 ==========

age = int(input("请输入年龄："))
if age < 12:
    print("儿童")
elif age < 18:
    print("青少年")
elif age < 60:
    print("成年人")
else:
    print("老年人")


# ========== 练习3：计价器 ==========

km = float(input("请输入公里数："))
if km <= 3:
    price = 10
else:
    price = 10 + (km - 3) * 2
print(f"应付{price}元")


# ========== 练习4（选做）：简易登录 ==========

username = input("请输入用户名：")
password = int(input("请输入密码："))
if username == "python" and password == 123:
    print("登录成功")
elif username != "python":
    print("用户名不存在")
else:
    print("密码错误")
