import random
import streamlit as st

# 設定網頁標題與排版
st.set_page_config(
    page_title="母語人士高頻語塊特訓", page_icon="🔥", layout="centered"
)


# 支援語音朗讀的 JavaScript / HTML 小工具
def speak_text(text):
  safe_text = text.replace('"', "'")
  html_code = f"""
    <script>
    function speak() {{
        let utterance = new SpeechSynthesisUtterance("{safe_text}");
        utterance.lang = 'en-US';
        utterance.rate = 0.9;
        window.speechSynthesis.speak(utterance);
    }}
    </script>
    <button onclick="speak()" style="background-color:#2e7d32; color:white; border:none; padding:6px 14px; border-radius:5px; cursor:pointer; font-weight:bold; font-size:14px;">
        🔊 播放朗讀
    </button>
    """
  st.components.v1.html(html_code, height=45)


st.title("🔥 母語人士高頻語塊口說特訓")
st.write(
    "背單字不如背語塊！以下收錄真正影響英文流利度的道地組合，點擊按鈕還能直接聽母語發音與情境對話。"
)

# 高頻核心語塊資料庫（精選道地、口說絕對會用到的語塊）
chunks_database = [
    {
        "id": 1,
        "category": "強烈認同 / 附和",
        "chunk": "tell me about it",
        "meaning": "可不是嗎、說得太對了、我超懂這種感覺",
        "scenario": "當別人抱怨或說中你的心聲時，比說 'I agree' 道地一百倍。",
        "dialogues": [
            (
                "Traffic is absolute nightmare this morning.",
                "今早的交通簡直是場惡夢。",
            ),
            (
                "Tell me about it! I was stuck for over an hour.",
                "可不是嗎！我卡了一個多小時。",
            ),
            ("I'm definitely taking the subway tomorrow.", "我明天絕對要改搭地鐵。"),
        ],
    },
    {
        "id": 2,
        "category": "坦承 / 說實話",
        "chunk": "to be honest with you",
        "meaning": "老實跟你說、坦白講",
        "scenario": "準備發表真心話、給予誠實建議或稍微反駁時的常用開場白。",
        "dialogues": [
            ("Do you think my new haircut looks okay?", "你覺得我新剪的頭髮好看嗎？"),
            (
                "To be honest with you, it's a bit too short on the sides.",
                "老實跟你說，兩側真的剪得有點太短了。",
            ),
            ("Ah, well, hair grows back!", "啊，好吧，頭髮會再長長嘛！"),
        ],
    },
    {
        "id": 3,
        "category": "狀況外 / 沒聽清楚",
        "chunk": "slip one's mind",
        "meaning": "一時忘記、腦袋當機沒想起來",
        "scenario": "忘記某件事時，用來委婉表達「我不是故意忘記的」。",
        "dialogues": [
            ("Did you send the report to the boss?", "你有把報告寄給老闆嗎？"),
            (
                "Oh no! It completely slipped my mind. I'll do it right now.",
                "糟糕！我完全忘得精光。我馬上處理。",
            ),
            ("Hurry up before she asks about it.", "趁她問起之前快點。"),
        ],
    },
    {
        "id": 4,
        "category": "隨性 / 看情況",
        "chunk": "play it by ear",
        "meaning": "走一步算一步、看情況再決定",
        "scenario": "當行程或計畫還沒定案，想保留彈性時使用。",
        "dialogues": [
            ("What's the plan for this Saturday?", "這禮拜六有什麼計畫？"),
            (
                "We haven't booked anything yet. Let's just play it by ear.",
                "我們還沒訂位。到時候看狀況再決定吧。",
            ),
            ("Sounds good, let me know.", "聽起來不錯，再跟我說。"),
        ],
    },
    {
        "id": 5,
        "category": "打圓場 / 緩解尷尬",
        "chunk": "break the ice",
        "meaning": "破冰、打破僵局",
        "scenario": "在陌生場合、聚會開頭或會議剛開始時炒熱氣氛。",
        "dialogues": [
            (
                "Everyone was so quiet when the meeting started.",
                "會議剛開始時大家安靜得可怕。",
            ),
            (
                "Fortunately, John told a funny joke to break the ice.",
                "幸好約翰講了一個好笑的笑話來破冰。",
            ),
            ("That really saved the atmosphere.", "那真的拯救了整個氣氛。"),
        ],
    },
    {
        "id": 6,
        "category": "形容麻煩 / 找罪受",
        "chunk": "go out of one's way",
        "meaning": "特地、格外費心去幫忙或做事",
        "scenario": "用來稱讚某人特別熱心，或表達自己為某事付出了額外心力。",
        "dialogues": [
            ("Thank you so much for picking me up at the station.", "太謝謝你特地去車站接我了。"),
            (
                "No problem at all. I didn't mind going out of my way.",
                "完全沒問題。我一點也不介意特地跑一趟。",
            ),
            ("I really appreciate your kindness.", "我很感激你的好意。"),
        ],
    },
    {
        "id": 7,
        "category": "應付 / 勉強過得去",
        "chunk": "make ends meet",
        "meaning": "勉強維持生計、收支打平",
        "scenario": "討論生活開銷、經濟壓力或物價上漲時非常道地的說法。",
        "dialogues": [
            (
                "With the rent going up, it's getting harder to live here.",
                "隨著房租上漲，在這裡生活越來越不容易了。",
            ),
            (
                "Yeah, working two jobs is the only way to make ends meet.",
                "對啊，打兩份工是勉強維持生計的唯一辦法。",
            ),
            ("Inflation is really hurting everyone.", "通膨真的在傷害每個人。"),
        ],
    },
    {
        "id": 8,
        "category": "關鍵轉折 / 話鋒一轉",
        "chunk": "at the end of the day",
        "meaning": "到頭來、說到底、歸根結底",
        "scenario": "在經歷一連串討論後，準備做最後總結或點出核心本質時使用。",
        "dialogues": [
            (
                "We had so many arguments about the marketing strategy.",
                "我們針對行銷策略爭論了超多次。",
            ),
            (
                "At the end of the day, customer satisfaction matters most.",
                "說到底，客戶滿意度才是最重要的。",
            ),
            ("I completely agree with that conclusion.", "我完全同意這個結論。"),
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
    "<div style='background-color:#e8f5e9; padding:22px; border-radius:12px;"
    " text-align:center; margin-bottom:15px; border: 1px solid #c8e6c9;'>"
    f"<h2 style='color:#2e7d32; margin:0;'>{current_data['chunk']}</h2>"
    "</div>",
    unsafe_allow_html=True,
)

# 發音按鈕
speak_text(current_data["chunk"])

st.markdown("---")

# 翻面按鈕邏輯
if st.button(
    "🔄 點擊翻面 / 查看情境與對話", use_container_width=True, type="primary"
):
  st.session_state.is_flipped = not st.session_state.is_flipped

# 如果翻面，顯示詳細中文、情境與對話（無 A/B 標註）
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
      speak_text(en_sent)

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
      st.success("🎉 太棒了！你已經看完這組高頻語塊了！")

st.markdown("---")
st.caption(
    "💡 小撇步：這套架構讓您可以隨時在 GitHub 的 `app.py` 中複製貼上新增更多"
    "語塊，想擴充到 300 或 1000 個都可以自己掌控！"
)
