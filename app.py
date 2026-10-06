import random
import streamlit as st

# ============================================================
# 設定網頁
# ============================================================
st.set_page_config(
    page_title="Daily English｜高頻語塊口說特訓",
    page_icon="🚀",
    layout="centered",
)

# ============================================================
# 語音朗讀
# ============================================================
def speak_text(text, key_suffix=""):
    safe_text = (
        text.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", " ")
    )

    html_code = f"""
    <script>
    function speak_{key_suffix}() {{
        let utterance = new SpeechSynthesisUtterance("{safe_text}");
        utterance.lang = 'en-US';
        utterance.rate = 0.9;
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(utterance);
    }}
    </script>

    <button onclick="speak_{key_suffix}()"
        style="
            background-color:#2e7d32;
            color:white;
            border:none;
            padding:6px 14px;
            border-radius:5px;
            cursor:pointer;
            font-weight:bold;
            font-size:14px;
        ">
        🔊 播放朗讀
    </button>
    """
    st.components.v1.html(html_code, height=45)


# ============================================================
# 高頻 Chunk 資料
# 每 3 個 chunks = 一個完整生活 / 職場情境
# ============================================================
chunks_database = [

    # ---------------- Day 1 ----------------
    {
        "day": 1,
        "scenario_title": "下班後約朋友吃飯",
        "category": "日常生活",
        "chunk": "feel like",
        "meaning": "想要、想做某事",
        "usage": "feel like + V-ing / 名詞",
        "challenge": "你今天很累，不太想出去吃飯。",
        "answer": "I don't feel like going out for dinner tonight.",
        "dialogue": [
            ("I'm pretty tired after work.", "我下班後蠻累的。"),
            ("I don't feel like going out for dinner tonight.", "我今晚不太想出去吃飯。"),
            ("Yeah, let's just eat at home.", "好啊，我們就在家吃吧。"),
        ],
    },
    {
        "day": 1,
        "scenario_title": "下班後約朋友吃飯",
        "category": "日常生活",
        "chunk": "I'd rather",
        "meaning": "我寧願……、我比較想……",
        "usage": "I'd rather + 原形動詞",
        "challenge": "你比較想在家吃。",
        "answer": "I'd rather eat at home.",
        "dialogue": [
            ("Do you want to grab something outside?", "你想出去吃點東西嗎？"),
            ("I'd rather eat at home.", "我比較想在家吃。"),
            ("Sounds good to me.", "我覺得可以。"),
        ],
    },
    {
        "day": 1,
        "scenario_title": "下班後約朋友吃飯",
        "category": "日常生活",
        "chunk": "How about",
        "meaning": "……怎麼樣？、要不要……？",
        "usage": "How about + 名詞 / V-ing?",
        "challenge": "你提議叫外送。",
        "answer": "How about ordering delivery?",
        "dialogue": [
            ("What should we eat tonight?", "今晚吃什麼？"),
            ("How about ordering delivery?", "叫外送怎麼樣？"),
            ("Sure. I'm good with that.", "好啊，我可以。"),
        ],
    },

    # ---------------- Day 2 ----------------
    {
        "day": 2,
        "scenario_title": "工作遇到問題",
        "category": "職場英文",
        "chunk": "I'm working on",
        "meaning": "我正在處理／努力做……",
        "usage": "I'm working on + 名詞 / V-ing",
        "challenge": "同事問你報告好了沒，你還在處理。",
        "answer": "I'm still working on the report.",
        "dialogue": [
            ("Is the report ready?", "報告好了嗎？"),
            ("I'm still working on the report.", "我還在處理報告。"),
            ("Okay, just let me know when it's ready.", "好，完成後跟我說一聲。"),
        ],
    },
    {
        "day": 2,
        "scenario_title": "工作遇到問題",
        "category": "職場英文",
        "chunk": "I'm trying to",
        "meaning": "我正在試著……",
        "usage": "I'm trying to + 原形動詞",
        "challenge": "你正在試著找出問題原因。",
        "answer": "I'm trying to figure out what caused the problem.",
        "dialogue": [
            ("Do you know what caused the problem?", "你知道問題是什麼造成的嗎？"),
            ("I'm trying to figure out what caused the problem.", "我正在試著找出問題原因。"),
            ("Let me know if you need any help.", "如果需要幫忙跟我說。"),
        ],
    },
    {
        "day": 2,
        "scenario_title": "工作遇到問題",
        "category": "職場英文",
        "chunk": "figure out",
        "meaning": "弄清楚、找出答案、想辦法解決",
        "usage": "figure out + 問題 / 方法 / 答案",
        "challenge": "你會想辦法解決這個問題。",
        "answer": "I'll figure out how to fix it.",
        "dialogue": [
            ("Can you fix this issue?", "你可以修好這個問題嗎？"),
            ("I'll figure out how to fix it.", "我會想辦法找出怎麼修。"),
            ("Thanks. Keep me posted.", "謝謝，有進度跟我說。"),
        ],
    },

    # ---------------- Day 3 ----------------
    {
        "day": 3,
        "scenario_title": "週末還沒決定",
        "category": "日常生活",
        "chunk": "Are you up for",
        "meaning": "你有沒有興趣／想不想……？",
        "usage": "Are you up for + 名詞 / V-ing?",
        "challenge": "問朋友週末要不要打棒球。",
        "answer": "Are you up for playing baseball this weekend?",
        "dialogue": [
            ("What are you doing this weekend?", "你這週末要做什麼？"),
            ("Are you up for playing baseball?", "你想打棒球嗎？"),
            ("Sure, I'm up for it.", "好啊，我有興趣。"),
        ],
    },
    {
        "day": 3,
        "scenario_title": "週末還沒決定",
        "category": "日常生活",
        "chunk": "play it by ear",
        "meaning": "到時候看情況再決定",
        "usage": "保留彈性、不先做死決定",
        "challenge": "還沒決定週日要去哪裡。",
        "answer": "Let's just play it by ear.",
        "dialogue": [
            ("Where should we go on Sunday?", "星期日要去哪？"),
            ("Let's just play it by ear.", "到時候看情況再決定吧。"),
            ("Sounds good. We'll see how we feel.", "可以，到時候再看。"),
        ],
    },
    {
        "day": 3,
        "scenario_title": "週末還沒決定",
        "category": "日常生活",
        "chunk": "We'll see",
        "meaning": "到時候再看看、再說",
        "usage": "對未確定的事情保持彈性",
        "challenge": "朋友問你星期六一定會不會去。",
        "answer": "We'll see. It depends on the weather.",
        "dialogue": [
            ("Are you definitely coming on Saturday?", "你星期六一定會來嗎？"),
            ("We'll see. It depends on the weather.", "到時候再看看，要看天氣。"),
            ("Okay, just keep me posted.", "好，有變化跟我說。"),
        ],
    },

    # ---------------- Day 4 ----------------
    {
        "day": 4,
        "scenario_title": "臨時忘記一件工作",
        "category": "職場英文",
        "chunk": "It slipped my mind",
        "meaning": "我一時忘記了",
        "usage": "委婉承認忘記某件事",
        "challenge": "你忘了回覆同事的信。",
        "answer": "Sorry, it slipped my mind.",
        "dialogue": [
            ("Did you reply to my email?", "你回我的信了嗎？"),
            ("Sorry, it slipped my mind.", "抱歉，我一時忘記了。"),
            ("No worries. Just get back to me today.", "沒關係，今天回覆我就好。"),
        ],
    },
    {
        "day": 4,
        "scenario_title": "臨時忘記一件工作",
        "category": "職場英文",
        "chunk": "I'll take care of it",
        "meaning": "我會處理好",
        "usage": "表示你會負責把事情處理掉",
        "challenge": "告訴同事這件事你會處理。",
        "answer": "Don't worry. I'll take care of it.",
        "dialogue": [
            ("Who is going to contact the supplier?", "誰要聯絡供應商？"),
            ("Don't worry. I'll take care of it.", "不用擔心，我會處理。"),
            ("Thanks. I appreciate it.", "謝謝，麻煩你了。"),
        ],
    },
    {
        "day": 4,
        "scenario_title": "臨時忘記一件工作",
        "category": "職場英文",
        "chunk": "make sure",
        "meaning": "確保、務必",
        "usage": "make sure + 子句 / make sure to + 原形動詞",
        "challenge": "提醒同事務必確認檔案。",
        "answer": "Make sure to check the file before you send it.",
        "dialogue": [
            ("I'm about to send the file.", "我準備要寄檔案了。"),
            ("Make sure to check it before you send it.", "寄之前務必確認一下。"),
            ("Good point. I'll check it again.", "有道理，我再確認一次。"),
        ],
    },

    # ---------------- Day 5 ----------------
    {
        "day": 5,
        "scenario_title": "工作進度更新",
        "category": "職場英文",
        "chunk": "so far",
        "meaning": "到目前為止",
        "usage": "描述目前累積的進度或結果",
        "challenge": "目前為止一切都很順利。",
        "answer": "Everything is going well so far.",
        "dialogue": [
            ("How's the project going?", "專案進行得如何？"),
            ("Everything is going well so far.", "到目前為止一切都很順利。"),
            ("That's good to hear.", "那很好。"),
        ],
    },
    {
        "day": 5,
        "scenario_title": "工作進度更新",
        "category": "職場英文",
        "chunk": "be on track",
        "meaning": "進度正常、按計畫進行",
        "usage": "The project / schedule / plan is on track.",
        "challenge": "告訴主管專案進度正常。",
        "answer": "The project is still on track.",
        "dialogue": [
            ("Are we still on schedule?", "我們還在原定進度上嗎？"),
            ("Yes, the project is still on track.", "是的，專案進度還正常。"),
            ("Great. Let's keep it moving.", "很好，繼續保持。"),
        ],
    },
    {
        "day": 5,
        "scenario_title": "工作進度更新",
        "category": "職場英文",
        "chunk": "keep me posted",
        "meaning": "有進度再告訴我、隨時更新我",
        "usage": "工作上非常常見的請求",
        "challenge": "請同事有任何進度就告訴你。",
        "answer": "Keep me posted if anything changes.",
        "dialogue": [
            ("I'll talk to the supplier tomorrow.", "我明天會跟供應商談。"),
            ("Okay. Keep me posted if anything changes.", "好，有任何變化跟我說。"),
            ("Sure, I'll keep you posted.", "沒問題，我會跟你更新。"),
        ],
    },
]


