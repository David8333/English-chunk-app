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
# 高頻 Chunk 資料 (總計 18 天，共 54 個 Chunks)
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

    # ---------------- Day 6 ----------------
    {
        "day": 6,
        "scenario_title": "餐廳點餐與推薦",
        "category": "日常生活",
        "chunk": "recommend",
        "meaning": "推薦、建議",
        "usage": "recommend + 名詞 / V-ing",
        "challenge": "請服務生推薦招牌菜。",
        "answer": "What do you recommend on the menu?",
        "dialogue": [
            ("Are you ready to order?", "準備好點餐了嗎？"),
            ("Not yet. What do you recommend on the menu?", "還沒。你們有推薦什麼嗎？"),
            ("Our grilled salmon is very popular.", "我們的烤鮭魚非常受歡迎。"),
        ],
    },
    {
        "day": 6,
        "scenario_title": "餐廳點餐與推薦",
        "category": "日常生活",
        "chunk": "I'll go with",
        "meaning": "我決定要……（點餐或選擇時常用）",
        "usage": "I'll go with + 選擇的項目",
        "challenge": "告訴服務生你決定點烤鮭魚。",
        "answer": "I'll go with the grilled salmon.",
        "dialogue": [
            ("Have you decided what to eat?", "決定好要吃什麼了嗎？"),
            ("Yes, I'll go with the grilled salmon.", "對，我決定點烤鮭魚。"),
            ("Got it. Would you like anything to drink?", "知道了。需要來點飲料嗎？"),
        ],
    },
    {
        "day": 6,
        "scenario_title": "餐廳點餐與推薦",
        "category": "日常生活",
        "chunk": "on the side",
        "meaning": "（醬料或配菜）另外裝、放旁邊",
        "usage": "某物 + on the side",
        "challenge": "要求沙拉醬另外放。",
        "answer": "Can I have the dressing on the side?",
        "dialogue": [
            ("Would you like dressing on your salad?", "沙拉要加醬嗎？"),
            ("Yes, but can I have the dressing on the side?", "要，不過可以把沙拉醬另外放嗎？"),
            ("No problem at all.", "沒問題。"),
        ],
    },

    # ---------------- Day 7 ----------------
    {
        "day": 7,
        "scenario_title": "會議中表達意見",
        "category": "職場英文",
        "chunk": "I'm of the opinion that",
        "meaning": "我認為……、我的看法是……",
        "usage": "I'm of the opinion that + 子句",
        "challenge": "在會議中表達你認為應該延後截止日。",
        "answer": "I'm of the opinion that we should extend the deadline.",
        "dialogue": [
            ("What do you think about the schedule?", "你覺得這個時程怎麼樣？"),
            ("I'm of the opinion that we should extend the deadline.", "我認為我們應該延長截止期限。"),
            ("That's an interesting point.", "這是一個有趣的觀點。"),
        ],
    },
    {
        "day": 7,
        "scenario_title": "會議中表達意見",
        "category": "職場英文",
        "chunk": "from my perspective",
        "meaning": "從我的角度來看",
        "usage": "From my perspective, + 子句",
        "challenge": "從你的角度來看，成本太高了。",
        "answer": "From my perspective, the cost is too high.",
        "dialogue": [
            ("Do you think we should buy this software?", "你覺得我們應該買這套軟體嗎？"),
            ("From my perspective, the cost is too high.", "從我的角度來看，成本太高了。"),
            ("I see your point. Let's reconsider.", "我懂你的意思。我們重新考慮一下。"),
        ],
    },
    {
        "day": 7,
        "scenario_title": "會議中表達意見",
        "category": "職場英文",
        "chunk": "I see your point",
        "meaning": "我懂你的意思／我理解你的看法",
        "usage": "表贊同或理解對方立場時的開頭",
        "challenge": "告訴同事你理解他的考量。",
        "answer": "I see your point, but we have to move faster.",
        "dialogue": [
            ("We shouldn't rush this launch.", "我們不該急著推出。"),
            ("I see your point, but we have to move faster.", "我懂你的意思，但我們必須動作快一點。"),
            ("Fair enough.", "也是有道理。"),
        ],
    },

    # ---------------- Day 8 ----------------
    {
        "day": 8,
        "scenario_title": "機場報到與託運",
        "category": "旅遊英文",
        "chunk": "Here is my",
        "meaning": "這我的……（拿證件給地勤或海關時說）",
        "usage": "Here is my + 護照／機票",
        "challenge": "把護照拿給地勤人員。",
        "answer": "Here is my passport and boarding pass.",
        "dialogue": [
            ("May I see your passport, please?", "請出示您的護照？"),
            ("Sure. Here is my passport and boarding pass.", "好的。這是我的護照和登機證。"),
            ("Thank you. Where are you flying to today?", "謝謝您。您今天要飛往哪裡？"),
        ],
    },
    {
        "day": 8,
        "scenario_title": "機場報到與託運",
        "category": "旅遊英文",
        "chunk": "carry-on baggage",
        "meaning": "隨身行李",
        "usage": "詢問或說明隨身行李限制",
        "challenge": "詢問這是否能當作隨身行李。",
        "answer": "Can I bring this bag as carry-on baggage?",
        "dialogue": [
            ("Is this suitcase going to be checked?", "這咖行李箱要託運嗎？"),
            ("No, can I bring this bag as carry-on baggage?", "不，我可以把這袋子當隨身行李帶上機嗎？"),
            ("Yes, as long as it fits in the overhead bin.", "可以，只要放得進上方置物櫃。"),
        ],
    },
    {
        "day": 8,
        "scenario_title": "機場報到與託運",
        "category": "旅遊英文",
        "chunk": "window or aisle",
        "meaning": "靠窗還是靠走道",
        "usage": "選擇機位時的固定問法",
        "challenge": "告訴地勤你想坐靠走道的位子。",
        "answer": "I'd prefer an aisle seat, please.",
        "dialogue": [
            ("Would you prefer a window or aisle seat?", "您想要靠窗還是靠走道的座位？"),
            ("I'd prefer an aisle seat, please.", "我比較想坐靠走道，謝謝。"),
            ("Got it. Here is your seat assignment.", "了解。這是您的座位。"),
        ],
    },

    # ---------------- Day 9 ----------------
    {
        "day": 9,
        "scenario_title": "飯店Check-in與詢問",
        "category": "旅遊英文",
        "chunk": "I have a reservation",
        "meaning": "我有預約／訂房",
        "usage": "I have a reservation under the name of + 姓名",
        "challenge": "告訴櫃檯你有用王小明名字訂房。",
        "answer": "I have a reservation under the name of Wang.",
        "dialogue": [
            ("Good afternoon. How can I help you?", "午安，有什麼需要協助的嗎？"),
            ("Hi, I have a reservation under the name of Wang.", "嗨，我有預約，名字是王。"),
            ("Let me check that for you.", "我幫您查一下。"),
        ],
    },
    {
        "day": 9,
        "scenario_title": "飯店Check-in與詢問",
        "category": "旅遊英文",
        "chunk": "Is breakfast included",
        "meaning": "有包含早餐嗎？",
        "usage": "Is breakfast included in the room rate?",
        "challenge": "詢問櫃檯房費是否包含早餐。",
        "answer": "Is breakfast included in the price?",
        "dialogue": [
            ("Here is your room key.", "這是您的房卡。"),
            ("Quick question, is breakfast included?", "順帶問一下，有包含早餐嗎？"),
            ("Yes, it's served from 7 to 10 AM at the restaurant.", "有的，早上 7 點到 10 點在餐廳供應。"),
        ],
    },
    {
        "day": 9,
        "scenario_title": "飯店Check-in與詢問",
        "category": "旅遊英文",
        "chunk": "What time is checkout",
        "meaning": "幾點退房？",
        "usage": "What time is checkout time?",
        "challenge": "詢問退房時間是幾點。",
        "answer": "What time is checkout tomorrow?",
        "dialogue": [
            ("Enjoy your stay!", "祝您住宿愉快！"),
            ("Thank you. What time is checkout tomorrow?", "謝謝。明天退房時間是幾點？"),
            ("Checkout is at 11 AM.", "退房時間是早上 11 點。"),
        ],
    },

    # ---------------- Day 10 ----------------
    {
        "day": 10,
        "scenario_title": "請求同事協助",
        "category": "職場英文",
        "chunk": "Do you have a second",
        "meaning": "你現在有空嗎？／你有幾秒鐘嗎？",
        "usage": "Do you have a second to talk?",
        "challenge": "問同事現在有沒有空講話。",
        "answer": "Do you have a second to look at this?",
        "dialogue": [
            ("Hi Mark, do you have a second?", "嗨 Mark，你現在有空嗎？"),
            ("Sure, what's up?", "可以啊，怎麼了？"),
            ("I need your advice on this email.", "這封信我想聽聽你的建議。"),
        ],
    },
    {
        "day": 10,
        "scenario_title": "請求同事協助",
        "category": "職場英文",
        "chunk": "Could you do me a favor",
        "meaning": "可以幫我一個忙嗎？",
        "usage": "Could you do me a favor and + 原形動詞",
        "challenge": "請同事幫忙看一下翻譯有沒有問題。",
        "answer": "Could you do me a favor and check this translation?",
        "dialogue": [
            ("Are you super busy right now?", "你現在超忙嗎？"),
            ("Not really. Could you do me a favor and check this translation?", "還好。可以幫我看一下這段翻譯嗎？"),
            ("No problem, let me see.", "沒問題，我看看。"),
        ],
    },
    {
        "day": 10,
        "scenario_title": "請求同事協助",
        "category": "職場英文",
        "chunk": "I'd really appreciate it",
        "meaning": "我會非常感激",
        "usage": "表示強烈的感謝與請求",
        "challenge": "告訴同事如果他能幫忙，你會非常感激。",
        "answer": "If you could help me with this, I'd really appreciate it.",
        "dialogue": [
            ("I can help you review this report.", "我可以幫你審閱這份報告。"),
            ("If you could help me with this, I'd really appreciate it.", "如果你能幫忙這個，我會非常感激。"),
            ("Don't mention it. Glad to help.", "別客氣，很高興能幫忙。"),
        ],
    },

    # ---------------- Day 11 ----------------
    {
        "day": 11,
        "scenario_title": "表達同意與贊同",
        "category": "社交對話",
        "chunk": "I couldn't agree more",
        "meaning": "我完全同意",
        "usage": "強烈表贊同對方的觀點",
        "challenge": "完全同意朋友說今天天氣真好。",
        "answer": "I couldn't agree more. It's a gorgeous day.",
        "dialogue": [
            ("This coffee shop has such a nice vibe.", "這家咖啡廳氛圍真好。"),
            ("I couldn't agree more. It's a gorgeous day.", "我完全同意。今天天氣真棒。"),
            ("We should come here more often.", "我們應該常來這裡。"),
        ],
    },
    {
        "day": 11,
        "scenario_title": "表達同意與贊同",
        "category": "社交對話",
        "chunk": "You can say that again",
        "meaning": "說得真對、完全沒錯（慣用語）",
        "usage": "用來強烈附和對方的話",
        "challenge": "附和同事說這項工作真的讓人壓力很大。",
        "answer": "You can say that again. I'm exhausted.",
        "dialogue": [
            ("This project is driving me crazy.", "這個專案快把我逼瘋了。"),
            ("You can say that again. I'm exhausted.", "說得真對，我都快累死了。"),
            ("Let's take a break.", "我們休息一下吧。"),
        ],
    },
    {
        "day": 11,
        "scenario_title": "表達同意與贊同",
        "category": "社交對話",
        "chunk": "That's so true",
        "meaning": "真的一點也沒錯",
        "usage": "自然且道地的日常同意說法",
        "challenge": "附和朋友說時間過得真快。",
        "answer": "That's so true. Time flies.",
        "dialogue": [
            ("I can't believe it's already December.", "真不敢相信已經 12 月了。"),
            ("That's so true. Time flies.", "真的一點也沒錯，時間過得真快。"),
            ("A whole year has passed.", "一整年就這樣過去了。"),
        ],
    },

    # ---------------- Day 12 ----------------
    {
        "day": 12,
        "scenario_title": "表達不確定或保留意見",
        "category": "日常與職場",
        "chunk": "I'm not so sure about",
        "meaning": "我對……不太確定／有點保留",
        "usage": "I'm not so sure about + 名詞 / V-ing",
        "challenge": "你對這個新計畫不太確定。",
        "answer": "I'm not so sure about this new plan.",
        "dialogue": [
            ("What do you think of the new strategy?", "你覺得這個新策略怎麼樣？"),
            ("I'm not so sure about this new plan.", "我對這個新計畫有點不太確定。"),
            ("Why? Do you see any risks?", "為什麼？你看到什麼風險嗎？"),
        ],
    },
    {
        "day": 12,
        "scenario_title": "表達不確定或保留意見",
        "category": "日常與職場",
        "chunk": "It depends",
        "meaning": "這要看情況",
        "usage": "當答案不是絕對時的標準回答",
        "challenge": "回答朋友明天要不要去爬山要看天氣。",
        "answer": "It depends on the weather.",
        "dialogue": [
            ("Are we going hiking tomorrow?", "我們明天要去爬山嗎？"),
            ("It depends on the weather.", "這要看天氣而定。"),
            ("Hope it doesn't rain.", "希望不要下雨。"),
        ],
    },
    {
        "day": 12,
        "scenario_title": "表達不確定或保留意見",
        "category": "日常與職場",
        "chunk": "I have mixed feelings about",
        "meaning": "我對……感到有些矛盾／百感交集",
        "usage": "I have mixed feelings about + 事物",
        "challenge": "你對要搬到外地工作這件事心情很矛盾。",
        "answer": "I have mixed feelings about moving to another city.",
        "dialogue": [
            ("Are you excited about the relocation?", "你對調職感到興奮嗎？"),
            ("I have mixed feelings about moving to another city.", "要搬到另一個城市，我心情其實滿矛盾的。"),
            ("I understand. It's a big change.", "我理解，這是一個大改變。"),
        ],
    },

    # ---------------- Day 13 ----------------
    {
        "day": 13,
        "scenario_title": "購物與詢問價格、尺寸",
        "category": "日常生活",
        "chunk": "Do you have this in",
        "meaning": "這個有沒有……尺寸／顏色？",
        "usage": "Do you have this in + 尺寸或顏色?",
        "challenge": "問店員這件衣服有沒有中號（Medium）。",
        "answer": "Do you have this in a medium?",
        "dialogue": [
            ("Can I help you find something?", "需要幫忙找什麼嗎？"),
            ("Yes, I like this jacket. Do you have this in a medium?", "對，我喜歡這件夾克。這件有中號嗎？"),
            ("Let me check the back storage for you.", "我幫您去後方倉庫查一下。"),
        ],
    },
    {
        "day": 13,
        "scenario_title": "購物與詢問價格、尺寸",
        "category": "日常生活",
        "chunk": "Can I try this on",
        "meaning": "我可以試穿這個嗎？",
        "usage": "Can I try this on?",
        "challenge": "詢問店員是否可以試穿這件褲子。",
        "answer": "Can I try these pants on?",
        "dialogue": [
            ("These pants look great.", "這件褲子看起來很好看。"),
            ("Can I try these pants on?", "我可以試穿這件褲子嗎？"),
            ("Of course, the fitting rooms are over there.", "當然可以，試衣間在那邊。"),
        ],
    },
    {
        "day": 13,
        "scenario_title": "購物與詢問價格、尺寸",
        "category": "日常生活",
        "chunk": "I'm just looking",
        "meaning": "我只是隨便看看",
        "usage": "逛街時不想被推銷的標準回答",
        "challenge": "告訴店員你只是隨便看看。",
        "answer": "Thanks, I'm just looking around.",
        "dialogue": [
            ("Hi there, looking for anything specific?", "嗨，有在找什麼特定的東西嗎？"),
            ("No thanks, I'm just looking around.", "不用了謝謝，我只是隨便看看。"),
            ("Let me know if you need any assistance.", "有需要協助隨時跟我說。"),
        ],
    },

    # ---------------- Day 14 ----------------
    {
        "day": 14,
        "scenario_title": "交通問路與求助",
        "category": "旅遊英文",
        "chunk": "How do I get to",
        "meaning": "我要怎麼去……？",
        "usage": "How do I get to + 地點?",
        "challenge": "問路人要怎麼去最近的地鐵站。",
        "answer": "Excuse me, how do I get to the nearest subway station?",
        "dialogue": [
            ("Excuse me, how do I get to the nearest subway station?", "不好意思，請問我要怎麼去最近的地鐵站？"),
            ("Go straight down this street and turn left.", "沿著這條街直走然後左轉。"),
            ("Thank you so much!", "非常謝謝你！"),
        ],
    },
    {
        "day": 14,
        "scenario_title": "交通問路與求助",
        "category": "旅遊英文",
        "chunk": "Is it far from here",
        "meaning": "離這裡遠嗎？",
        "usage": "Is it far from here?",
        "challenge": "詢問目的地離這裡遠不遠。",
        "answer": "Is the museum far from here?",
        "dialogue": [
            ("I want to visit the national museum.", "我想去參觀國家博物館。"),
            ("Is the museum far from here?", "博物館離這裡遠嗎？"),
            ("Not really, it's about a ten-minute walk.", "不遠，走路大概十分鐘。"),
        ],
    },
    {
        "day": 14,
        "scenario_title": "交通問路與求助",
        "category": "旅遊英文",
        "chunk": "Which way is",
        "meaning": "哪裡是……的方向？／往哪走？",
        "usage": "Which way is + 地點?",
        "challenge": "詢問出口在哪個方向。",
        "answer": "Excuse me, which way is the exit?",
        "dialogue": [
            ("Excuse me, which way is the exit?", "不好意思，請問出口往哪走？"),
            ("Head towards the food court and you'll see it.", "往美食街的方向走就會看到了。"),
            ("Got it, appreciate it.", "了解，謝謝。"),
        ],
    },

    # ---------------- Day 15 ----------------
    {
        "day": 15,
        "scenario_title": "表達感謝與回應",
        "category": "社交對話",
        "chunk": "I really appreciate your help",
        "meaning": "我真的很感謝你的幫忙",
        "usage": "正式且誠懇的道謝方式",
        "challenge": "向幫你大忙的朋友表達謝意。",
        "answer": "I really appreciate your help today.",
        "dialogue": [
            ("Did you finish moving the boxes?", "箱子搬完了嗎？"),
            ("Yes, thanks to you. I really appreciate your help today.", "搬完了，多虧有你。我真的非常感謝你今天的幫忙。"),
            ("Anytime! Glad I could help.", "隨時都可以！很高興能幫忙。"),
        ],
    },
    {
        "day": 15,
        "scenario_title": "表達感謝與回應",
        "category": "社交對話",
        "chunk": "Don't mention it",
        "meaning": "別客氣、不足掛齒",
        "usage": "當別人對你說謝謝時的回應",
        "challenge": "當同事跟你道謝時，回答「別客氣」。",
        "answer": "Don't mention it. It was no big deal.",
        "dialogue": [
            ("Thanks for covering my shift yesterday.", "謝謝你昨天幫我代班。"),
            ("Don't mention it. It was no big deal.", "別客氣，這沒什麼大不了的。"),
            ("You're a lifesaver.", "你真是我的救星。"),
        ],
    },
    {
        "day": 15,
        "scenario_title": "表達感謝與回應",
        "category": "社交對話",
        "chunk": "It's the least I could do",
        "meaning": "這是我應該做的（微不足道的事）",
        "usage": "謙虛地回應別人的感謝",
        "challenge": "回答「這是我微不足道的心意／應該做的」。",
        "answer": "It's the least I could do after all your help.",
        "dialogue": [
            ("Thank you so much for the dinner treat.", "非常謝謝你請吃晚餐。"),
            ("It's the least I could do after all your help.", "這是我之前受你幫忙、最少該做的事了。"),
            ("That's very kind of you.", "你人真好。"),
        ],
    },

    # ---------------- Day 16 ----------------
    {
        "day": 16,
        "scenario_title": "電話與視訊會議開場",
        "category": "職場英文",
        "chunk": "Can you hear me clearly",
        "meaning": "你們聽得清楚我說話嗎？",
        "usage": "視訊或電話會議開始時的標準問句",
        "challenge": "開會時問大家聽不聽得到你說話。",
        "answer": "Hi everyone, can you hear me clearly?",
        "dialogue": [
            ("Hi everyone, can you hear me clearly?", "嗨大家好，你們聽得清楚我說話嗎？"),
            ("Yes, loud and clear.", "聽得到，聲音很清楚。"),
            ("Great, let's get started.", "很好，那我們開始吧。"),
        ],
    },
    {
        "day": 16,
        "scenario_title": "電話與視訊會議開場",
        "category": "職場英文",
        "chunk": "I'll share my screen",
        "meaning": "我要分享我的畫面了",
        "usage": "線上會議中準備簡報時常用",
        "challenge": "告訴大家你要分享螢幕畫面。",
        "answer": "I'll share my screen with you now.",
        "dialogue": [
            ("Are you ready to show the slides?", "準備好展示投影片了嗎？"),
            ("Yes, I'll share my screen with you now.", "準備好了，我現在要把畫面分享給各位。"),
            ("Take your time.", "請慢慢來。"),
        ],
    },
    {
        "day": 16,
        "scenario_title": "電話與視訊會議開場",
        "category": "職場英文",
        "chunk": "Let's move on to",
        "meaning": "接下來我們進入到……、我們來看下一個……",
        "usage": "Let's move on to + 下一個主題",
        "challenge": "在會議中提議進入下一個議程。",
        "answer": "If there are no other questions, let's move on to the next topic.",
        "dialogue": [
            ("We've discussed the budget.", "我們已經討論過預算。"),
            ("If there are no other questions, let's move on to the next topic.", "如果沒有其他問題，我們進入下一個主題吧。"),
            ("Sounds good. Let's proceed.", "好的，請繼續。"),
        ],
    },

    # ---------------- Day 17 ----------------
    {
        "day": 17,
        "scenario_title": "提出建議與邀約",
        "category": "日常生活",
        "chunk": "Why don't we",
        "meaning": "我們何不……呢？",
        "usage": "Why don't we + 原形動詞?",
        "challenge": "提議週末一起去喝杯咖啡。",
        "answer": "Why don't we grab some coffee this weekend?",
        "dialogue": [
            ("Are you free this weekend?", "你這週末有空嗎？"),
            ("Why don't we grab some coffee this weekend?", "我們這週末去喝杯咖啡怎麼樣？"),
            ("I'd love that! What time?", "我很樂意！幾點？"),
        ],
    },
    {
        "day": 17,
        "scenario_title": "提出建議與邀約",
        "category": "日常生活",
        "chunk": "Count me in",
        "meaning": "算我一份！",
        "usage": "當聽到有趣的活動時熱情答應",
        "challenge": "聽到大家要去唱歌，立刻說算我一份。",
        "answer": "That sounds fun. Count me in!",
        "dialogue": [
            ("We're planning a karaoke night on Friday.", "我們計畫禮拜五去唱KTV。"),
            ("That sounds fun. Count me in!", "聽起來很好玩，算我一份！"),
            ("Awesome, the more the better.", "太棒了，人越多越好。"),
        ],
    },
    {
        "day": 17,
        "scenario_title": "提出建議與邀約",
        "category": "日常生活",
        "chunk": "Maybe next time",
        "meaning": "或許下次吧（婉拒邀約）",
        "usage": "無法參加活動時的禮貌拒絕",
        "challenge": "因為今天有事，禮貌跟朋友說下次再約。",
        "answer": "I have to pass tonight, but maybe next time.",
        "dialogue": [
            ("Do you want to join us for a movie?", "你要一起去看電影嗎？"),
            ("I have to pass tonight, but maybe next time.", "我今晚得婉拒了，不過或許下次吧。"),
            ("No worries, another time!", "沒關係，改天囉！"),
        ],
    },

    # ---------------- Day 18 ----------------
    {
        "day": 18,
        "scenario_title": "表達歉意與解釋",
        "category": "日常與職場",
        "chunk": "I apologize for",
        "meaning": "我為……感到抱歉",
        "usage": "I apologize for + 名詞 / V-ing (較正式的道歉)",
        "challenge": "為今天的遲到向主管道歉。",
        "answer": "I apologize for being late this morning.",
        "dialogue": [
            ("You were a bit late to the morning meeting.", "你今天早會稍微遲到了點。"),
            ("I apologize for being late this morning. The traffic was terrible.", "我為今早遲到感到抱歉，交通狀況太糟了。"),
            ("Try to leave earlier next time.", "下次試著早點出門。"),
        ],
    },
    {
        "day": 18,
        "scenario_title": "表達歉意與解釋",
        "category": "日常與職場",
        "chunk": "It was my fault",
        "meaning": "這是我的錯、我該負責任",
        "usage": "主動承擔錯誤時的直白說法",
        "challenge": "大方承認錯誤，說這件事是你的疏忽。",
        "answer": "It was my fault. I misread the schedule.",
        "dialogue": [
            ("Why did we miss the deadline?", "為什麼我們會錯過期限？"),
            ("It was my fault. I misread the schedule.", "這是我的錯，我看錯時程表了。"),
            ("Let's figure out how to fix it together.", "我們一起想辦法解決吧。"),
        ],
    },
    {
        "day": 18,
        "scenario_title": "表達歉意與解釋",
        "category": "日常與職場",
        "chunk": "I'll make sure it doesn't happen again",
        "meaning": "我保證這種事不會再發生了",
        "usage": "出錯後向對方做出承諾",
        "challenge": "向主管保證下次不會再犯同樣的錯。",
        "answer": "I'll make sure it doesn't happen again.",
        "dialogue": [
            ("Please double-check your work next time.", "下次請確實雙重確認你的工作。"),
            ("Understood. I'll make sure it doesn't happen again.", "知道了，我保證這種事不會再發生。"),
            ("Okay, I trust you.", "好，我相信你。"),
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
