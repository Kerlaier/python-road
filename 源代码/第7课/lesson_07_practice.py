# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
"""
============================================================
  第7课练习 —— 元组 tuple
============================================================
"""

print("=" * 40)
print("  第7课练习")
print("=" * 40)

# ========== 练习1：创建月份元组 ==========
# 创建一个元组 months，包含12个月的中文名："一月"~"十二月"
# 用索引打印第一个月、第六个月、最后一个月
# 用切片打印前三个月

# 提示：
#   元组用 () 创建
#   索引从 0 开始，-1 是最后一个
#   切片 [起点:终点] 含头不含尾
months = ("一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月")
print(f'first month: {months[0]}')
print(f'sixth month: {months[5]}')
print(f'last month: {months[-1]}')
print(f'first three months: {months[:3]}')



# ========== 练习2：交换两个变量 ==========
# 不用临时变量，直接交换 a 和 b 的值
# 然后打印交换后的结果

a = "咖啡"
b = "奶茶"

# 提示：元组拆包 a, b = b, a  ← 这一行就够了！
a,b = b,a
print(f'a:{a},b:{b}')




# ========== 练习3：餐厅菜单 ==========
# 下面有一个菜单元组的列表, 每条是 (菜名, 价格)
# 请用 for 循环 + 拆包 打印所有菜品和价格
# 计算并打印: "最贵的菜是: xxx"

menu = [
    ("红烧肉", 38),
    ("清蒸鱼", 45),
    ("炒青菜", 18),
    ("番茄汤", 15),
]

# 打印所有菜品
for name, price in menu:
    print(f"菜品: {name}, 价格: {price}")

# 找最高价 —— 用普通 for 循环
max_price = menu[0][1]           # 先假设第一个最贵
for name, price in menu:
    if price > max_price:        # 遇到更贵的就更新
        max_price = price

# 找最贵的菜名
for name, price in menu:
    if price == max_price:
        print(f"最贵的菜是: {name}, 价格: {max_price}")


# 提示：
#   for name, price in menu:   ← 遍历 + 拆包
#   max() 不能直接对元组列表用，需要自己用循环找


# ========== 练习4（选做）：成绩统计 ==========
# 下面 students 是 (姓名, 分数) 的列表
# 1. 计算平均分 sum() / len()
# 2. 打印所有不及格（<60）的学生姓名
# 3. 用 enumerate 给每个人加上序号打印

students = [
    ("小明", 90),
    ("小红", 55),
    ("小刚", 78),
    ("小美", 42),
    ("小华", 85),
]

# 1. 收集分数，求平均分
scores = []                          # 空列表装分数
for name, score in students:
    scores.append(score)             # 把每个分数装进去
avg = sum(scores) / len(scores)
print(f"平均分: {avg:.1f}")

# 2. 找不及格的（<60）
print("不及格的学生:")
for name, score in students:
    if score < 60:
        print(f"  {name}: {score}分")

# 3. 用 enumerate 给每个人加序号
print("全部学生:")
for i, (name, score) in enumerate(students, 1):
    print(f"  {i}. {name}: {score}分")




# 提示：
#   sum() 不能直接对元组列表用，需要另外收集分数
#   先建一个空列表，循环把分数 append 进去
