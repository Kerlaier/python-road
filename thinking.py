# 练习一
robot = {"型号":"UR5","自由度":6,"负载":5}
for k,v in robot.items():
    print(k,v)

#练习二    
#print(robot["精度"])  #会报错 
print(robot.get("精度"))

#练习三
sensors = {"温度": 36.5, "湿度": 45.2, "气压": 1013}
sensors["风速"] = 3.2
sensors["温度"] = 37.1
del sensors["湿度"]
print(sensors) 

#选做
motor_temps = {"电机A":42, "电机B":55, "电机C":38, "电机D":60, "电机E":45}
for k,v in motor_temps.items():
    if v >= 50:
        print(f"{k}过热")
    else:
        print(f"{k}正常")


