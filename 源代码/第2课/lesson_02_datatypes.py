# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
"""
============================================================
  Python 从入门到精通 —— 第2课：数据类型
  （第1课「变量」已学完）
============================================================
运行方式：
  在终端中执行：python lesson_02_datatypes.py

AI助手注：你在Windows上，按 Ctrl+J 打开终端，
输入 python lesson_02_datatypes.py 即可运行。
（先 cd 到当前目录，或用正斜杠路径）
============================================================
"""

print("=" * 60)
print("  Python 数据类型")
print("=" * 60)

# ============================================================
# 一、数字类型 (Numeric Types)
# ============================================================
print("\n" + "-" * 40)
print("[1] 一、数字类型：int（整数）、float（小数）")
print("-" * 40)

# --- int（整数）---
age = 25              # 正整数
temperature = -10     # 负整数
population = 14_0000_0000  # 可以用下划线分隔，更易读

print(f"年龄: {age},  类型: {type(age)}")
print(f"温度: {temperature},  类型: {type(temperature)}")
print(f"中国人口约: {population}")

# --- float（浮点数 / 小数）---
pi = 3.1415926
price = 19.99
scientific = 1.5e-3   # 科学计数法 = 0.0015

print(f"\n圆周率: {pi},  类型: {type(pi)}")
print(f"价格: {price}")
print(f"科学计数法 1.5e-3 = {scientific}")

# --- 基本运算 ---
a, b = 10, 3
print(f"\n--- 基本运算 (a={a}, b={b}) ---")
print(f"加法:   {a} + {b} = {a + b}")
print(f"减法:   {a} - {b} = {a - b}")
print(f"乘法:   {a} * {b} = {a * b}")
print(f"除法:   {a} / {b} = {a / b}      <- 永远返回 float")
print(f"整除:   {a} // {b} = {a // b}     <- 去掉小数部分")
print(f"取余:   {a} % {b} = {a % b}       <- 余数")
print(f"幂运算: {a} ** {b} = {a ** b}     <- a的b次方")

# --- 内置数学函数 ---
print(f"\n--- 常用数学函数 ---")
print(f"abs(-5)    = {abs(-5)}          <- 绝对值")
print(f"round(3.6) = {round(3.6)}       <- 四舍五入")
print(f"round(3.14159, 2) = {round(3.14159, 2)}  <- 保留2位小数")
print(f"max(1,5,3) = {max(1, 5, 3)}     <- 最大值")
print(f"min(1,5,3) = {min(1, 5, 3)}     <- 最小值")
print(f"pow(2, 10) = {pow(2, 10)}       <- 2的10次方")


# ============================================================
# 二、字符串类型 (String)
# ============================================================
print("\n" + "-" * 40)
print("[2] 二、字符串类型：str")
print("-" * 40)

# --- 创建字符串 ---
name = 'Python'                  # 单引号
greeting = "你好，世界！"        # 双引号（推荐）
poem = """静夜思
床前明月光，疑是地上霜。
举头望明月，低头思故乡。"""     # 三引号（多行）

print(f'单引号: {name}')
print(f'双引号: {greeting}')
print(f'三引号多行:\n{poem}')

# --- 字符串索引（从0开始）---
word = "Hello Python"
print(f"\n--- 索引：word = '{word}' ---")
print(f"word[0]  = '{word[0]}'     <- 第1个字符")
print(f"word[1]  = '{word[1]}'     <- 第2个字符")
print(f"word[-1] = '{word[-1]}'    <- 倒数第1个")
print(f"word[-2] = '{word[-2]}'    <- 倒数第2个")

# --- 字符串切片 [起始:结束:步长] ---
print(f"\n--- 切片：word = '{word}' ---")
print(f"word[0:5]   = '{word[0:5]}'       <- 索引0到4（不含5）")
print(f"word[6:]    = '{word[6:]}'          <- 从索引6到末尾")
print(f"word[:5]    = '{word[:5]}'          <- 从开头到索引4")
print(f"word[::2]   = '{word[::2]}'        <- 每隔一个字符")
print(f"word[::-1]  = '{word[::-1]}'       <- 反转字符串！")

# --- 字符串常用方法 ---
print(f"\n--- 常用方法 ---")
s = "  Hello, Python World!  "
print(f"原始字符串:  '{s}'")
print(f"strip():     '{s.strip()}'          <- 去首尾空格")
print(f"upper():     '{s.upper()}'          <- 全大写")
print(f"lower():     '{s.lower()}'          <- 全小写")
print(f"replace():   '{s.replace('World', '朋友')}'  <- 替换")
print(f"split():     {s.strip().split()}           <- 按空格分割")
print(f"len():       {len(s)}                <- 字符串长度")

# --- f-string（格式化字符串）*** 重要！---
# 语法：f"任意文字 {变量名} 任意文字"
# 在字符串前面加 f，然后用 { } 把变量包起来
print(f"\n--- f-string 格式化（最常用）---")
name, score = "小明", 95.5

# 基础用法：{变量} 会被替换成变量的值
print(f"{name}考了{score}分！")
# 输出：小明考了95.5分！

