# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
"""
============================================================
  Python 从入门到精通 —— 第3课：输入输出 & 运算符
  场景：做一个"餐厅点餐计算器"
============================================================
"""

print("=" * 50)
print("  第3课：输入输出 & 运算符")
print("  实战项目：餐厅点餐计算器")
print("=" * 50)

# ============================================================
# 一、print() —— 输出内容到屏幕
# ============================================================
print("\n" + "-" * 40)
print("[场景1] 打印小票")
print("-" * 40)

# print() 可以一次输出多个东西，用逗号隔开
dish = "红烧肉"
price = 38
print("菜品:", dish, "| 价格:", price, "元")

# sep 控制分隔符，默认是空格
print("姓名", "张三", "金额", "100", sep=" | ")

# end 控制结尾，默认换行
print("正在计算", end="...")
print("完成！")       # 紧跟在 ... 后面

# 实际应用：打印一个简单小票
print("\n===== 点餐小票 =====")
print("菜品: 红烧肉 x1   38元")
print("菜品: 可乐 x2      10元")
print("-------------------")
print("合计:             48元")
print("===================")


# ============================================================
# 二、input() —— 从键盘获取输入
# ============================================================
print("\n" + "-" * 40)
print("[场景2] 让用户输入信息")
print("-" * 40)

print("注意：运行到这里会停下来等你输入！")

# 模拟输入（注释掉真实的 input，用变量代替，
# 这样你运行脚本时不会被卡住）
# name = input("请输入你的名字: ")

# 为了脚本能跑完，我们先模拟一下结果：
name = "小明"    # 假装用户输入了"小明"
print(f"欢迎光临，{name}！")

# *** 黄金规则：input() 返回的永远是字符串！***
# age = input("请输入年龄: ")   # 假设输入 25
# age 此时是 "25"（字符串），不是 25（数字）！
# age + 1  会报错！因为 "25" + 1 不能运算


# ============================================================
# 三、类型转换 —— 把 input 的字符串转成数字
# ============================================================
print("\n" + "-" * 40)
print("[场景3] 计算总价（input + 类型转换）")
print("-" * 40)

# 模拟用户输入
price_str = "38"      # input() 返回的就是这种字符串
count_str = "2"

# 转成数字再算
price = int(price_str)      # "38" -> 38
count = int(count_str)      # "2"  -> 2
total = price * count

print(f"单价: {price}元")
print(f"数量: {count}")
print(f"小计: {total}元")      # 76元


# ============================================================
# 四、运算符实战 —— 餐厅账单计算
# ============================================================
print("\n" + "-" * 40)
print("[场景4] 完整的餐厅账单")
print("-" * 40)

dish_price = 38        # 一道菜的价格
dish_count = 2         # 点了两份
drink_price = 5        # 饮料单价
drink_count = 3        # 点了三杯
service_fee_rate = 0.1  # 服务费 10%

# 算术运算符：+ - * / // % **
food_total = dish_price * dish_count     # 菜品小计
drink_total = drink_price * drink_count  # 饮料小计
subtotal = food_total + drink_total      # 小计
service_fee = subtotal * service_fee_rate # 服务费
grand_total = subtotal + service_fee     # 总计

print(f"菜品: {dish_price}元 x {dish_count} = {food_total}元")
print(f"饮料: {drink_price}元 x {drink_count} = {drink_total}元")
print(f"小计: {subtotal}元")
print(f"服务费({service_fee_rate*100}%): {service_fee:.1f}元")
print(f"应付总额: {grand_total:.1f}元")

# 比较运算符：检查预算
budget = 120
print(f"\n预算: {budget}元")
print(f"超预算了? {grand_total > budget}")   # True/False
print(f"刚好够? {grand_total <= budget}")

# 整除和取余：AA制
people = 3
per_person = grand_total // people   # 整除：每人付多少
remainder = grand_total % people     # 取余：剩几块零头
print(f"\n{people}人AA:")
print(f"每人付: {per_person:.0f}元, 多出: {remainder:.1f}元")


# ============================================================
# 五、运算符速查
# ============================================================
print("\n" + "-" * 40)
print("[运算符速查表]")
print("-" * 40)

x, y = 10, 3
print(f"假设 x={x}, y={y}")

print(f"\n--- 算术 ---")
print(f"x + y  = {x + y}    # 加")
print(f"x - y  = {x - y}     # 减")
print(f"x * y  = {x * y}    # 乘")
print(f"x / y  = {x / y:.2f}  # 除（有小数）")
print(f"x // y = {x // y}     # 整除（不要小数）")
print(f"x % y  = {x % y}      # 取余（剩下的）")
print(f"x ** y = {x ** y}   # 次方")

print(f"\n--- 比较（结果是 True/False）---")
print(f"x == y  = {x == y}   # 等于（双等号！）")
print(f"x != y  = {x != y}    # 不等于")
print(f"x > y   = {x > y}    # 大于")
print(f"x < y   = {x < y}   # 小于")
print(f"x >= 10 = {x >= 10}    # 大于等于")

print(f"\n--- 赋值 ---")
print("x += 5  等价于  x = x + 5")
print("x -= 5  等价于  x = x - 5")


# ============================================================
# 本课小结
# ============================================================
print("\n" + "=" * 50)
print("[总结] 你学到了什么？")
print("=" * 50)
print("""
[v] print() 输出，sep/end 控制格式
[v] input() 获取用户输入（记住：永远返回字符串！）
[v] int() / float() 把字符串转成数字
[v] 算术运算符：+ - * / // % **
[v] 比较运算符：== != > < >= <= （结果是 True/False）
[v] 实战：完整计算一个餐厅账单

下一课：条件判断 if/elif/else
  - 根据消费金额给不同折扣
  - 根据分数评等级
  - 登录成功/失败的判断
""")

print("脚本运行完毕！接下来自己动手输入才是关键。")
