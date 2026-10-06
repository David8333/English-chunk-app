import random
from chunks_data import chunks_database
import streamlit as st

# 設定網頁標題與排版
st.set_page_config(
    page_title="10個高頻語塊口說特訓", page_icon="🚀", layout="centered"
)


# 支援語音朗讀的小工具
def speak_text(text, key_suffix=""):
  safe_text = text.replace('"', "'")
  html_code = f"""
    <script>
    function speak_{key_suffix}() {{
        let utterance = new SpeechSynthesisUtterance("{safe_text}");
        utterance.lang = 'en-US';
        utterance.rate = 0.9;
        window.speechSynthesis.speak(utterance);
    }}
    </script>
    <button onclick="speak_{key_suffix}()" style="background-color:#2e7d32; color:white; border:none; padding:6px 14px; border-radius:5px; cursor:pointer; font-weight:bold; font-size:14px;">
        🔊 播放朗讀
    </button>
    """
  st.components.v1.html(html_code, height=45)


st.title("🚀 10個母語人士高頻語塊口說特訓庫")
st.write(
    "專為打造英文流利度設計！本工具透過獨立資料檔載入 10 個高頻語塊與發音功能。"
)

# 初始化 Session 狀態
if "card_index" not in st.session_state:
  st.session_state.card_index = 0
if "is_flipped" not in st.session_state:
  st.session_state.is_flipped = False

# 側邊欄分類導航
st.sidebar.title("🗂️ 語塊導航選單")
category_list = ["全部顯示"] + list(
    set([item["category"] for item in chunks_database])
)
selected_category = st.sidebar.selectbox(
    "選擇練習主題分類：", category_list
)

# 根據分類過濾清單
if selected_category != "全部顯示":
  filtered_db = [
      item for item in chunks_database if item["category"] == selected_category
  ]
else:
  filtered_db = chunks_database

# 確保索引不超過範圍
if st.session_state.card_index >= len(filtered_db):
  st.session_state.card_index = 0

current_data = filtered_db[st.session_state.card_index]

# 主畫面上方進度
st.markdown(
    f"### 📚 學習卡片 ({st.session_state.card_index + 1} /"
    f" {len(filtered_db)})"
)
st.progress((st.session_state.card_index + 1) / len(filtered_db))

# 單字卡主體區
st.markdown("---")
col_cat, col_id = st.columns([3, 1])
with col_cat:
  st.markdown(f"🏷️ **分類主題**：`{current_data['category']}`")
with col_id:
  st.markdown(f"**編號**：#{current_data['id']}")

# 正面：顯示英文語塊
st.markdown(
    "<div style='background-color:#e8f5e9; padding:22px; border-radius:12px;"
    " text-align:center; margin-bottom:15px; border: 1px solid #c8e6c9;'>"
    f"<h2 style='color:#2e7d32; margin:0;'>{current_data['chunk']}</h2>"
    "</div>",
    unsafe_allow_html=True,
)

# 發音按鈕
speak_text(current_data["chunk"], key_suffix=f"main_{current_data['id']}")

st.markdown("---")

# 翻面按鈕邏輯
if st.button(
    "🔄 點擊翻面 / 查看情境與對話", use_container_width=True, type="primary"
):
  st.session_state.is_flipped = not st.session_state.is_flipped

# 如果翻面，顯示詳細中文、情境與自然對話
if st.session_state.is_flipped:
  st.success(f"🇹🇼 **中文解釋**：{current_data['meaning']}")
  st.info(f"💡 **使用情境**：{current_data['scenario']}")

  st.markdown("### 💬 母語情境對話（自然互動）")
  for i, (en_sent, zh_sent) in enumerate(current_data["dialogues"], 1):
    with st.container():
      st.markdown(
          f"<div style='background-color:#f9f9f9; padding:10px;"
          f" border-radius:8px; margin-bottom:8px; border-left:4px solid"
          f" #4caf50;'>"
          f"💬 <b>{en_sent}</b><br><span"
          f" style='color:#666;'>{zh_sent}</span>"
          "</div>",
          unsafe_allow_html=True,
      )
      speak_text(en_sent, key_suffix=f"dlg_{current_data['id']}_{i}")

# 底部切換控制按鈕
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
  if st.button("⬅ 上一張"):
    if st.session_state.card_index > 0:
      st.session_state.card_index -= 1
      st.session_state.is_flipped = False
      st.rerun()

with col2:
  if st.button("🔀 隨機抽卡"):
    st.session_state.card_index = random.randint(0, len(filtered_db) - 1)
    st.session_state.is_flipped = False
    st.rerun()

with col3:
  if st.button("下一張 ➡️"):
    if st.session_state.card_index < len(filtered_db) - 1:
      st.session_state.card_index += 1
      st.session_state.is_flipped = False
      st.rerun()
    else:
      st.success("🎉 太棒了！你已經看完這個分類的所有卡片了！")

st.markdown("---")
st.caption("💡 透過 `from chunks_data import chunks_database` 成功串接！")
