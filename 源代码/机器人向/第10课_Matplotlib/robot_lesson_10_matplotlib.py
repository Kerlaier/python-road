# -*- coding: utf-8 -*-
"""
============================================================
  第10课 —— Matplotlib
  让数据"看得见"：画舵机运动轨迹曲线
============================================================
"""

import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用微软雅黑显示中文
matplotlib.rcParams['axes.unicode_minus'] = False              # 解决负号显示成方块

import matplotlib.pyplot as plt    # 约定俗成的别名 plt
import numpy as np

print("=" * 50)
print("  第10课：Matplotlib")
print("=" * 50)

# ============================================================
# 一、为什么需要画图？
# ============================================================
# 一堆数字看不出规律，画成图就一目了然。
#   温度: 36.5 38.2 37.0 42.1 36.8  → 看数字：眼花
#   折线图：一眼看出哪个点温度异常！

# 语法公式：
#   plt.plot(x轴数据, y轴数据)    ← 画线
#   plt.show()                   ← 显示图形


# ============================================================
# 二、第一张图：温度变化曲线
# ============================================================

# 数据准备
time  = [0, 1, 2, 3, 4, 5]                    # x 轴：时间
temps = [36.5, 38.2, 37.0, 42.1, 36.8, 37.5]  # y 轴：温度

# 画图四步
plt.figure(figsize=(8, 4))          # 1. 创建画布（宽8高4英寸）
plt.plot(time, temps, marker='o')   # 2. 画线，marker='o' 加上圆点
plt.title("机器人温度变化")          # 3. 标题
plt.xlabel("时间 (秒)")              #    x轴标签
plt.ylabel("温度 (°C)")              #    y轴标签
plt.grid(True)                      #   网格线
plt.show()                           # 4. 显示！

# 运行后弹出一个窗口，点 × 关掉才能继续


# ============================================================
# 三、舵机运动轨迹 —— sin 曲线
# ============================================================
# 场景：舵机来回摆动，角度随时间变化

t = np.linspace(0, 2*np.pi, 100)     # 0 到 2π，取100个点（光滑曲线）
angle = 90 * np.sin(t) + 90          # 舵机角度：0°~180°，以90°为中心正弦摆动
#             ↑ sin值在-1~1，乘90后范围-90~90，再加90偏移为0~180

plt.figure(figsize=(8, 4))
plt.plot(t, angle, color='blue', linewidth=2)  # 蓝线，线宽2平
plt.axhline(y=90, color='gray', linestyle='--', label='中位 90°')  # 水平参考线
plt.title("舵机正弦摆动轨迹")
plt.xlabel("时间 (弧度)")
plt.ylabel("角度 (°)")
plt.legend()                         # 显示图例
plt.grid(True)
plt.show()

print()


# ============================================================
# 四、多条曲线 + 图例
# ============================================================
# 场景：对比三个关节的角度变化

t = np.linspace(0, 2*np.pi, 100)

shoulder = np.sin(t) * 45 + 45       # 肩部：0~90°
elbow    = np.sin(t + 1) * 30 + 60   # 肘部：相位偏移1，看起来有时差
wrist    = np.sin(t + 2) * 20 + 80   # 腕部：相位偏移2

plt.figure(figsize=(8, 4))
plt.plot(t, shoulder, label='肩部', linewidth=2)   # label 决定图例显示什么
plt.plot(t, elbow,    label='肘部', linewidth=2)
plt.plot(t, wrist,    label='腕部', linewidth=2)
plt.title("三关节舵机运动对比")
plt.xlabel("时间")
plt.ylabel("角度 (°)")
plt.legend()                         # 图例自动取每条线的 label
plt.grid(True)
plt.show()

print()


# ============================================================
# 五、子图 —— 一页放多张图
# ============================================================
# 场景：同时监控温度和电压

t = np.linspace(0, 5, 50)
temp   = 36 + np.sin(t) * 2 + np.random.randn(50) * 0.5     # 温度（加噪音）
voltage = 12 + np.sin(t + 0.5) + np.random.randn(50) * 0.3  # 电压

# plt.subplot(行数, 列数, 第几个)
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)                 # 1行2列，第1个
plt.plot(t, temp, color='red')
plt.title("温度")
plt.xlabel("时间")
plt.ylabel("°C")
plt.grid(True)

plt.subplot(1, 2, 2)                 # 1行2列，第2个
plt.plot(t, voltage, color='blue')
plt.title("电机电压")
plt.xlabel("时间")
plt.ylabel("V")
plt.grid(True)

plt.tight_layout()                   # 自动调间距，不让标题重叠
plt.show()

print()


# ============================================================
# 六、实战：机械臂末端运动轨迹
# ============================================================
# 场景：机械臂末端画一个圆，实际就是 x=cosθ, y=sinθ

theta = np.linspace(0, 2*np.pi, 200)
r = 5                                # 臂长 5

x = r * np.cos(theta)                # x 坐标
y = r * np.sin(theta)                # y 坐标

plt.figure(figsize=(5, 5))
plt.plot (x, y, linewidth=2, color='green')
plt.plot(0, 0, 'ro', markersize=8)   # 原点（基座）标红点
plt.title("机械臂末端圆形轨迹（半径=5）")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis('equal')                    # x和y轴等比例，圆形不变椭圆！
plt.grid(True)
plt.show()

print()


# ============================================================
# 七、保存图片到文件
# ============================================================
# 用 plt.savefig() 替代 plt.show()，图片存硬盘，不弹窗
x = np.linspace(0, 4*np.pi, 500)
y = np.sin(x)

plt.figure(figsize=(8, 3))
plt.plot(x, y, linewidth=1)
plt.title("sin(x) 曲线")
plt.grid(True)
plt.savefig("sin_curve.png", dpi=150)   # 存为图片，dpi=150 清晰度
print("图片已保存：sin_curve.png")


# ============================================================
# 小结
# ============================================================
# ┌────────────────────┬───────────────────────────┐
# │ 操作                │ 写法                       │
# ├────────────────────┼───────────────────────────┤
# │ 画线                │ plt.plot(x, y)            │
# │ 标题/轴标签         │ plt.title/label(x/y)label │
# │ 网格                │ plt.grid(True)            │
# │ 图例                │ plt.legend()              │
# │ 显示                │ plt.show()                │
# │ 保存                │ plt.savefig("文件名.png")  │
# │ 子图                │ plt.subplot(行, 列, 序号)  │
# │ 等比例轴            │ plt.axis('equal')         │
# └────────────────────┴───────────────────────────┘
#
# 一句话：Matplotlib 把你的数据变成图，眼睛比脑子更快发现规律。
