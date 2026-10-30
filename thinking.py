import pandas as pd

df = pd.DataFrame({
    "姓名": ["小明", "小红", "小刚"],
    "数学": [90, 85, 78],
    "英语": [88, 92, 70],
})

print(df["数学"])
df["总分"] = df["数学"] + df["英语"]     # 加一列
print(df)


