# Streamlit Demo Project

## 프로젝트 개요
재사용이 용이하도록 Streamlit 예제들을 재구성한 프로젝트입니다.  
기본 사용법부터 레이아웃, 입력 폼, 데이터 시각화, 세션 상태 관리, 부하 테스트까지 포함합니다.

## 설치 및 실행 방법
```bash
pip install streamlit pandas
streamlit run <파일명>.py
## 디렉터리 구조
하위 구조 없음.

## 프로젝트 구조
```
streamlit/
├── 01_hello_streamlit.py
├── 02_streamlit_layout.py
├── 03_streamlit_form.py
├── 04_streamlit_dataframe_chart.py
├── 05_streamlit_session_state.py
:
:
├── 
└── README.md
```
```
주요 파일 요약
01_hello_streamlit.py  
기본 사용법 예제 (타이틀, 텍스트 출력, 입력창)

02_streamlit_layout.py  
레이아웃 요소 실습 (섹션, 구분선, 확장탭)

03_streamlit_form.py  
입력 위젯을 활용한 회원가입 폼 (텍스트, 숫자, 선택, 날짜, 파일 업로드, 체크박스)

04_streamlit_dataframe_chart.py  
데이터프레임 표시, 정적 테이블, 난수 기반 Line/Bar 차트 시각화

05_streamlit_session_state.py  
세션 상태 관리 예제 (사용자 입력 유지, 상태 공유)

0004_streamlit_loadtest.py  
사용자 입력 포함 부하 테스트 (users.csv 기반, 타이핑 시뮬레이션, 평균 응답시간 계산)
```