# ============================================================
# Session State
# ============================================================
if "day" not in st.session_state:
    st.session_state.day = 1

if "card_index" not in st.session_state:
    st.session_state.card_index = 0

if "is_flipped" not in st.session_state:
    st.session_state.is_flipped = False

if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

if "last_day" not in st.session_state:
    st.session_state.last_day = st.session_state.day


# ============================================================
# 標題
# ============================================================
st.title("🚀 Daily English｜高頻語塊口說特訓庫")

st.write(
    "專為打造英文流利度設計！每天 3 個高頻語塊，放在同一個真實情境中練習。"
)


# ============================================================
# 側邊欄
# ============================================================
st.sidebar.title("🗂️ 學習導航")

day_list = sorted(set(item["day"] for item in chunks_database))

selected_day = st.sidebar.selectbox(
    "選擇學習天數：",
    day_list,
    index=day_list.index(st.session_state.day),
    format_func=lambda x: f"Day {x}",
)

if selected_day != st.session_state.day:
    st.session_state.day = selected_day
    st.session_state.card_index = 0
    st.session_state.is_flipped = False
    st.session_state.show_answer = False
    st.rerun()


category_list = ["全部顯示"] + sorted(
    set(item["category"] for item in chunks_database)
)

selected_category = st.sidebar.selectbox(
    "選擇練習主題分類：",
    category_list,
)

