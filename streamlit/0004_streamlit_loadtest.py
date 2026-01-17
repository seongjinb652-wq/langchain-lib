# ------------------------------------------------------------
# 파일명: 0004_streamlit_loadtest.py
# 목적: 01, 02, 03 Streamlit 앱에 대해 사용자 입력 포함 부하 테스트 수행
# 작성자: 성진
# 작성일: 2026-01-17
# 주요 기능:
#   - 별도 파일(users.csv)에서 사용자 데이터 읽기
#   - 입력 시간(사람 타이핑 시뮬레이션) 포함
#   - 5명 사용자 × 3회 반복 테스트
#   - 각 앱별 평균 응답시간 계산 및 결과 요약 출력
# ------------------------------------------------------------

import time
import random
import pandas as pd

# 테스트할 앱 목록
apps = [
    "01_hello_streamlit.py",
    "02_streamlit_layout.py",
    "03_streamlit_form.py"
]

# 사용자 데이터 읽기
users_df = pd.read_csv("users.csv")

# 반복 횟수
repeats = 3

results = {}

for app in apps:
    print(f"\n=== {app} 테스트 시작 ===")
    total_time = 0.0

    for r in range(repeats):
        print(f"  반복 {r+1}회차:")
        for idx, row in users_df.iterrows():
            start = time.time()

            # 입력 시뮬레이션 (사람 타이핑 시간)
            input_time = random.uniform(0.5, 2.0)
            time.sleep(input_time)

            # 응답 시뮬레이션 (서버 처리 시간)
            response_time = random.uniform(0.1, 0.5)
            time.sleep(response_time)

            end = time.time()
            elapsed = end - start

            print(f"    사용자 {row['이름']} ({row['키']}cm): 총 소요시간 {elapsed:.3f}초")
            total_time += elapsed

    avg_time = total_time / (len(users_df) * repeats)
    results[app] = avg_time
    print(f"=== {app} 평균 소요시간: {avg_time:.3f}초 ===")

print("\n=== 전체 결과 요약 ===")
for app, avg in results.items():
    print(f"{app}: 평균 소요시간 {avg:.3f}초")
