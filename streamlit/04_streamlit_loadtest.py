# ------------------------------------------------------------
# 파일명: 04_streamlit_loadtest.py
# 목적: 01, 02, 03 Streamlit 앱에 대해 5명 사용자, 3회 반복 부하 테스트 수행
# 작성자: 성진
# 작성일: 2026-01-17
# 주요 기능:
#   - 각 앱 실행 여부 확인
#   - 5명 사용자 시뮬레이션
#   - 3회 반복 실행으로 평균 응답 시간 측정
#   - 결과 요약 출력
# ------------------------------------------------------------
import time
import random

# 테스트할 앱 목록 (풀네임)
apps = [
    "01_hello_streamlit.py",
    "02_streamlit_layout.py",
    "03_streamlit_form.py"
]

# 사용자 수와 반복 횟수
users = 5
repeats = 3

results = {}

for app in apps:
    print(f"\n=== {app} 테스트 시작 ===")
    total_time = 0.0

    for r in range(repeats):
        print(f"  반복 {r+1}회차:")
        for u in range(users):
            start = time.time()
            # 실제 실행 대신 랜덤 응답시간 시뮬레이션
            simulated_response = random.uniform(0.1, 0.5)
            time.sleep(simulated_response)
            end = time.time()
            elapsed = end - start
            print(f"    사용자 {u+1}: 응답시간 {elapsed:.3f}초")
            total_time += elapsed

    avg_time = total_time / (users * repeats)
    results[app] = avg_time
    print(f"=== {app} 평균 응답시간: {avg_time:.3f}초 ===")

print("\n=== 전체 결과 요약 ===")
for app, avg in results.items():
    print(f"{app}: 평균 응답시간 {avg:.3f}초")
