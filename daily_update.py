# -*- coding: utf-8 -*-
"""每日自动更新脚本 —— 检测新内容并生成文档推送到 GitHub"""
import os, subprocess, sys, glob

SOURCE = os.path.expanduser(r"~\Desktop\python学习文件")
OUTPUT_DESKTOP = os.path.expanduser(r"~\Desktop\学习录")
OUTPUT_REPO = os.path.expanduser(r"~\Desktop\python-road\学习录")
STATE_FILE = os.path.expanduser(r"~\Desktop\python-road\.last_update")
SCRIPT = os.path.expanduser(r"~\Desktop\python-road\generate_doc.py")

def get_latest_py_time(folder):
    """获取文件夹中最新的 .py 文件修改时间"""
    py_files = glob.glob(os.path.join(folder, "*.py"))
    if not py_files:
        return 0
    return max(os.path.getmtime(f) for f in py_files)

def main():
    latest = get_latest_py_time(SOURCE)
    if latest == 0:
        print("[跳过] 学习文件夹为空")
        return

    # 读取上次记录的时间
    last = 0
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            try:
                last = float(f.read().strip())
            except:
                last = 0

    if latest <= last:
        print(f"[跳过] 没有新内容（上次更新: {last}, 最新文件: {latest})")
        return

    print(f"[检测到新内容] 生成文档...")
    result = subprocess.run([sys.executable, "-X", "utf8", SCRIPT],
                          capture_output=True, text=True, encoding="utf-8")
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

    # 复制到仓库目录
    os.makedirs(OUTPUT_REPO, exist_ok=True)
    for f in glob.glob(os.path.join(OUTPUT_DESKTOP, "*.docx")):
        dst = os.path.join(OUTPUT_REPO, os.path.basename(f))
        import shutil
        shutil.copy2(f, dst)
    print("[已复制到仓库]")

    # 推送到 GitHub
    repo = os.path.expanduser(r"~\Desktop\python-road")
    subprocess.run(["git", "-C", repo, "-c", "http.proxy=http://127.0.0.1:7890", "-c", "https.proxy=http://127.0.0.1:7890", "add", "-A"], check=False)
    subprocess.run(["git", "-C", repo, "-c", "http.proxy=http://127.0.0.1:7890", "-c", "https.proxy=http://127.0.0.1:7890", "commit", "-m", f"自动更新: 学习录 {os.path.basename(SOURCE)}"],
                   check=False)
    subprocess.run(["git", "-C", repo, "-c", "http.proxy=http://127.0.0.1:7890", "-c", "https.proxy=http://127.0.0.1:7890", "push", "origin", "main"], check=False)
    print("[已推送到 GitHub]")

    # 记录本次更新时间
    with open(STATE_FILE, "w") as f:
        f.write(str(latest))
    print("[完成]")

if __name__ == "__main__":
    main()

