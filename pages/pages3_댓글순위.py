import streamlit as st
import pandas as pd
from youtube_comment_downloader import YoutubeCommentDownloader

st.title("🏆 댓글 좋아요 순위")

url = st.text_input("유튜브 링크를 입력하세요")
limit = st.slider("가져올 댓글 개수", 10, 300, 100)

def vote_to_number(vote):
    try:
        vote = str(vote).replace(",", "").replace("좋아요", "").strip()
        if "K" in vote:
            return int(float(vote.replace("K", "")) * 1000)
        return int(vote)
    except:
        return 0

if st.button("순위 보기"):
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

                votes = comment.get("votes", "0")

                data.append({
                    "작성자": comment.get("author", ""),
                    "댓글": comment.get("text", ""),
                    "좋아요": votes,
                    "좋아요수": vote_to_number(votes),
                    "작성시간": comment.get("time", "")
                })

            df = pd.DataFrame(data)

            df = df.sort_values(by="좋아요수", ascending=False)

            st.success("좋아요가 많은 댓글 순위입니다.")
            st.dataframe(
                df[["작성자", "댓글", "좋아요", "작성시간"]],
                use_container_width=True
            )

        except Exception as e:
            st.error("오류가 발생했습니다.")
            st.write(e)
