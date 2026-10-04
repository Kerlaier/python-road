# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
"""
============================================================
  Python 从入门到精通 —— 第6课：函数
  实战场景：舵机PWM计算、传感器判断、电机控制
============================================================
"""

# ============================================================
# 一、为什么要学函数？—— 代码别写两遍
# ============================================================
print("[场景1] 控制6个舵机——没学函数你会怎么写？")
print("-" * 30)

# 假如舵机角度转PWM公式是：PWM = 500 + 角度 × 2000 ÷ 180
# 没函数的时候，每个舵机都要重写一遍公式：

servo1 = 500 + 30 * 2000 / 180     # 算死你，公式一模一样！
servo2 = 500 + 60 * 2000 / 180
servo3 = 500 + 90 * 2000 / 180
# ... 写到第6个已经烦了

print(f"servo1: {servo1}")
print(f"servo2: {servo2}")
print(f"servo3: {servo3}")

# 而且万一公式错了，6行全部得改。函数就是解决这个问题的。

# ============================================================
# 二、函数的创建和调用 —— def = 定义一个函数
# ============================================================
print("\n[场景2] 用函数封装舵机角度→PWM计算")
print("-" * 30)

# 语法：
#   def 函数名(参数):
#       return 结果

def angle_to_pwm(angle):                                 # 定义函数
    """把舵机角度(0-180°)转成PWM值(500-2500)"""           # 说明书（可选）
    pwm = 500 + angle * 2000 / 180                       # 计算公式
    return pwm                                           # 返回结果

# 调用：直接用！
print(f"30° → PWM = {angle_to_pwm(30)}")        # 833.33
print(f"60° → PWM = {angle_to_pwm(60)}")        # 1166.67
print(f"90° → PWM = {angle_to_pwm(90)}")        # 1500.0
print(f"180° → PWM = {angle_to_pwm(180)}")       # 2500.0

# 口诀：
#   def 函数名(参数):      ← 创建函数，就像写了一个"公式模板"
#   return 计算结果         ← 把结果扔出去，谁调用就给谁

# ============================================================
# 三、参数 —— 函数能收多个输入
# ============================================================
print("\n[场景3] 计算小车电机转速——两个参数")
print("-" * 30)

# 语法：
#   def 函数名(参数1, 参数2):
#       return 结果

def wheel_speed(voltage, wheel_diameter):
    """输入电压(V)和轮径(cm)，返回转速(rpm)
       公式：转速 = (电压 × 60) / (轮径 × π) × 10  （简化公式）"""
    rpm = (voltage * 60) / (wheel_diameter * 3.14) * 10
    return rpm

speed1 = wheel_speed(12, 6.5)     # 12V电压，6.5cm轮子
speed2 = wheel_speed(7.4, 6.5)    # 7.4V电压，同样的轮子

print(f"12V电压: {speed1:.0f} rpm")        # 约 353 rpm
print(f"7.4V电压: {speed2:.0f} rpm")       # 约 218 rpm  — 电压低转得慢

# ============================================================
# 四、return vs print —— 这俩不一样！
# ============================================================
print("\n[重要] return 和 print 的区别")
print("-" * 30)

def add_with_return(a, b):
    return a + b                  # return：把结果交回去，可以存变量

def add_with_print(a, b):
    print(a + b)                  # print：只是在屏幕上显示，没交回去

result1 = add_with_return(3, 5)   # result1 = 8 ✅
result2 = add_with_print(3, 5)    # 屏幕显示 8，但 result2 是 None ❌

print(f"result1 = {result1}")     # 8
print(f"result2 = {result2}")     # None  ← 空的！print 没法把值存到变量

# 口诀：
#   return  → 把结果交给外部，可以存变量、接着算
#   print   → 只是让你看一眼，别的什么也做不了

# ============================================================
# 五、默认参数 —— 不传值就用默认的
# ============================================================
print("\n[场景4] 电机控制器——多数情况用默认电压")
print("-" * 30)

