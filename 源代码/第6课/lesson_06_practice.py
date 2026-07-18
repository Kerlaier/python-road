# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import random
"""
============================================================
  第6课练习 —— 列表
============================================================
"""

print("=" * 40)
print("  第6课练习")
print("=" * 40)

# ========== 练习1：创建和管理购物清单 ==========
# 创建一个空列表 shopping = []
# 依次用 append 加入：鸡蛋、牛奶、面包、苹果
# 用 remove 删掉面包
# 最后打印清单
shopping = []
shopping.append("鸡蛋")
shopping.append("牛奶")
shopping.append("面包")
shopping.append("苹果")
shopping.remove("面包")
print("购物清单：", shopping)


# ========== 练习2：成绩分析 ==========
# 有一个成绩列表：[68, 85, 92, 77, 59, 90]
# 1. 打印总人数 len()
# 2. 用 sort 排序后打印最高分和最低分
# 3. 用 for 循环统计及格人数（>=60）
scores = [68, 85, 92, 77, 59, 90]
print("总人数：", len(scores))
scores.sort()
print("最高分：", scores[-1])
print("最低分：", scores[0])
passing_students = 0
for score in scores:
    if score >= 60:
        passing_students = passing_students + 1
print("及格人数：", passing_students)


# ========== 练习3：猜词游戏 ==========
# 有一个词库列表：["python", "apple", "banana", "orange", "hello"]
# 随机选一个词：import random 然后 random.choice(词库)
# 让用户猜这个词，猜对为止
# 每次提示"错了，再猜"，猜对打印猜了几次
word = ["python", "apple", "banana", "orange", "hello"]
target_word = random.choice(word)
guess_count = 0

while True:
    guess = input("猜一个词：")
    guess_count += 1
    if guess == target_word:
        print(f"猜对了！你猜了 {guess_count} 次。")
        break
    else:
        print("错了，再猜")


# ========== 练习4（选做）：去重 ==========
# 列表 [1, 2, 2, 3, 3, 3, 4]，去掉重复的数字
# 提示：用 in 判断是否已经在新列表里
num = [1, 2, 2, 3, 3, 3, 4]
new = []
for n in num:
    if n not in new:
        new.append(n)
print(new)