# ============================================================
# 篩選
# ============================================================
day_db = [
    item for item in chunks_database
    if item["day"] == st.session_state.day
]

if selected_category != "全部顯示":
    filtered_db = [
        item for item in day_db
        if item["category"] == selected_category
    ]
else:
    filtered_db = day_db

if not filtered_db:
    st.warning("這個分類目前沒有內容。")
    st.stop()

if st.session_state.card_index >= len(filtered_db):
    st.session_state.card_index = 0

current_data = filtered_db[st.session_state.card_index]


# ============================================================
# 上方進度
# ============================================================
st.markdown(
    f"### 📚 Day {st.session_state.day}｜"
    f"學習卡片 ({st.session_state.card_index + 1} / {len(filtered_db)})"
)

st.progress(
    (st.session_state.card_index + 1) / len(filtered_db)
)

st.markdown(
    f"💬 **今日情境：{current_data['scenario_title']}**"
)

st.markdown("---")


# ============================================================
# 分類與編號
# ============================================================
col_cat, col_id = st.columns([3, 1])

with col_cat:
    st.markdown(
        f"🏷️ **分類主題**：`{current_data['category']}`"
    )

with col_id:
    st.markdown(
        f"**Day {current_data['day']} / #{current_data.get('id', st.session_state.card_index + 1)}**"
    )


