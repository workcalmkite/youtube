import streamlit as st
import pandas as pd
from youtube_comment_downloader import YoutubeCommentDownloader

st.set_page_config(page_title="유튜브 댓글 분석", page_icon="💬", layout="wide")

st.title("💬 유튜브 댓글 분석")

url = st.text_input("유튜브 링크를 입력하세요")

limit = st.slider("가져올 댓글 개수", 10, 200, 50)

if st.button("댓글 가져오기"):
    if not url:
        st.warning("유튜브 링크를 입력해주세요.")
    else:
        try:
            downloader = YoutubeCommentDownloader()
            comments = downloader.get_comments_from_url(url)

            data = []

            for i, comment in enumerate(comments):
                if i >= limit:
                    break

                data.append({
                    "작성자": comment.get("author", ""),
                    "댓글": comment.get("text", ""),
                    "좋아요": comment.get("votes", ""),
                    "작성시간": comment.get("time", "")
                })

            df = pd.DataFrame(data)

            if df.empty:
                st.warning("댓글을 가져오지 못했습니다.")
            else:
                st.success(f"댓글 {len(df)}개를 가져왔습니다.")
                st.dataframe(df, use_container_width=True)

                csv = df.to_csv(index=False).encode("utf-8-sig")

                st.download_button(
                    label="CSV로 다운로드",
                    data=csv,
                    file_name="youtube_comments.csv",
                    mime="text/csv"
                )

        except Exception as e:
            st.error("댓글을 가져오는 중 오류가 발생했습니다.")
            st.write(e)
