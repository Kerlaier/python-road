# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
"""
============================================================
  第8课练习 —— 文件读写
  规则：每个练习只给提示，请把答案写在下面
============================================================
"""

print("=" * 40)
print("  第8课练习 —— 文件读写")
print("=" * 40)

# ========== 练习1：写入巡检日志 ==========
# 题干：
#   机器人巡检了两个房间，把结果写入 room_check.txt：
#     房间A: 正常
#     房间B: 异常（温度过高）
#   每行一条，用 with open + write 实现

# 提示：
#   with open("room_check.txt", "w") as f:
#       f.write("内容\n")    ← \n 换行

# ↓↓↓ 你的代码 ↓↓↓
with open("room_check.txt", "w") as f:
    f.write("房间A: 正常\n")
    f.write("房间B: 异常（温度过高）\n")


# ========== 练习2：读取并统计 ==========
# 题干：
#   先创建一个 temp_data.txt，写入以下内容：
#     36.5
#     38.2
#     37.0
#     42.1
#     36.8
#   然后读取这个文件，计算并打印所有温度的平均值

# 提示：
#   - 写入：遍历列表，逐行 f.write(str(t) + "\n")
#   - 读取：for line in f: 拿到每行，float(line.strip()) 转数字
#   - 累计 sum / 计数 len 求平均

# ↓↓↓ 你的代码 ↓↓↓
with open ("temp_date.txt","w") as f:
    f.write(str(36.5) + "\n")
    f.write(str(38.2) + "\n")
    f.write(str(37.0) + "\n")
    f.write(str(42.1) + "\n")
    f.write(str(36.8) + "\n")
with open ("temp_date.txt","r") as f:
    total = 0
    count = 0
    for line in f:
        num = float(line.strip())
        total = total + num
        count = count + 1
    print(f"average = {total / count}")
  
# ========== 练习3：CSV日志追加 ==========
# 题干：
#   先创建一个 motor_log.csv，写入表头和两条电机转速记录：
#     时间, 电机, 转速
#     08:00, A, 1500
#     08:05, A, 1480
#   然后用追加模式 "a"，再加一条：08:10, A, 1520
#   最后读取整个文件并打印确认

# 提示：
#   - 写/追加都用 csv.writer(f)
#   - writer.writerow([值1, 值2, 值3])
#   - 读用 csv.reader(f)，for row in reader:

import csv

# ↓↓↓ 你的代码 ↓↓↓
with open("motor_log", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["时间","电机","转速"])
    w.writerow(["08:00","A","1500"])
    w.writerow(["08:05","A","1480"])

with open("motor_log", "a", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["08:10","A","1520"])

with open("motor_log", "r", newline="", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



# ========== 练习4（选做）：异常日志追加 ==========
# 题干：
#   机器人运行中偶尔报错，用追加模式往 error.log 里记录错误
#   格式：时间, 错误代码, 描述
#   模拟写入两条错误记录，然后读出全部内容

# 提示：
#   追加模式 "a"，普通 write 就行，不用 csv 模块

# ↓↓↓ 你的代码 ↓↓↓
with open ("error.log","w") as f:
    f.write("时间,错误代码,描述\n")
with open ("error.log","a") as f:
    f.write("08:05, E002, 传感器离线\n")
with open("error.log", "r") as f:
    print(f.read())        