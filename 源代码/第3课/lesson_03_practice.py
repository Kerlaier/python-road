# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("=" * 40)
print("  BMI 计算器")
print("=" * 40)

# ========== 练习1：获取用户输入 ==========

height = float(input("请输入你的身高（米）："))
weight = float(input("请输入你的体重（公斤）："))


# ========== 练习2：计算 BMI ==========

bmi = weight / (height * height)


# ========== 练习3：输出结果 ==========

print(f"你的 BMI 是: {bmi:.2f}")


# ========== 练习4（选做）：AA制分账 ==========

total = 298
people = 3
per_person = total // people
left = total % people
print(f"每人付{per_person}元，还剩{left}元")


# ========== 练习5（选做）：判断是否超预算 ==========

budget = 50
spent = 67.5
print(spent > budget)
