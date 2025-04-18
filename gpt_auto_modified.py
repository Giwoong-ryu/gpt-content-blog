
# ✅ 2번 실행 (수정 버전): .md 자동 수집 → _posts 복사 → GitHub 푸시 자동화
# 파일명 앞에 중복 날짜 붙이지 않도록 수정됨

import os
import shutil
import datetime
import subprocess

# 사용자 설정
SOURCE_DIR = "C:/Users/user/Desktop/gpt-outputs"        # GPT가 자동 생성한 .md 파일 폴더
TARGET_DIR = "C:/Users/user/Desktop/gpt/gpt-content-blog/_posts"  # Jekyll 블로그 _posts 경로
REPO_DIR = "C:/Users/user/Desktop/gpt/gpt-content-blog"  # Git 저장소 루트 폴더

# 오늘 날짜
TODAY = datetime.datetime.now().strftime("%Y-%m-%d")

# 1. .md 파일 복사 (outputs → _posts), 파일명 그대로 사용
def copy_md_files():
    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith(".md"):
            src = os.path.join(SOURCE_DIR, filename)
            dst = os.path.join(TARGET_DIR, filename)
            shutil.copy2(src, dst)
            print(f"✅ 복사 완료: {dst}")

# 2. Git add, commit, push 자동 실행
def git_push():
    subprocess.run(["git", "add", "."], cwd=REPO_DIR)
    subprocess.run(["git", "commit", "-m", f"자동 포스팅: {TODAY}"], cwd=REPO_DIR)
    subprocess.run(["git", "push"], cwd=REPO_DIR)

if __name__ == "__main__":
    print("🛠 자동 블로그 포스팅 시작")
    copy_md_files()
    git_push()
    print("🚀 블로그 자동 업데이트 완료!")
