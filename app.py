import random
import streamlit as st

st.set_page_config(
    page_title="英文語塊學習小工具", page_icon="🧩", layout="centered"
)

st.title("🧩 英文語塊 (Chunks) 學習小工具")
st.write(
    "背單字不如背「語塊」！語塊是母語人士習慣成群使用的字詞組合。請根據提示填入缺少的語塊。"
)

chunks_data = [
    {
        "chunk": "take into account",
        "meaning": "把...考慮進去、顧及",
        "sentence": "We must _______ all the factors before making a decision.",
    },
    {
        "chunk": "shed light on",
        "meaning": "闡明、使人理解、照亮",
        "sentence": "The new evidence helped to _______ the mystery.",
    },
    {
        "chunk": "by and large",
        "meaning": "大體上、總的來說",
        "sentence": "_______, it was a successful event.",
    },
    {
        "chunk": "play a pivotal role",
        "meaning": "扮演關鍵角色",
        "sentence": "Technology tends to _______ in modern education.",
    },
    {
        "chunk": "catch someone off guard",
        "meaning": "殺個措手不及、使人毫無防備",
        "sentence": "The sudden question managed to _______ her _______.",
    },
]

if "index" not in st.session_state:
  st.session_state.index = 0
if "score" not in st.session_state:
  st.session_state.score = 0

current_item = chunks_data[st.session_state.index]

st.markdown("---")
st.subheader(f"第 {st.session_state.index + 1} 題 / 共 {len(chunks_data)} 題")
st.info(f"💡 **中文意思**：{current_item['meaning']}")
st.markdown(f"**例句練習**：`{current_item['sentence']}`")

with st.form(key=f"form_{st.session_state.index}"):
  user_answer = st.text_input(
      "請輸入正確的英文語塊或缺空字詞："
  ).strip()
  submit_btn = st.form_submit_button("提交答案")

  if submit_btn:
    if (
        user_answer.lower() in current_item["chunk"].lower()
        and len(user_answer) > 2
    ):
      st.success(
          f"答對了！🎉 完整的正確語塊是：**{current_item['chunk']}**"
      )
      st.session_state.score += 1
    else:
      st.error(
          f"答錯囉！正確的語塊應為：**{current_item['chunk']}**"
      )

col1, col2 = st.columns(2)
with col1:
  if st.button("下一題"):
    if st.session_state.index < len(chunks_data) - 1:
      st.session_state.index += 1
      st.rerun()
    else:
      st.warning("已經是最後一題囉！")

with col2:
  if st.button("重新開始"):
    st.session_state.index = 0
    st.session_state.score = 0
    st.rerun()

st.markdown("---")
st.write(f"目前累計得分：**{st.session_state.score}** 分")
