import streamlit as st

st.set_page_config(
    page_title="Portal Game Kelas 5B",
    page_icon="🎮",
    layout="centered"
)

st.title("🎮 Portal Game Kelas 5B")
st.write("Silakan pilih game untuk dimainkan")

st.markdown("---")

# Tombol Game
if st.button("🟢 Main Game GemKite"):
    st.markdown(
        "[Klik di sini untuk membuka GemKite](https://www.bookwidgets.com/play/7KpXqRU_-iQAFBfhvoQAAA/VHLBQV3?teacher_id=6130752844726272)",
        unsafe_allow_html=True
    )

if st.button("🟡 Main Game Puzzle"):
    st.markdown(
        "[Klik di sini untuk membuka Game Puzzle](https://www.bookwidgets.com/play/3ehwm0fQ-iQAFB43MYQAAA/2HLFS2K?teacher_id=6130752844726272)",
        unsafe_allow_html=True
    )

st.markdown("---")
st.caption("© Kelas 5B")
