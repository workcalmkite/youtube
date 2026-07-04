import streamlit as st
import pandas as pd
from youtube_comment_downloader import YoutubeCommentDownloader

st.title("🔍 댓글 검색")

url = st.text_input("유튜브 링크를 입력하세요")
keyword = st.text_input("검색할 단어를 입력하세요")
limit = st.slider("가져올 댓글 개수", 10, 300, 100)

if st.button("검색하기"):
    if not url or not keyword:
        st.warning("유튜브 링크와 검색어를 모두 입력해주세요.")
    else:
        try:
            downloader = YoutubeCommentDownloader()
            comments = downloader.get_comments_from_url(url)

            data = []

            for i, comment in enumerate(comments):
                if i >= limit:
                    break

                text = comment.get("text", "")

                if keyword in text:
                    data.append({
                        "작성자": comment.get("author", ""),
                        "댓글": text,
                        "좋아요": comment.get("votes", ""),
                        "작성시간": comment.get("time", "")
                    })

            df = pd.DataFrame(data)

            st.success(f"'{keyword}'가 들어간 댓글 {len(df)}개를 찾았습니다.")
            st.dataframe(df, use_container_width=True)

        except Exception as e:
            st.error("오류가 발생했습니다.")
            st.write(e)
