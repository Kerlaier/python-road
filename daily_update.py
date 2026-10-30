# -*- coding: utf-8 -*-
"""每日自动更新脚本 —— 检测新内容并生成文档推送到 GitHub"""
import os, subprocess, sys, glob, shutil

SOURCE = os.path.expanduser(r"~\Desktop\python学习文件")
STATE_FILE = os.path.expanduser(r"~\Desktop\python-road\.last_update")
REPO = os.path.expanduser(r"~\Desktop\python-road")
SCRIPT = os.path.join(REPO, "generate_doc.py")

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
    if result.returncode != 0:
        print(f"[生成失败] returncode={result.returncode}")
        sys.exit(1)

    # generate_doc.py 已直接输出到仓库学习录目录，无需额外复制

    # 复制 thinking.py 到仓库根目录
    thinking_src = os.path.join(SOURCE, "thinking.py")
    if os.path.exists(thinking_src):
        shutil.copy2(thinking_src, os.path.join(REPO, "thinking.py"))
        print("  已复制 thinking.py")

    print("[已复制到仓库]")

    # 推送到 GitHub：代理可选；任何关键 Git 步骤失败都不更新状态。
    repo = os.path.expanduser(r"~\Desktop\python-road")
    proxy_args = []
    pet_proxy = os.environ.get("PET_GIT_PROXY", "").strip()
    if pet_proxy:
        proxy_args = ["-c", f"http.proxy={pet_proxy}", "-c", f"https.proxy={pet_proxy}"]
    else:
        http_proxy = (os.environ.get("HTTP_PROXY") or os.environ.get("http_proxy") or "").strip()
        https_proxy = (os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy") or "").strip()
        if http_proxy:
            proxy_args.extend(["-c", f"http.proxy={http_proxy}"])
        if https_proxy:
            proxy_args.extend(["-c", f"https.proxy={https_proxy}"])

    git_prefix = ["git", "-C", repo, *proxy_args]

    def run_git(args, action):
        completed = subprocess.run(
            [*git_prefix, *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        if completed.stdout:
            print(completed.stdout, end="")
        if completed.stderr:
            print(completed.stderr, end="", file=sys.stderr)
        if completed.returncode != 0:
            print(f"[{action}失败] returncode={completed.returncode}")
            sys.exit(1)
        return completed

    run_git(["add", "-A"], "git add")
    commit = subprocess.run(
        [*git_prefix, "commit", "-m", f"自动更新: 学习录 {os.path.basename(SOURCE)}"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if commit.stdout:
        print(commit.stdout, end="")
    if commit.stderr:
        print(commit.stderr, end="", file=sys.stderr)
    if commit.returncode != 0:
        commit_output = f"{commit.stdout or ''}\n{commit.stderr or ''}".lower()
        if "nothing to commit" not in commit_output and "no changes added to commit" not in commit_output:
            print(f"[git commit失败] returncode={commit.returncode}")
            sys.exit(1)
        print("[无新变更] 跳过提交，继续推送已有本地提交")

    run_git(["push", "origin", "main"], "git push")
    print("[已推送到 GitHub]")

    # 仅在生成、提交和推送均成功后记录更新时间。
    with open(STATE_FILE, "w") as f:
        f.write(str(latest))
    print("[完成]")

if __name__ == "__main__":
    main()