# 控小数：{变量:.Nf} 保留 N 位小数
print(f"保留2位: {score:.2f}")    # 95.50
print(f"保留1位: {score:.1f}")    # 95.5
print(f"保留0位: {score:.0f}")    # 96  （四舍五入）

# 可以直接写表达式
a, b = 10, 3
print(f"{a} + {b} = {a + b}")     # 10 + 3 = 13

# 对齐（知道就行，不常用）：
print(f"右对齐10格: |{name:>10}|")   # |        小明|
print(f"左对齐10格: |{name:<10}|")   # |小明        |


# ============================================================
# 三、布尔类型 (Boolean)
# ============================================================
print("\n" + "-" * 40)
print("[3] 三、布尔类型：bool")
print("-" * 40)

is_raining = True
has_umbrella = False

print(f"下雨了吗？ {is_raining},  类型: {type(is_raining)}")
print(f"带伞了吗？ {has_umbrella}")

# --- 比较运算产生布尔值 ---
print(f"\n--- 比较运算 ---")
x, y = 10, 3
print(f"x={x}, y={y}")
print(f"x > y   -> {x > y}     <- 大于")
print(f"x < y   -> {x < y}     <- 小于")
print(f"x == y  -> {x == y}     <- 等于（注意是两个等号！）")
print(f"x != y  -> {x != y}     <- 不等于")
print(f"x >= y  -> {x >= y}     <- 大于等于")
print(f"x <= y  -> {x <= y}     <- 小于等于")
print(f"\n!! 注意：一个等号 = 是赋值，两个等号 == 是比较！")

# --- 逻辑运算 ---
print(f"\n--- 逻辑运算 ---")
print(f"True and True   = {True and True}    <- and：全真才真")
print(f"True and False  = {True and False}")
print(f"True or False   = {True or False}    <- or：有真就真")
print(f"False or False  = {False or False}")
print(f"not True        = {not True}         <- not：取反")
print(f"not False       = {not False}")

# --- bool() 函数：判断"真假" ---
print(f"\n--- bool() 判断真假 ---")
print(f"bool(0)     = {bool(0)}       <- 0 是 False")
print(f"bool(1)     = {bool(1)}        <- 非0数字是 True")
print(f"bool(100)   = {bool(100)}     <- 非0数字是 True")
print(f"bool('')    = {bool('')}       <- 空字符串是 False")
print(f"bool('Hi')  = {bool('Hi')}    <- 非空字符串是 True")
print(f"bool([])    = {bool([])}       <- 空列表是 False")


# ============================================================
# 四、类型转换 (Type Conversion)
# ============================================================
print("\n" + "-" * 40)
print("[4] 四、类型转换")
print("-" * 40)

# str -> int/float
num_str = "42"
print(f'str->int:   int("42")   = {int(num_str)}')
print(f'str->float: float("3.14") = {float("3.14")}')

# int/float -> str
print(f'int->str:   str(100)    = \'{str(100)}\'')

# 任何值 -> bool
print(f'int->bool:  bool(0)     = {bool(0)}')
print(f'int->bool:  bool(5)     = {bool(5)}')
print(f'str->bool:  bool("")    = {bool("")}')
print(f'str->bool:  bool("abc") = {bool("abc")}')

# !! 常见坑
print(f"\n!! 常见坑：")
print(f'"5" + "3"  = \'{"5" + "3"}\'     <- 字符串拼接！不是加法')
print(f'5 + 3      = {5 + 3}           <- 数字加法')
print(f'int("5") + int("3") = {int("5") + int("3")}   <- 先转换再运算')


# ============================================================
# 五、type() 和 isinstance() —— 检查类型
# ============================================================
print("\n" + "-" * 40)
print("[5] 五、检查类型")
print("-" * 40)

value = 42
print(f"type(value) = {type(value)}")
print(f"isinstance(value, int)  -> {isinstance(value, int)}")
print(f"isinstance(value, str)  -> {isinstance(value, str)}")
print(f"isinstance(value, (int, float))  -> {isinstance(value, (int, float))}  <- 多种类型")


# ============================================================
# 六、动手练习
# ============================================================
print("\n" + "=" * 60)
print(">> 动手练习（在下面自己写代码试试！）")
print("=" * 60)
print("""
练习1：计算圆的面积
  提示：面积 = pi * r ** 2  (pi约等于3.14)

练习2：把 "apple,banana,grape" 按逗号分割成列表

练习3：检查 100 是奇数还是偶数（用 % 取余）

练习4：把你的名字反转输出（用切片）

练习5：判断 2024 是否是闰年
  提示：能被4整除但不能被100整除，或者能被400整除
""")


# ============================================================
# 本课小结
# ============================================================
print("-" * 40)
print("[总结] 本课小结 - 你学到了什么？")
print("-" * 40)
print("""
[v] 数字类型：int（整数）和 float（小数），以及基本运算
[v] 字符串：索引、切片、常用方法（strip/upper/split等）
[v] f-string：最常用的格式化方式 f"我叫{name}"
[v] 布尔类型：True/False，比较运算和逻辑运算
[v] 类型转换：int()、str()、float()、bool()
[v] type() 和 isinstance() 检查类型

下一课预习：输入输出 input()/print() -> 条件判断 if/elif/else
""")

print("\n恭喜完成第2课！试着完成上面的练习吧~")
