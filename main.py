import streamlit as st

st.set_page_config(
    page_title="유튜브 댓글 분석 앱",
    page_icon="💬",
    layout="wide"
)

st.title("💬 유튜브 댓글 분석 앱")

st.markdown("""
## 유튜브 링크를 넣으면 댓글을 볼 수 있는 앱입니다.

왼쪽 메뉴에서 원하는 기능을 선택하세요.

### 메뉴
- 💬 유튜브 댓글 분석
- 🔍 댓글 검색
- 🏆 댓글 순위
- 📘 사용 방법
""")

st.info("왼쪽 사이드바에서 페이지를 선택하세요.")