# ============================================================
# Chunk 正面
# ============================================================
st.markdown(
    "<div style='background-color:#e8f5e9; padding:22px; "
    "border-radius:12px; text-align:center; margin-bottom:15px; "
    "border:1px solid #c8e6c9;'>"
    f"<h2 style='color:#2e7d32; margin:0;'>{current_data['chunk']}</h2>"
    "</div>",
    unsafe_allow_html=True,
)

speak_text(
    current_data["chunk"],
    key_suffix=f"main_{current_data['day']}_{st.session_state.card_index}",
)

st.markdown("---")


# ============================================================
# 口說挑戰
# ============================================================
st.markdown("### 🎤 口說挑戰")

st.info(
    f"🇹🇼 **情境：** {current_data['challenge']}\n\n"
    "👉 先不要看答案，直接用英文說出來。"
)

if st.button(
    "👀 我說完了，查看自然英文",
    use_container_width=True,
):
    st.session_state.show_answer = True

if st.session_state.show_answer:
    st.success(
        f"🇺🇸 **自然英文：** {current_data['answer']}"
    )
    speak_text(
        current_data["answer"],
        key_suffix=f"answer_{current_data['day']}_{st.session_state.card_index}",
    )

st.markdown("---")


# ============================================================
# 翻面
# ============================================================
if st.button(
    "🔄 點擊翻面 / 查看完整情境對話",
    use_container_width=True,
    type="primary",
):
    st.session_state.is_flipped = not st.session_state.is_flipped


if st.session_state.is_flipped:

    st.success(
        f"🇹🇼 **中文解釋：** {current_data['meaning']}"
    )

    st.info(
        f"💡 **使用方式：** {current_data['usage']}"
    )

    st.markdown("### 💬 母語情境對話")

    for i, (en_sent, zh_sent) in enumerate(
        current_data["dialogue"], 1
    ):
        with st.container():

            st.markdown(
                "<div style='background-color:#f9f9f9; "
                "padding:10px; border-radius:8px; "
                "margin-bottom:8px; border-left:4px solid #4caf50;'>"
                f"💬 <b>{en_sent}</b><br>"
                f"<span style='color:#666;'>{zh_sent}</span>"
                "</div>",
                unsafe_allow_html=True,
            )

            speak_text(
                en_sent,
                key_suffix=(
                    f"dlg_{current_data['day']}_"
                    f"{st.session_state.card_index}_{i}"
                ),
            )


# ============================================================
# 底部控制
# ============================================================
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅️ 上一張", use_container_width=True):

        if st.session_state.card_index > 0:
            st.session_state.card_index -= 1
        else:
            st.session_state.card_index = len(filtered_db) - 1

        st.session_state.is_flipped = False
        st.session_state.show_answer = False
        st.rerun()


with col2:
    if st.button("🔀 隨機抽卡", use_container_width=True):

        st.session_state.card_index = random.randint(
            0, len(filtered_db) - 1
        )

        st.session_state.is_flipped = False
        st.session_state.show_answer = False
        st.rerun()


with col3:
    if st.button("下一張 ➡️", use_container_width=True):

        if st.session_state.card_index < len(filtered_db) - 1:
            st.session_state.card_index += 1
            st.session_state.is_flipped = False
            st.session_state.show_answer = False
            st.rerun()
        else:
            st.success(
                "🎉 今天 3 個 chunks 都完成了！"
            )


# ============================================================
# 今日學習提示
# ============================================================
st.markdown("---")

st.caption(
    "💡 建議：先看中文情境 → 自己說英文 → 查看答案 → 聽朗讀 → 再看完整對話。"
)

st.caption(
    "🚀 每天只練 3 個 chunks，不求一次背很多，重點是能真的說出口。"
)
