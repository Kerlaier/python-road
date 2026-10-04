# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
"""
============================================================
  第9课练习 —— NumPy
  规则：每个练习只给提示，请把答案写在下面
============================================================
"""

import numpy as np

print("=" * 40)
print("  第9课练习 —— NumPy")
print("=" * 40)

# ========== 练习1：传感器读数批量转换 ==========
# 题干：
#   6 个电机电压读数（伏特）：12.1, 11.8, 12.5, 11.2, 12.0, 11.9
#   用 np.array 创建数组，每个元素加 0.3（电压补偿），打印结果

# 提示：
#   arr = np.array([...])
#   print(arr + 0.3)

# ↓↓↓ 你的代码 ↓↓↓
arr = np.array([12.1, 11.8, 12.5, 11.2, 12.0, 11.9])
print(arr + 0.3)

# ========== 练习2：创建角度序列 ==========
# 题干：
#   舵机从 0° 到 180°，每隔 45° 取一个角度
#   用 np.arange 创建这个序列，打印结果

# 提示：
#   np.arange(起点, 终点不含, 步长)  ← 注意终点要写多少

# ↓↓↓ 你的代码 ↓↓↓
print(np.arange(0,181,45))

# ========== 练习3：旋转 180° ==========
# 题干：
#   机械臂末端在 (2.0, 3.0)，绕原点旋转 180°
#   用旋转矩阵 + @ 运算符计算旋转后的新坐标，打印结果
#   （180° 旋转后，(x, y) → (-x, -y)，正好相反方向）

# 提示：
#   theta = np.radians(180)
#   rot = np.array([[np.cos(theta), -np.sin(theta)],
#                   [np.sin(theta),  np.cos(theta)]])
#   new_pos = rot @ pos

# ↓↓↓ 你的代码 ↓↓↓
original = np.array([2.0,3.0])
theta = np.radians(180)
rot = np.array([[np.cos(theta), -np.sin(theta)],
                [np.sin(theta),  np.cos(theta)]])
new_pos = rot @ original
print(f"原坐标: ({original[0]:.1f}, {original[1]:.1f})")
print(f"旋转180°后: ({new_pos[0]:.1f}, {new_pos[1]:.1f})")

# ========== 练习4（选做）：统计传感器稳定性 ==========
# 题干：
#   超声波传感器连续测距 10 次（单位 cm）：
#   150, 152, 149, 151, 148, 153, 150, 152, 149, 151
#   用 np.array 创建数组，计算并打印：平均值、最大值、最小值

# 提示：
#   np.mean(arr) / np.max(arr) / np.min(arr)

# ↓↓↓ 你的代码 ↓↓↓
arr = np.array([150, 152, 149, 151, 148, 153, 150, 152, 149, 151])
print('平均值：',np.mean(arr))
print('最大值：',np.max(arr))
print('最小值：',np.min(arr))