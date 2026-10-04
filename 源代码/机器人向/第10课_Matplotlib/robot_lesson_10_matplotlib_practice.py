# -*- coding: utf-8 -*-
"""
============================================================
  第10课练习 —— Matplotlib
  规则：每个练习只给提示，请把答案写在下面
============================================================
"""

import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用微软雅黑显示中文
matplotlib.rcParams['axes.unicode_minus'] = False              # 解决负号显示成方块

import matplotlib.pyplot as plt
import numpy as np

# ========== 练习1：电池放电曲线 ==========
# 题干：
#   机器人运行中，电池电压从 12.6V 线性降到 11.0V，持续 60 分钟
#   画一条折线图，显示电压随时间的变化
#   要求：有标题、x轴"时间(分钟)"、y轴"电压(V)"、网格

# 提示：
#   time = np.array([0, 60])               ← 两个端点
#   voltage = np.array([12.6, 11.0])
#   plt.plot(time, voltage, marker='o')
#   plt.title(...)
#   plt.xlabel(...)
#   plt.ylabel(...)
#   plt.grid(True)
#   plt.show()

# ↓↓↓ 你的代码 ↓↓↓
time = np.array([0, 60])             
voltage = np.array([12.6, 11.0])
plt.figure(figsize=(8,4)) 
plt.plot(time, voltage, marker='o')
plt.title("电池放电曲线")
plt.xlabel("时间(分钟)")
plt.ylabel("电压(V)") 
plt.grid(True)
plt.show()


# ========== 练习2：两个舵机的摆动对比 ==========
# 题干：
#   舵机A：角度 = sin(t)*60 + 60（0°~120°）
#   舵机B：角度 = cos(t)*60 + 60（0°~120°）
#   t 从 0 到 2π，取200个点
#   两条线画在同一张图上，加 label、图例、网格

# 提示：
#   t = np.linspace(0, 2*np.pi, 200)
#   servo_a = np.sin(t)*60 + 60
#   servo_b = np.cos(t)*60 + 60
#   plt.plot(t, servo_a, label='舵机A')
#   plt.plot(t, servo_b, label='舵机B')
#   plt.legend()

# ↓↓↓ 你的代码 ↓↓↓
t = np.linspace(0,2*np.pi,200)
舵机A = np.sin(t)*60 + 60
舵机B = np.cos(t)*60 + 60
plt.figure(figsize=(8,4))
plt.plot(t, 舵机A, label='舵机A',color='blue')
plt.plot(t, 舵机B, label='舵机B',color='yellow')
plt.legend() 
plt.grid(True)
plt.show()


# ========== 练习3：机械臂画方形轨迹 ==========
# 题干：
#   机械臂末端走一个正方形路径：(0,0) → (4,0) → (4,4) → (0,4) → (0,0)
#   用 plt.plot 画出这个方形轨迹
#   要求：axis('equal') 保持正方形不变形，画网格

# 提示：
#   x = [0, 4, 4, 0, 0]    ← 首尾相接
#   y = [0, 0, 4, 4, 0]
#   plt.plot(x, y, marker='o')
#   plt.axis('equal')

# ↓↓↓ 你的代码 ↓↓↓
x = [0, 4, 4, 0, 0]
y = [0, 0, 4, 4, 0]
plt.figure(figsize=(5, 5))
plt.plot(x, y, marker='o')
plt.axis('equal')
plt.grid(True)
plt.show()


# ========== 练习4（选做）：保存轨迹图 ==========
# 题干：
#   画一条 sin(t) 曲线（t 0~4π，500个点），保存为 "sine_wave.png"

# 提示：
#   用 plt.savefig("sine_wave.png") 替换 plt.show()

# ↓↓↓ 你的代码 ↓↓↓
x = np.linspace(0,4*np.pi,500)
y = np.sin(x)
plt.figure(figsize=(8, 3))
plt.plot(x, y, linewidth=1)
plt.title("sin(x) 曲线")
plt.grid(True)
plt.savefig("sine_wave.png", dpi=150)   # 存为图片，dpi=150 清晰度
print("图片已保存：sine_wave.png")