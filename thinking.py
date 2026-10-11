# 练习一
def area(width,height):
    area1 = width * height
    return area1

width,height = int(input("请输入宽度:")),int(input("请输入高度:"))
print(f"面积为: {area(width,height)}")

#练习二
def add_return(a,b):
    m =  a + b
    return m

def add_print(a,b):
    m = a+b
    print(m)

x = add_return(3,5)
y = add_print(3,5)
print(x)
print(y) 

#练习三
def check_score(score):
    if score >= 60:
        return"及格"
    else:
        return"不及格"  
grade = (85,59,60)
for i in grade:
    print(f"{i},{check_score(i)}")

#选做
def make_tag(name,prefix = "机器人"):
    return prefix + "-" +name
print(make_tag("A01"))
print(make_tag("A01","机械臂"))
