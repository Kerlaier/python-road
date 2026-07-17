# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
"""
============================================================
  第5课练习 —— 循环
============================================================
"""

print("=" * 40)
print("  第5课练习")
print("=" * 40)

# ========== 练习1：数到100 ==========
# 用 for 循环和 range() 打出 1 到 100 中所有能被 7 整除的数字
# 提示：range(1, 101)，配合 if 判断
for num in range(1,101):
    if num % 7 == 0:
        print(num)


# ========== 练习2：累加求和 ==========
# 用 for 循环计算 1+2+3+...+100 的总和
# 提示：sum = 0，每次循环 sum = sum + 当前数
sum =0
for num in range(1,101): 
    sum =sum+num
print(sum)


# ========== 练习3：猜数字 ==========
# 把讲义里的猜数字游戏改成真正用 input() 的版本
# 预设目标数字 target = 66，让用户猜，每次提示"大了""小了"
# 猜对后打印猜了几次，用 break 结束
target = 66
attempts = 0

while True:
    number = int(input("让我们猜数字，请输入一个数字："))
    attempts = attempts + 1
    if number < target:
       print('小了')
    elif number > target:
       print('大了')
    else:
        print('对了')
        print(f'你猜了{attempts}次')
        break
  



# ========== 练习4（选做）：打印九九乘法表 ==========
# 两层循环嵌套，输出完整的乘法口诀表
# 提示：for i in range(1, 10):
#           for j in range(1, i+1):
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}",end="\t")
    print()