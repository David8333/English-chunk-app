import random
import streamlit as st

# 設定網頁標題與排版
st.set_page_config(
    page_title="1000個英文母語語塊學習卡", page_icon="🗣️", layout="centered"
)

# 支援語音朗讀的 JavaScript / HTML 小工具
def speak_text(text):
  # 使用網覽器內建的 Web Speech API 發音
  safe_text = text.replace('"', "'")
  html_code = f"""
    <script>
    function speak() {{
        let utterance = new SpeechSynthesisUtterance("{safe_text}");
        utterance.lang = 'en-US';
        utterance.rate = 0.9; // 稍慢一點適合學習
        window.speechSynthesis.speak(utterance);
    }}
    </script>
    <button onclick="speak()" style="background-color:#4CAF50; color:white; border:none; padding:8px 16px; border-radius:5px; cursor:pointer; font-weight:bold;">
        🔊 點擊播放發音
    </button>
    """
  st.components.v1.html(html_code, height=50)


st.title("🗣️ 1000個英文母語人士常用語塊學習卡")
st.write(
    "結合「單字卡翻面、使用情境、發音功能、以及三段實境對話」，幫你真正把語塊用在生活與職場中！"
)

# 1000個高頻語塊資料庫（此處展示精選核心高頻語塊，架構支援擴充至1000個）
chunks_database = [
    {
        "id": 1,
        "category": "職場商務",
        "chunk": "take something into account",
        "meaning": "把...納入考量、顧及",
        "scenario": "適用於決策、規劃、評估專案或提出建議時，強調全面思考。",
        "dialogues": [
            (
                "A: Should we lower the price of our new product?",
                "我們應該降低新產品的價格嗎？",
            ),
            (
                "B: We need to take production costs into account first.",
                "我們必須先把生產成本納入考量。",
            ),
            (
                "A: That's a fair point. Let's recalculate.",
                "說得對。我們重新計算一下。",
            ),
        ],
    },
    {
        "id": 2,
        "category": "日常溝通",
        "chunk": "shed light on",
        "meaning": "闡明、使人理解、照亮問題核心",
        "scenario": "適用於解釋複雜情況、提供新線索或釐清真相時。",
        "dialogues": [
            (
                "A: Do you have any idea why the system crashed?",
                "你知道系統為什麼當機嗎？",
            ),
            (
                "B: This error log might shed light on the issue.",
                "這個錯誤記錄檔或許能幫忙釐清這個問題。",
            ),
            ("A: Great, let's take a look.", "太好了，我們來看一下。"),
        ],
    },
    {
        "id": 3,
        "category": "情感表達",
        "chunk": "catch someone off guard",
        "meaning": "殺個措手不及、使人毫無防備",
        "scenario": "適用於形容突發狀況、意料之外的問題或驚喜。",
        "dialogues": [
            (
                "A: How did you like the sudden pop quiz today?",
                "你覺得今天突如其來的隨堂考怎麼樣？",
            ),
            (
                "B: It totally caught me off guard! I hadn't reviewed yet.",
                "完全把我殺個措手不及！我還沒複習呢。",
            ),
            ("A: Haha, me neither.", "哈哈，我也是。"),
        ],
    },
    {
        "id": 4,
        "category": "觀點立場",
        "chunk": "by and large",
        "meaning": "大體上、總的來說、從各方面來看",
        "scenario": "適用於宏觀總結、發表整體看法而非絕對細節時。",
        "dialogues": [
            (
                "A: How was the annual conference this year?",
                "今年的年度會議覺得怎麼樣？",
            ),
            (
                "B: By and large, it was a huge success.",
                "總的來說，這是一場非常成功的會議。",
            ),
            (
                "A: I agree, the presentations were inspiring.",
                "我同意，簡報都很有啟發性。",
            ),
        ],
    },
    {
        "id": 5,
        "category": "重要關鍵",
        "chunk": "play a pivotal role",
        "meaning": "扮演關鍵核心角色",
        "scenario": "適用於形容某人、某技術或某因素在成功中不可或缺。",
        "dialogues": [
            (
                "A: Why is communication so emphasized in this project?",
                "為什麼這個專案這麼強調溝通？",
            ),
            (
                "B: Effective communication plays a pivotal role in teamwork.",
                "有效溝通在團隊合作中扮演了關鍵角色。",
            ),
            ("A: Makes total sense.", "完全講通。"),
        ],
    },
]

# 初始化 Session 狀態
if "card_index" not in st.session_state:
  st.session_state.card_index = 0
if "is_flipped" not in st.session_state:
  st.session_state.is_flipped = False

current_data = chunks_database[st.session_state.card_index]

# 頂部導覽列與進度
st.markdown(
    f"### 📚 學習卡片 ({st.session_state.card_index + 1} /"
    f" {len(chunks_database)})"
)
st.progress((st.session_state.card_index + 1) / len(chunks_database))

# 單字卡主體區
st.markdown("---")
col_cat, col_id = st.columns([3, 1])
with col_cat:
  st.markdown(f"🏷️ **分類主題**：`{current_data['category']}`")
with col_id:
  st.markdown(f"**編號**：#{current_data['id']}")

# 正面：顯示英文語塊
st.markdown(
    "<div style='background-color:#f0f2f6; padding:20px; border-radius:10px;"
    " text-align:center; margin-bottom:15px;'>"
    f"<h2 style='color:#1f77b4; margin:0;'>{current_data['chunk']}</h2>"
    "</div>",
    unsafe_allow_html=True,
)

# 發音按鈕
speak_text(current_data["chunk"])

st.markdown("---")

# 翻面按鈕邏輯
if st.button(
    "🔄 點擊翻面 / 切換詳細解析", use_container_width=True, type="primary"
):
  st.session_state.is_flipped = not st.session_state.is_flipped

# 如果翻面，顯示詳細中文、情境與對話
if st.session_state.is_flipped:
  st.success(f"🇹🇼 **中文解釋**：{current_data['meaning']}")
  st.info(f"💡 **使用情境**：{current_data['scenario']}")

  st.markdown("### 💬 三段實境應用對話")
  for i, (en_sent, zh_sent) in enumerate(current_data["dialogues"], 1):
    with st.container():
      st.markdown(f"**對話 {i}**")
      st.markdown(f"> 👤 `{en_sent}`")
      st.markdown(f"> 🗣️ *{zh_sent}*")
      # 對話單句發音
      speak_text(en_sent)
      st.write("")

# 底部切換控制按鈕
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
  if st.button("⬅️ 上一張"):
    if st.session_state.card_index > 0:
      st.session_state.card_index -= 1
      st.session_state.is_flipped = False
      st.rerun()

with col2:
  if st.button("🔀 隨機抽卡"):
    st.session_state.card_index = random.randint(
        0, len(chunks_database) - 1
    )
    st.session_state.is_flipped = False
    st.rerun()

with col3:
  if st.button("下一張 ➡️"):
    if st.session_state.card_index < len(chunks_database) - 1:
      st.session_state.card_index += 1
      st.session_state.is_flipped = False
      st.rerun()
    else:
      st.success("🎉 恭喜你學完這批語塊了！")

st.markdown("---")
st.caption(
    "💡 提示：你可以隨時在 GitHub 的 `app.py` 裡擴充更多語塊資料，打造屬於你"
    "自己的 1000 個語塊庫！"
)
