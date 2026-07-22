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
shopping = []
shopping.append("鸡蛋")
shopping.append("牛奶")
shopping.append("面包")
shopping.append("苹果")
shopping.remove("面包")
print("购物清单：", shopping)


# ========== 练习2：成绩分析 ==========
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
num = [1, 2, 2, 3, 3, 3, 4]
new = []
for n in num:
    if n not in new:
        new.append(n)
print(new)
