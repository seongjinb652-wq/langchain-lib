## 프로젝트 개요 : 재사용 용이하도록 streamlit 재구성
## 설치/실행 방법 : streamlit run   xxxxx.py
## 디렉터리 구조 : 하위 구조 없음.
## 주요 기능 요약 : 파일명 일치.
## 프로젝트 구조
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

## 파일명: 01_hello_streamlit.py
- 목적: Streamlit 기본 사용법 
- 실행: streamlit run 01_hello_streamlit.py
- 주요 기능: 타이틀, 텍스트 출력, 입력창

## 파일명: 02_streamlit_layout.py
- 목적: Streamlit 레이아웃 요소 실습 (섹션, 구분선, 확장탭)
- 실행: streamlit run 02_streamlit_layout.py
- 작성자: 성진
- 작성일: 2026-01-17
- 주요 기능:
-   - st.header()로 섹션 구분
-   - st.divider() / st.markdown("---")로 구분선 추가
-   - st.expander()로 접히는 영역 구현
## 파일명: 03_streamlit_form.py
- 목적: Streamlit 입력 위젯을 활용한 회원가입 폼 구현
- 작성자: 성진
- 작성일: 2026-01-17
- 주요 기능:
-   - 텍스트 입력 (이름, 자기소개)
-   - 숫자 입력 (나이, 키)
-   - 선택 요소 (성별, 좋아하는 색상, 관심사)
-   - 날짜 입력 (생일)
-   - 파일 업로드 (프로필 사진)
-   - 체크박스 및 버튼 (약관 동의, 회원가입)