# 语法：
#   def 函数名(参数=默认值):
#       return 结果

def motor_power(speed_percent, voltage=12):
    """计算电机实际功率(W)
       speed_percent: 速度百分比(0-100)
       voltage: 供电电压(V)，默认12V"""
    current = speed_percent / 100 * 2    # 最大电流2A
    power = voltage * current
    return power

# 12V系统（默认值）      # 7.4V系统（手动指定）
p1 = motor_power(50)     # 不传 voltage，默认用 12V
p2 = motor_power(50, 7.4)  # 传了 7.4，覆盖默认值

print(f"12V系统 50%速度: {p1:.1f}W")     # 12.0W
print(f"7.4V系统 50%速度: {p2:.1f}W")    # 7.4W

# ============================================================
# 六、函数可以调用函数 —— 搭积木
# ============================================================
print("\n[场景5] 机械臂末端位置计算——函数套函数")
print("-" * 30)

def shoulder_angle_to_xy(angle):
    """肩关节角度 → 肩部末端的(x,y)坐标
       假设大臂长20cm，计算公式（简化）"""
    import math
    rad = math.radians(angle)           # 角度转弧度
    x = 20 * math.cos(rad)              # x = 臂长 × cos(角度)
    y = 20 * math.sin(rad)              # y = 臂长 × sin(角度)
    return (x, y)                       # 返回一个元组

def arm_position(shoulder_angle):
    """机械臂整体位置计算，调用上面的函数"""
    x, y = shoulder_angle_to_xy(shoulder_angle)   # 调用另一个函数！
    print(f"肩关节 {shoulder_angle}° → 坐标 ({x:.1f}, {y:.1f})")

# 测试几个角度
arm_position(0)     # 0°   → 水平，坐标 (20.0, 0.0)
arm_position(45)    # 45°  → 斜上，坐标 (14.1, 14.1)
arm_position(90)    # 90°  → 垂直，坐标 (0.0, 20.0)

# ============================================================
# 七、实战：机器人传感器报警系统
# ============================================================
print("\n[场景6] 传感器报警系统——多个函数协作")
print("-" * 30)

# 三个独立的判断函数
def check_temperature(temp):
    """温度传感器检查：>70°C 报警"""
    if temp > 70:
        return f"⚠ 高温警报！{temp}°C"
    return f"✓ 温度正常 {temp}°C"

def check_distance(dist):
    """超声波传感器检查：<30cm 报警"""
    if dist < 30:
        return f"⚠ 碰撞警报！距离{30}cm"

def check_current(current, limit=5):
    """电流检查：>限制值报警"""
    if current > limit:
        return f"⚠ 过流警报！{current}A"
    return f"✓ 电流正常 {current}A"

# 一次检查所有传感器
temp_status = check_temperature(75)      # 75°C，会报警
dist_status = check_distance(50)         # 50cm，安全
curr_status = check_current(3.2)         # 3.2A，正常

print(f"温度传感器: {temp_status}")
print(f"距离传感器: {dist_status}")
print(f"电流传感器: {curr_status}")

# ============================================================
# 本课小结
# ============================================================
print("\n" + "=" * 50)
print("[总结] 函数速查")
print("=" * 50)
print("""
  创建（带参数）：
      def 函数名(参数1, 参数2):
          return 结果

  创建（带默认值）：
      def 函数名(参数1, 参数2=默认值):
          return 结果

  调用：
      函数名(值1, 值2)            ← 按位置传参
      函数名(参数1=值1)            ← 按名字传参

  关键区别：
      return → 把结果交出去，能存变量继续用
      print  → 只在屏幕上显示

  记忆口诀：
      def 加 函数名 加 括号和冒号
      return 把结果扔掉
      调用直接写名字，传个参数就完事

下一课：列表与字典 —— 传感器数据存储与处理
""")
