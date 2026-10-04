# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
"""
============================================================
  第6课练习 —— 函数
============================================================
"""

print("=" * 40)
print("  第6课练习")
print("=" * 40)

# ========== 练习1：舵机角度转PWM ==========
# 写一个函数 servo_pwm(angle)，输入角度(0-180)，返回PWM值
# 公式：PWM = 500 + angle * 2000 / 180
# 调用它计算 0°、90°、180° 的PWM值并打印
def servo_pwm(angle):
    pwm = 500 + angle * 2000 / 180
    return pwm

print(f"0° → PWM = {servo_pwm(0)}")
print(f"90° → PWM = {servo_pwm(90)}")
print(f"180° → PWM = {servo_pwm(180)}")

# ========== 练习2：超声波距离判断 ==========
# 写一个函数 is_too_close(distance)，传入距离(cm)
# 小于30cm 返回 True（太近），否则返回 False
# 测试 25cm、50cm、30cm 三个值

def is_too_close(distance):
    if distance < 30:
        return True
    else:
        return False
print(f'25cm → Too close: {is_too_close(25)}')
print(f'50cm → Too close: {is_too_close(50)}')
print(f'30cm → Too close: {is_too_close(30)}')
# ========== 练习3：电池电量计算 ==========
# 写一个函数 battery_life(capacity, current)
# capacity: 电池容量(mAh)，current: 工作电流(mA)
# 返回续航时间 = capacity / current（小时）
# 参数 current 默认值设为 500(mA)
# 测试 capacity=3000，一次不传 current，一次传 current=1000
def battery_life(capacity,current=500):
    return capacity / current

print(f'time ={battery_life(3000)}')
print(f'time ={battery_life(3000,1000)}')

# ========== 练习4（选做）：电机控制组合函数 ==========
# 题干：
#   小车有左轮和右轮，各有一个速度(0-100)
#   写三个函数：
#     1. avg_speed(left, right)           返回左右轮平均速度
#     2. is_turning(left, right)          如果左右速度不等返回 True（在转弯）
#     3. move_forward(speed, time_sec)    返回前进距离 = speed × 0.1 × time_sec (cm)
#   最后调用三个函数，计算：左80右60，运行2秒的结果

# 提示：
#   函数1: return (left + right) / 2
#   函数2: return left != right
#   函数3: return speed * 0.1 * time_sec

def avg_speed(left,right):
    return (left + right) / 2

def is_turning(left,right):
    return left != right

def move_forward(speed, time_sec):
    return speed * 0.1 * time_sec

# 测试：左80右60，运行2秒
left_speed = 80
right_speed = 60
time = 2

print(f"平均速度: {avg_speed(left_speed, right_speed)}")
print(f"是否转弯: {is_turning(left_speed, right_speed)}")
print(f"前进距离: {move_forward(avg_speed(left_speed, right_speed), time)}")