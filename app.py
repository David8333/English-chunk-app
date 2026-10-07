import random
import streamlit as st

# =========================================================
# 頁面設定
# =========================================================
st.set_page_config(
    page_title="Daily English｜高頻語塊口說特訓",
    page_icon="🚀",
    layout="centered"
)


# =========================================================
# 語音功能
# =========================================================
def speak_text(text, key_suffix=""):
    safe_text = text.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ")

    html = f"""
    <script>
    function speak_{key_suffix}() {{
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance('{safe_text}');
        utterance.lang = 'en-US';
        utterance.rate = 0.9;
        window.speechSynthesis.speak(utterance);
    }}
    </script>

    <button
        onclick="speak_{key_suffix}()"
        style="
            border: none;
            background-color: #f0f2f6;
            border-radius: 8px;
            padding: 5px 10px;
            cursor: pointer;
            font-size: 14px;
        "
    >
        🔊 聽發音
    </button>
    """

    st.components.v1.html(html, height=45)


# =========================================================
# 54 個核心 Chunk
# 每天 3 個，共 18 天
# =========================================================
chunks_database = [

    # =====================================================
    # Day 1
    # =====================================================
    {
        "day": 1,
        "scenario_title": "下班後約朋友吃飯",
        "category": "日常社交",
        "chunk": "feel like",
        "meaning": "想要／想做某事",
        "usage": "feel like + V-ing / 名詞",
        "challenge": "你今晚想出去吃飯嗎？",
        "answer": "Do you feel like going out for dinner tonight?",
        "supplement": [
            "Do you want to...?",
            "I'm in the mood for..."
        ],
        "dialogue": [
            ("Do you feel like going out for dinner tonight?", "你今晚想出去吃飯嗎？"),
            ("I don't really feel like cooking.", "我不太想煮飯。"),
            ("How about trying that new restaurant?", "去試試那間新餐廳如何？")
        ]
    },

    {
        "day": 1,
        "scenario_title": "下班後約朋友吃飯",
        "category": "日常社交",
        "chunk": "I'd rather",
        "meaning": "我寧願／我比較想",
        "usage": "I'd rather + 原形動詞",
        "challenge": "我今晚比較想待在家裡。",
        "answer": "I'd rather stay home tonight.",
        "supplement": [
            "I'd prefer to...",
            "I'd rather not..."
        ],
        "dialogue": [
            ("Do you want to eat out tonight?", "你今晚想出去吃嗎？"),
            ("I'd rather stay home tonight.", "我今晚比較想待在家裡。"),
            ("That's fine with me.", "我沒問題。")
        ]
    },

    {
        "day": 1,
        "scenario_title": "下班後約朋友吃飯",
        "category": "日常社交",
        "chunk": "How about",
        "meaning": "……如何？／要不要……？",
        "usage": "How about + 名詞 / V-ing",
        "challenge": "吃火鍋如何？",
        "answer": "How about having hot pot?",
        "supplement": [
            "What about...?",
            "Why don't we...?"
        ],
        "dialogue": [
            ("How about having hot pot?", "吃火鍋如何？"),
            ("Sounds good to me.", "我覺得不錯。"),
            ("Let's do that.", "就吃那個吧。")
        ]
    },

    # =====================================================
    # Day 2
    # =====================================================
    {
        "day": 2,
        "scenario_title": "工作遇到問題",
        "category": "職場",
        "chunk": "I'm working on",
        "meaning": "我正在處理／進行",
        "usage": "I'm working on + 名詞",
        "challenge": "我正在處理這個問題。",
        "answer": "I'm working on this issue.",
        "supplement": [
            "I'm dealing with...",
            "I'm handling..."
        ],
        "dialogue": [
            ("How's the report going?", "報告進度如何？"),
            ("I'm working on it right now.", "我現在正在處理。"),
            ("I'll send it to you when it's ready.", "完成後我會寄給你。")
        ]
    },

    {
        "day": 2,
        "scenario_title": "工作遇到問題",
        "category": "職場",
        "chunk": "I'm trying to",
        "meaning": "我正在試著／努力",
        "usage": "I'm trying to + 原形動詞",
        "challenge": "我正在試著找出問題。",
        "answer": "I'm trying to figure out the problem.",
        "supplement": [
            "I'm doing my best to...",
            "I'm working on..."
        ],
        "dialogue": [
            ("What's the problem?", "問題是什麼？"),
            ("I'm trying to figure it out.", "我正在試著弄清楚。"),
            ("I'll let you know when I know more.", "有更多資訊我會告訴你。")
        ]
    },

    {
        "day": 2,
        "scenario_title": "工作遇到問題",
        "category": "職場",
        "chunk": "figure out",
        "meaning": "弄清楚／找出解決方法",
        "usage": "figure out + 問題／方法",
        "challenge": "我們需要找出發生什麼事。",
        "answer": "We need to figure out what happened.",
        "supplement": [
            "find out",
            "work out"
        ],
        "dialogue": [
            ("Do you know what's wrong?", "你知道哪裡有問題嗎？"),
            ("Not yet. I'm trying to figure it out.", "還不知道，我正在試著弄清楚。"),
            ("Let's figure it out together.", "我們一起找出原因吧。")
        ]
    },

    # =====================================================
    # Day 3
    # =====================================================
    {
        "day": 3,
        "scenario_title": "週末還沒決定",
        "category": "日常社交",
        "chunk": "Are you up for",
        "meaning": "你有興趣／想要……嗎？",
        "usage": "Are you up for + 名詞 / V-ing",
        "challenge": "你週末想去看電影嗎？",
        "answer": "Are you up for going to a movie this weekend?",
        "supplement": [
            "Do you feel like...?",
            "Are you interested in...?"
        ],
        "dialogue": [
            ("Are you up for going to a movie this weekend?", "你週末想去看電影嗎？"),
            ("Maybe. I'm not sure yet.", "也許吧，我還不確定。"),
            ("We'll see.", "到時候再看看。")
        ]
    },

    {
        "day": 3,
        "scenario_title": "週末還沒決定",
        "category": "日常社交",
        "chunk": "play it by ear",
        "meaning": "到時候再看／隨機應變",
        "usage": "play it by ear",
        "challenge": "我們先不要決定，到時候再看看。",
        "answer": "Let's just play it by ear.",
        "supplement": [
            "We'll see how it goes.",
            "Let's see what happens."
        ],
        "dialogue": [
            ("Do we need to make plans now?", "我們現在需要先安排嗎？"),
            ("Not really. Let's just play it by ear.", "不用，我們到時候再看看。"),
            ("Sounds good.", "好啊。")
        ]
    },

    {
        "day": 3,
        "scenario_title": "週末還沒決定",
        "category": "日常社交",
        "chunk": "We'll see",
        "meaning": "到時候再看看",
        "usage": "用於不確定的回答",
        "challenge": "你週末會去嗎？到時候再看看。",
        "answer": "Will you go this weekend? We'll see.",
        "supplement": [
            "I'm not sure yet.",
            "I haven't decided yet."
        ],
        "dialogue": [
            ("Are you going to the party?", "你會去派對嗎？"),
            ("We'll see.", "到時候再看看。"),
            ("Okay, just let me know.", "好，有決定再告訴我。")
        ]
    },

    # =====================================================
    # Day 4
    # =====================================================
    {
        "day": 4,
        "scenario_title": "臨時忘記一件工作",
        "category": "職場",
        "chunk": "It slipped my mind",
        "meaning": "我一時忘了",
        "usage": "It slipped my mind.",
        "challenge": "抱歉，我一時忘了。",
        "answer": "Sorry, it slipped my mind.",
        "supplement": [
            "I forgot about it.",
            "It completely slipped my mind."
        ],
        "dialogue": [
            ("Did you send the file?", "你把檔案寄了嗎？"),
            ("Sorry, it slipped my mind.", "抱歉，我一時忘了。"),
            ("I'll send it right away.", "我馬上寄。")
        ]
    },

    {
        "day": 4,
        "scenario_title": "臨時忘記一件工作",
        "category": "職場",
        "chunk": "I'll take care of it",
        "meaning": "我會處理／我來處理",
        "usage": "I'll take care of + 名詞",
        "challenge": "沒問題，我來處理。",
        "answer": "No problem. I'll take care of it.",
        "supplement": [
            "I'll handle it.",
            "I've got it."
        ],
        "dialogue": [
            ("Can you take care of this?", "你可以處理這個嗎？"),
            ("Sure. I'll take care of it.", "當然，我來處理。"),
            ("Thanks, I appreciate it.", "謝謝，我很感謝。")
        ]
    },

    {
        "day": 4,
        "scenario_title": "臨時忘記一件工作",
        "category": "職場",
        "chunk": "make sure",
        "meaning": "確保／確認",
        "usage": "make sure + 子句 / to V",
        "challenge": "請確認你有寄給客戶。",
        "answer": "Make sure you send it to the customer.",
        "supplement": [
            "double-check",
            "be sure to..."
        ],
        "dialogue": [
            ("Is the file ready?", "檔案好了嗎？"),
            ("Almost. I'll make sure everything is correct.", "差不多了，我會確認全部都正確。"),
            ("Great.", "很好。")
        ]
    },

    # =====================================================
    # Day 5
    # =====================================================
    {
        "day": 5,
        "scenario_title": "工作進度更新",
        "category": "職場",
        "chunk": "so far",
        "meaning": "到目前為止",
        "usage": "放在句尾或句中",
        "challenge": "到目前為止，一切都很順利。",
        "answer": "Everything is going well so far.",
        "supplement": [
            "up to now",
            "at this point"
        ],
        "dialogue": [
            ("How's the project going?", "專案進度如何？"),
            ("Everything is going well so far.", "到目前為止都很順利。"),
            ("That's good to hear.", "那很好。")
        ]
    },

    {
        "day": 5,
        "scenario_title": "工作進度更新",
        "category": "職場",
        "chunk": "keep me posted",
        "meaning": "隨時告訴我最新進度",
        "usage": "keep me posted on + 名詞",
        "challenge": "有任何進展請告訴我。",
        "answer": "Keep me posted on any updates.",
        "supplement": [
            "Let me know if anything changes.",
            "Keep me updated."
        ],
        "dialogue": [
            ("I'll check with the customer.", "我會跟客戶確認。"),
            ("Okay. Keep me posted.", "好，有進度告訴我。"),
            ("Sure, I will.", "好的。")
        ]
    },

    {
        "day": 5,
        "scenario_title": "工作進度更新",
        "category": "職場",
        "chunk": "I'm running late",
        "meaning": "我晚到了／我會遲到",
        "usage": "I'm running late + for...",
        "challenge": "抱歉，我今天上班會遲到。",
        "answer": "Sorry, I'm running late this morning.",
        "supplement": [
            "I'm going to be late.",
            "I got held up."
        ],
        "dialogue": [
            ("Are you on your way?", "你在路上了嗎？"),
            ("Yes, but I'm running late.", "有，但我會晚到。"),
            ("No worries. Take your time.", "沒關係，慢慢來。")
        ]
    },

    # =====================================================
    # Day 6
    # =====================================================
    {
        "day": 6,
        "scenario_title": "餐廳點餐與推薦",
        "category": "餐廳",
        "chunk": "What do you recommend?",
        "meaning": "你推薦什麼？",
        "usage": "詢問餐廳推薦",
        "challenge": "你推薦這裡吃什麼？",
        "answer": "What do you recommend here?",
        "supplement": [
            "What's good here?",
            "What do you usually get?"
        ],
        "dialogue": [
            ("What do you recommend here?", "你推薦這裡吃什麼？"),
            ("The steak is really good.", "牛排很好吃。"),
            ("Okay, I'll go with the steak.", "好，那我點牛排。")
        ]
    },

    {
        "day": 6,
        "scenario_title": "餐廳點餐與推薦",
        "category": "餐廳",
        "chunk": "I'll go with",
        "meaning": "我就選／我要點",
        "usage": "I'll go with + 名詞",
        "challenge": "那我就點牛肉麵。",
        "answer": "I'll go with the beef noodles.",
        "supplement": [
            "I'll have...",
            "I'll take..."
        ],
        "dialogue": [
            ("What are you getting?", "你要點什麼？"),
            ("I'll go with the beef noodles.", "我就點牛肉麵。"),
            ("Good choice.", "不錯的選擇。")
        ]
    },

    {
        "day": 6,
        "scenario_title": "餐廳點餐與推薦",
        "category": "餐廳",
        "chunk": "on the side",
        "meaning": "另外放／另外提供",
        "usage": "點餐時要求醬料等另外放",
        "challenge": "醬汁請另外放。",
        "answer": "Can I get the sauce on the side?",
        "supplement": [
            "Could I get...?",
            "Can I have...?"
        ],
        "dialogue": [
            ("What would you like?", "你想要什麼？"),
            ("I'll have the salad with the dressing on the side.", "我要沙拉，醬汁另外放。"),
            ("Sure.", "好的。")
        ]
    },

    # =====================================================
    # Day 7
    # =====================================================
    {
        "day": 7,
        "scenario_title": "會議中表達意見",
        "category": "職場會議",
        "chunk": "I think",
        "meaning": "我認為／我覺得",
        "usage": "I think + 子句",
        "challenge": "我覺得我們應該再確認一次。",
        "answer": "I think we should double-check it.",
        "supplement": [
            "I don't think...",
            "I think we should..."
        ],
        "dialogue": [
            ("What do you think?", "你覺得呢？"),
            ("I think we should double-check it.", "我覺得我們應該再確認一次。"),
            ("That makes sense.", "有道理。")
        ]
    },

    {
        "day": 7,
        "scenario_title": "會議中表達意見",
        "category": "職場會議",
        "chunk": "The way I see it",
        "meaning": "依我看／照我的看法",
        "usage": "The way I see it, + 子句",
        "challenge": "依我看，我們有兩個選擇。",
        "answer": "The way I see it, we have two options.",
        "supplement": [
            "As I see it...",
            "From what I can see..."
        ],
        "dialogue": [
            ("How should we handle this?", "我們應該怎麼處理？"),
            ("The way I see it, we have two options.", "依我看，我們有兩個選擇。"),
            ("Let's talk about both options.", "我們來討論兩個選項。")
        ]
    },

    {
        "day": 7,
        "scenario_title": "會議中表達意見",
        "category": "職場會議",
        "chunk": "I see your point",
        "meaning": "我懂你的意思／我理解你的觀點",
        "usage": "用於表示理解對方觀點",
        "challenge": "我懂你的意思，但我還是不同意。",
        "answer": "I see your point, but I still disagree.",
        "supplement": [
            "I understand what you mean.",
            "I get what you're saying."
        ],
        "dialogue": [
            ("I think we should wait.", "我覺得我們應該等等。"),
            ("I see your point, but we need to move forward.", "我懂你的意思，但我們需要繼續往前。"),
            ("That's fair.", "這有道理。")
        ]
    },

    # =====================================================
    # Day 8
    # =====================================================
    {
        "day": 8,
        "scenario_title": "機場報到與託運",
        "category": "旅遊",
        "chunk": "I'd like to check in",
        "meaning": "我想辦理報到",
        "usage": "機場／飯店都可使用",
        "challenge": "我想辦理登機報到。",
        "answer": "I'd like to check in for my flight.",
        "supplement": [
            "I'm here to check in.",
            "I'd like to check in."
        ],
        "dialogue": [
            ("Good morning. How can I help you?", "早安，有什麼可以幫您？"),
            ("I'd like to check in for my flight.", "我想辦理登機報到。"),
            ("May I see your passport?", "可以看一下您的護照嗎？")
        ]
    },

    {
        "day": 8,
        "scenario_title": "機場報到與託運",
        "category": "旅遊",
        "chunk": "carry-on",
        "meaning": "隨身行李",
        "usage": "carry-on bag / carry-on luggage",
        "challenge": "這個可以當隨身行李嗎？",
        "answer": "Can I take this as a carry-on?",
        "supplement": [
            "checked baggage",
            "check this bag"
        ],
        "dialogue": [
            ("Do you have any bags to check?", "你有行李要託運嗎？"),
            ("No, I only have a carry-on.", "沒有，我只有隨身行李。"),
            ("Okay, you're all set.", "好的，都辦好了。")
        ]
    },

    {
        "day": 8,
        "scenario_title": "機場報到與託運",
        "category": "旅遊",
        "chunk": "window or aisle",
        "meaning": "靠窗還是靠走道",
        "usage": "window seat / aisle seat",
        "challenge": "我想要靠窗的位置。",
        "answer": "I'd like a window seat, please.",
        "supplement": [
            "middle seat",
            "an aisle seat"
        ],
        "dialogue": [
            ("Would you like a window or aisle seat?", "您想要靠窗還是靠走道？"),
            ("I'd like a window seat, please.", "我想要靠窗的位置。"),
            ("Sure. Let me check.", "好的，我幫您確認。")
        ]
    },

    # =====================================================
    # Day 9
    # =====================================================
    {
        "day": 9,
        "scenario_title": "飯店 Check-in 與詢問",
        "category": "旅遊",
        "chunk": "I have a reservation",
        "meaning": "我有預訂",
        "usage": "I have a reservation under + 姓名",
        "challenge": "我有預訂，名字是 Chen。",
        "answer": "I have a reservation under the name Chen.",
        "supplement": [
            "I booked a room.",
            "I made a reservation."
        ],
        "dialogue": [
            ("Welcome. How can I help you?", "歡迎，有什麼可以幫您？"),
            ("I have a reservation under the name Chen.", "我有預訂，名字是 Chen。"),
            ("Sure. May I see your ID?", "好的，可以看一下您的證件嗎？")
        ]
    },

    {
        "day": 9,
        "scenario_title": "飯店 Check-in 與詢問",
        "category": "旅遊",
        "chunk": "Is breakfast included?",
        "meaning": "早餐有包含嗎？",
        "usage": "詢問房價是否包含早餐",
        "challenge": "請問早餐有包含嗎？",
        "answer": "Is breakfast included?",
        "supplement": [
            "Does the room include breakfast?",
            "Is breakfast included in the price?"
        ],
        "dialogue": [
            ("Is breakfast included?", "早餐有包含嗎？"),
            ("Yes, it's included.", "有，包含在裡面。"),
            ("Great. What time is breakfast?", "太好了，早餐幾點開始？")
        ]
    },

    {
        "day": 9,
        "scenario_title": "飯店 Check-in 與詢問",
        "category": "旅遊",
        "chunk": "What time do I need to check out?",
        "meaning": "我需要幾點退房？",
        "usage": "詢問退房時間",
        "challenge": "我需要幾點退房？",
        "answer": "What time do I need to check out?",
        "supplement": [
            "What time is check-out?",
            "When do I need to check out?"
        ],
        "dialogue": [
            ("What time do I need to check out?", "我需要幾點退房？"),
            ("Check-out is at 11 a.m.", "退房時間是早上 11 點。"),
            ("Got it. Thanks.", "了解，謝謝。")
        ]
    },

    # =====================================================
    # Day 10
    # =====================================================
    {
        "day": 10,
        "scenario_title": "請求同事協助",
        "category": "職場",
        "chunk": "Do you have a second?",
        "meaning": "你有空一下嗎？",
        "usage": "禮貌地詢問對方是否有空",
        "challenge": "你現在有空一下嗎？",
        "answer": "Do you have a second?",
        "supplement": [
            "Do you have a minute?",
            "Are you free for a minute?"
        ],
        "dialogue": [
            ("Do you have a second?", "你有空一下嗎？"),
            ("Sure. What's up?", "有啊，怎麼了？"),
            ("I need your help with something.", "我需要你幫我一件事。")
        ]
    },

    {
        "day": 10,
        "scenario_title": "請求同事協助",
        "category": "職場",
        "chunk": "Could you do me a favor?",
        "meaning": "可以幫我一個忙嗎？",
        "usage": "Could you do me a favor and + V",
        "challenge": "可以幫我一個忙嗎？",
        "answer": "Could you do me a favor?",
        "supplement": [
            "Could you help me with...?",
            "Would you mind...?"
        ],
        "dialogue": [
            ("Could you do me a favor?", "可以幫我一個忙嗎？"),
            ("Sure. What do you need?", "當然，你需要什麼？"),
            ("Could you check this file for me?", "可以幫我確認這個檔案嗎？")
        ]
    },

    {
        "day": 10,
        "scenario_title": "請求同事協助",
        "category": "職場",
        "chunk": "I'd really appreciate it",
        "meaning": "我會非常感謝",
        "usage": "用於禮貌地表達感謝",
        "challenge": "如果你能幫忙，我會非常感謝。",
        "answer": "I'd really appreciate it if you could help.",
        "supplement": [
            "That would be a big help.",
            "Thanks, I really appreciate it."
        ],
        "dialogue": [
            ("Could you send me the file?", "你可以把檔案寄給我嗎？"),
            ("Sure.", "可以。"),
            ("I'd really appreciate it.", "我會非常感謝。")
        ]
    },

    # =====================================================
    # Day 11
    # =====================================================
    {
        "day": 11,
        "scenario_title": "表達同意與贊同",
        "category": "日常社交",
        "chunk": "I couldn't agree more",
        "meaning": "我完全同意",
        "usage": "強烈表示同意",
        "challenge": "我完全同意你的看法。",
        "answer": "I couldn't agree more.",
        "supplement": [
            "Absolutely.",
            "I totally agree."
        ],
        "dialogue": [
            ("We need to get more sleep.", "我們需要多睡一點。"),
            ("I couldn't agree more.", "我完全同意。"),
            ("I'm always tired these days.", "我最近總是很累。")
        ]
    },

    {
        "day": 11,
        "scenario_title": "表達同意與贊同",
        "category": "日常社交",
        "chunk": "You can say that again",
        "meaning": "你說得太對了",
        "usage": "強烈同意對方說法",
        "challenge": "最近真的很忙。你說得太對了。",
        "answer": "You can say that again.",
        "supplement": [
            "Tell me about it.",
            "I know what you mean."
        ],
        "dialogue": [
            ("Work has been crazy lately.", "最近工作真的很瘋狂。"),
            ("You can say that again.", "你說得太對了。"),
            ("I can't wait for the weekend.", "我等不及週末了。")
        ]
    },

    {
        "day": 11,
        "scenario_title": "表達同意與贊同",
        "category": "日常社交",
        "chunk": "That's so true",
        "meaning": "真的很對／確實如此",
        "usage": "自然地表示認同",
        "challenge": "你說得沒錯。",
        "answer": "That's so true.",
        "supplement": [
            "Exactly.",
            "That's right."
        ],
        "dialogue": [
            ("It's hard to find time for everything.", "很難有時間處理所有事情。"),
            ("That's so true.", "真的。"),
            ("We need to slow down a little.", "我們需要稍微放慢一點。")
        ]
    },

    # =====================================================
    # Day 12
    # =====================================================
    {
        "day": 12,
        "scenario_title": "表達不確定或保留意見",
        "category": "日常溝通",
        "chunk": "I'm not so sure about",
        "meaning": "我不太確定／我對……有點疑慮",
        "usage": "I'm not so sure about + 名詞",
        "challenge": "我不太確定這個計畫。",
        "answer": "I'm not so sure about this plan.",
        "supplement": [
            "I'm not sure about...",
            "I'm not convinced."
        ],
        "dialogue": [
            ("Should we go with this plan?", "我們應該採用這個計畫嗎？"),
            ("I'm not so sure about it.", "我不太確定。"),
            ("Maybe we should think about it again.", "也許我們應該再想一下。")
        ]
    },

    {
        "day": 12,
        "scenario_title": "表達不確定或保留意見",
        "category": "日常溝通",
        "chunk": "It depends",
        "meaning": "要看情況",
        "usage": "It depends on + 名詞",
        "challenge": "要看天氣。",
        "answer": "It depends on the weather.",
        "supplement": [
            "That depends.",
            "It depends on..."
        ],
        "dialogue": [
            ("Are you going tomorrow?", "你明天會去嗎？"),
            ("It depends on the weather.", "要看天氣。"),
            ("Let's check the forecast.", "我們看一下天氣預報。")
        ]
    },

    {
        "day": 12,
        "scenario_title": "表達不確定或保留意見",
        "category": "日常溝通",
        "chunk": "I'm not sure if",
        "meaning": "我不確定是否……",
        "usage": "I'm not sure if + 子句",
        "challenge": "我不確定他今天會不會來。",
        "answer": "I'm not sure if he's coming today.",
        "supplement": [
            "I'm not sure whether...",
            "I don't know if..."
        ],
        "dialogue": [
            ("Is John coming today?", "John 今天會來嗎？"),
            ("I'm not sure if he's coming today.", "我不確定他今天會不會來。"),
            ("I'll ask him later.", "我晚點問他。")
        ]
    },

    # =====================================================
    # Day 13
    # =====================================================
    {
        "day": 13,
        "scenario_title": "購物與詢問價格、尺寸",
        "category": "購物",
        "chunk": "Do you have this in",
        "meaning": "這個有……尺寸／顏色嗎？",
        "usage": "Do you have this in + 尺寸／顏色",
        "challenge": "這件有大一號嗎？",
        "answer": "Do you have this in a larger size?",
        "supplement": [
            "Do you have a bigger one?",
            "Do you have this in black?"
        ],
        "dialogue": [
            ("Do you have this in a larger size?", "這件有大一號嗎？"),
            ("Let me check for you.", "我幫你確認一下。"),
            ("Thank you.", "謝謝。")
        ]
    },

    {
        "day": 13,
        "scenario_title": "購物與詢問價格、尺寸",
        "category": "購物",
        "chunk": "Can I try this on?",
        "meaning": "我可以試穿嗎？",
        "usage": "服飾店試穿",
        "challenge": "我可以試穿這件嗎？",
        "answer": "Can I try this on?",
        "supplement": [
            "Where are the fitting rooms?",
            "Can I try this on in a different size?"
        ],
        "dialogue": [
            ("Can I try this on?", "我可以試穿這件嗎？"),
            ("Sure. The fitting rooms are over there.", "可以，試衣間在那邊。"),
            ("Thanks.", "謝謝。")
        ]
    },

    {
        "day": 13,
        "scenario_title": "購物與詢問價格、尺寸",
        "category": "購物",
        "chunk": "I'm looking for",
        "meaning": "我正在找／我想找",
        "usage": "I'm looking for + 名詞",
        "challenge": "我在找一件黑色外套。",
        "answer": "I'm looking for a black jacket.",
        "supplement": [
            "I'm trying to find...",
            "Do you have...?"
        ],
        "dialogue": [
            ("Can I help you?", "需要幫忙嗎？"),
            ("I'm looking for a black jacket.", "我在找一件黑色外套。"),
            ("Sure. What size are you?", "好的，你穿什麼尺寸？")
        ]
    },

    # =====================================================
    # Day 14
    # =====================================================
    {
        "day": 14,
        "scenario_title": "交通問路與求助",
        "category": "旅遊",
        "chunk": "How do I get to",
        "meaning": "我要怎麼去……？",
        "usage": "How do I get to + 地點",
        "challenge": "我要怎麼去車站？",
        "answer": "How do I get to the station?",
        "supplement": [
            "What's the best way to get to...?",
            "How can I get to...?"
        ],
        "dialogue": [
            ("Excuse me. How do I get to the station?", "不好意思，我要怎麼去車站？"),
            ("Go straight and turn left.", "直走然後左轉。"),
            ("Thank you.", "謝謝。")
        ]
    },

    {
        "day": 14,
        "scenario_title": "交通問路與求助",
        "category": "旅遊",
        "chunk": "How long does it take to",
        "meaning": "需要多久時間……？",
        "usage": "How long does it take to + V",
        "challenge": "到那裡要多久？",
        "answer": "How long does it take to get there?",
        "supplement": [
            "How far is it?",
            "How long will it take?"
        ],
        "dialogue": [
            ("How long does it take to get there?", "到那裡要多久？"),
            ("About twenty minutes.", "大約 20 分鐘。"),
            ("By taxi or on foot?", "搭計程車還是走路？")
        ]
    },

    {
        "day": 14,
        "scenario_title": "交通問路與求助",
        "category": "旅遊",
        "chunk": "Where can I find",
        "meaning": "我在哪裡可以找到……？",
        "usage": "詢問地點或設施",
        "challenge": "請問哪裡可以找到洗手間？",
        "answer": "Where can I find the restroom?",
        "supplement": [
            "Where is...?",
            "Could you tell me where... is?"
        ],
        "dialogue": [
            ("Excuse me. Where can I find the restroom?", "不好意思，哪裡可以找到洗手間？"),
            ("It's around the corner.", "就在轉角那邊。"),
            ("Thanks a lot.", "非常謝謝。")
        ]
    },

    # =====================================================
    # Day 15
    # =====================================================
    {
        "day": 15,
        "scenario_title": "表達感謝與回應",
        "category": "日常社交",
        "chunk": "I really appreciate your help",
        "meaning": "真的很感謝你的幫忙",
        "usage": "表達真誠感謝",
        "challenge": "真的很感謝你的幫忙。",
        "answer": "I really appreciate your help.",
        "supplement": [
            "I really appreciate it.",
            "Thanks so much for your help."
        ],
        "dialogue": [
            ("Thanks for helping me with this.", "謝謝你幫我處理這個。"),
            ("No problem.", "沒問題。"),
            ("I really appreciate your help.", "真的很感謝你的幫忙。")
        ]
    },

    {
        "day": 15,
        "scenario_title": "表達感謝與回應",
        "category": "日常社交",
        "chunk": "No problem",
        "meaning": "沒問題／不會",
        "usage": "回應感謝或表示沒關係",
        "challenge": "謝謝你。沒問題。",
        "answer": "Thanks. No problem.",
        "supplement": [
            "No worries.",
            "Sure thing."
        ],
        "dialogue": [
            ("Thanks for waiting.", "謝謝你等我。"),
            ("No problem.", "沒問題。"),
            ("I know you were busy.", "我知道你很忙。")
        ]
    },

    {
        "day": 15,
        "scenario_title": "表達感謝與回應",
        "category": "日常社交",
        "chunk": "No worries",
        "meaning": "沒事／別擔心／沒關係",
        "usage": "非常常見的口語回應",
        "challenge": "抱歉讓你等了。沒關係。",
        "answer": "Sorry to keep you waiting. No worries.",
        "supplement": [
            "It's okay.",
            "That's okay."
        ],
        "dialogue": [
            ("Sorry I'm late.", "抱歉我遲到了。"),
            ("No worries.", "沒關係。"),
            ("Thanks for understanding.", "謝謝你的理解。")
        ]
    },

    # =====================================================
    # Day 16
    # =====================================================
    {
        "day": 16,
        "scenario_title": "電話與視訊會議開場",
        "category": "職場會議",
        "chunk": "Can you hear me?",
        "meaning": "你聽得到我嗎？",
        "usage": "電話／視訊會議",
        "challenge": "你聽得到我嗎？",
        "answer": "Can you hear me?",
        "supplement": [
            "Can everyone hear me?",
            "Is my audio okay?"
        ],
        "dialogue": [
            ("Can you hear me?", "你聽得到我嗎？"),
            ("Yes, I can hear you.", "有，我聽得到。"),
            ("Great. Let's get started.", "很好，我們開始吧。")
        ]
    },

    {
        "day": 16,
        "scenario_title": "電話與視訊會議開場",
        "category": "職場會議",
        "chunk": "I'll share my screen",
        "meaning": "我來分享我的畫面",
        "usage": "線上會議",
        "challenge": "我來分享我的畫面。",
        "answer": "I'll share my screen.",
        "supplement": [
            "Let me share my screen.",
            "Can you see my screen?"
        ],
        "dialogue": [
            ("I'll share my screen.", "我來分享我的畫面。"),
            ("Okay, I can see it.", "好，我看得到。"),
            ("Let me show you the latest version.", "我來給你看最新版本。")
        ]
    },

    {
        "day": 16,
        "scenario_title": "電話與視訊會議開場",
        "category": "職場會議",
        "chunk": "Let's move on to",
        "meaning": "我們接著進入……",
        "usage": "會議中轉換下一個議題",
        "challenge": "我們接著談下一個議題。",
        "answer": "Let's move on to the next topic.",
        "supplement": [
            "Let's talk about...",
            "Next, let's look at..."
        ],
        "dialogue": [
            ("I think we've covered everything here.", "我想這部分我們都談到了。"),
            ("Okay. Let's move on to the next topic.", "好，我們接著談下一個議題。"),
            ("Sounds good.", "好的。")
        ]
    },

    # =====================================================
    # Day 17
    # =====================================================
    {
        "day": 17,
        "scenario_title": "提出建議與邀約",
        "category": "日常社交",
        "chunk": "Why don't we",
        "meaning": "我們何不……？",
        "usage": "Why don't we + 原形動詞",
        "challenge": "我們何不明天再討論？",
        "answer": "Why don't we talk about it tomorrow?",
        "supplement": [
            "How about we...?",
            "Why don't you...?"
        ],
        "dialogue": [
            ("We don't have much time today.", "我們今天沒多少時間。"),
            ("Why don't we talk about it tomorrow?", "我們何不明天再談？"),
            ("That works for me.", "我可以。")
        ]
    },

    {
        "day": 17,
        "scenario_title": "提出建議與邀約",
        "category": "日常社交",
        "chunk": "Count me in",
        "meaning": "算我一份／我參加",
        "usage": "表示願意參加",
        "challenge": "如果你們要去，我也參加。",
        "answer": "If you're going, count me in.",
        "supplement": [
            "I'm in.",
            "I'm down."
        ],
        "dialogue": [
            ("We're going out for dinner tonight.", "我們今晚要出去吃飯。"),
            ("Count me in.", "算我一份。"),
            ("Great. Let's meet at seven.", "好，七點見。")
        ]
    },

    {
        "day": 17,
        "scenario_title": "提出建議與邀約",
        "category": "日常社交",
        "chunk": "Maybe next time",
        "meaning": "也許下次吧",
        "usage": "婉拒邀約",
        "challenge": "今天不行，也許下次吧。",
        "answer": "I can't make it today. Maybe next time.",
        "supplement": [
            "Maybe another time.",
            "I'll pass this time."
        ],
        "dialogue": [
            ("Do you want to come with us?", "你要跟我們一起去嗎？"),
            ("I can't make it today. Maybe next time.", "今天不行，也許下次吧。"),
            ("Sure, no problem.", "好，沒問題。")
        ]
    },

    # =====================================================
    # Day 18
    # =====================================================
    {
        "day": 18,
        "scenario_title": "表達歉意與解釋",
        "category": "日常溝通",
        "chunk": "I'm sorry about",
        "meaning": "對……感到抱歉",
        "usage": "I'm sorry about + 名詞",
        "challenge": "很抱歉造成這個問題。",
        "answer": "I'm sorry about the problem.",
        "supplement": [
            "I'm sorry for...",
            "I'm really sorry about..."
        ],
        "dialogue": [
            ("The file was sent to the wrong person.", "檔案寄錯人了。"),
            ("I'm sorry about that.", "很抱歉。"),
            ("I'll fix it right away.", "我會馬上處理。")
        ]
    },

    {
        "day": 18,
        "scenario_title": "表達歉意與解釋",
        "category": "日常溝通",
        "chunk": "It was my fault",
        "meaning": "是我的錯",
        "usage": "承認責任",
        "challenge": "是我的錯，我應該再確認一次。",
        "answer": "It was my fault. I should have double-checked.",
        "supplement": [
            "My mistake.",
            "I should have..."
        ],
        "dialogue": [
            ("The wrong file was sent.", "寄錯檔案了。"),
            ("It was my fault. I should have double-checked.", "是我的錯，我應該再確認一次。"),
            ("It's okay. Let's fix it.", "沒關係，我們處理好就行。")
        ]
    },

    {
        "day": 18,
        "scenario_title": "表達歉意與解釋",
        "category": "日常溝通",
        "chunk": "I'll make sure it doesn't happen again",
        "meaning": "我會確保不會再發生",
        "usage": "道歉後承諾改進",
        "challenge": "我會確保這種事不會再發生。",
        "answer": "I'll make sure it doesn't happen again.",
        "supplement": [
            "It won't happen again.",
            "I'll be more careful next time."
        ],
        "dialogue": [
            ("I'm sorry about the mistake.", "很抱歉這次的錯誤。"),
            ("I'll make sure it doesn't happen again.", "我會確保不會再發生。"),
            ("Okay. Thanks for taking care of it.", "好，謝謝你處理。")
        ]
    }
]


# =========================================================
# Session State
# =========================================================
if "day" not in st.session_state:
    st.session_state.day = "全部 Chunk"

if "card_index" not in st.session_state:
    st.session_state.card_index = 0

if "is_flipped" not in st.session_state:
    st.session_state.is_flipped = False

if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

if "last_day" not in st.session_state:
    st.session_state.last_day = st.session_state.day


# =========================================================
# 主標題
# =========================================================
st.title("🚀 Daily English｜高頻語塊口說特訓庫")

st.write(
    "專為打造英文流利度設計！每天 3 個高頻語塊，放在同一個真實情境中練習。"
)


# =========================================================
# 側邊欄
# =========================================================
with st.sidebar:

    st.header("🗂️ 學習導航")

    day_options = ["全部 Chunk"] + [
        f"Day {day}"
        for day in sorted(set(item["day"] for item in chunks_database))
    ]

    current_day_index = (
        day_options.index(st.session_state.day)
        if st.session_state.day in day_options
        else 0
    )

    selected_day = st.selectbox(
        "選擇學習日",
        day_options,
        index=current_day_index
    )

    # Day 改變
    if selected_day != st.session_state.day:
        st.session_state.day = selected_day
        st.session_state.card_index = 0
        st.session_state.is_flipped = False
        st.session_state.show_answer = False
        st.rerun()

    categories = ["全部顯示"] + sorted(
        set(item["category"] for item in chunks_database)
    )

    selected_category = st.selectbox(
        "選擇分類",
        categories
    )


# =========================================================
# 篩選資料
# =========================================================
if st.session_state.day == "全部 Chunk":

    filtered_db = chunks_database.copy()

else:

    selected_day_number = int(
        st.session_state.day.replace("Day ", "")
    )

    filtered_db = [
        item
        for item in chunks_database
        if item["day"] == selected_day_number
    ]


# 分類篩選
if selected_category != "全部顯示":

    filtered_db = [
        item
        for item in filtered_db
        if item["category"] == selected_category
    ]


# 沒有資料
if not filtered_db:
    st.warning("目前沒有符合條件的 Chunk。")
    st.stop()


# 防止 index 超出範圍
if st.session_state.card_index >= len(filtered_db):
    st.session_state.card_index = 0


current_data = filtered_db[st.session_state.card_index]


# =========================================================
# 學習卡片
# =========================================================
if st.session_state.day == "全部 Chunk":

    display_day = f"Day {current_data['day']}"

else:

    display_day = st.session_state.day


st.markdown(
    f"### 📚 {display_day}｜學習卡片 "
    f"({st.session_state.card_index + 1}/{len(filtered_db)})"
)


progress = (
    (st.session_state.card_index + 1)
    / len(filtered_db)
)

st.progress(progress)


st.info(
    f"🎯 情境：{current_data['scenario_title']}"
)


st.divider()


# =========================================================
# Chunk 基本資訊
# =========================================================
col1, col2 = st.columns(2)

with col1:
    st.caption(f"📂 {current_data['category']}")

with col2:
    st.caption(
        f"Day {current_data['day']} / "
        f"#{chunks_database.index(current_data) + 1}"
    )


st.markdown(
    f"""
    <div style="
        background-color:#e8f5e9;
        padding:22px;
        border-radius:12px;
        margin-top:10px;
        margin-bottom:10px;
    ">
        <div style="
            font-size:14px;
            color:#555;
            margin-bottom:8px;
        ">
            ⭐ 核心 Chunk
        </div>

        <div style="
            font-size:30px;
            font-weight:bold;
            color:#1b5e20;
        ">
            {current_data["chunk"]}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


speak_text(
    current_data["chunk"],
    f"main_chunk_{current_data['day']}_{st.session_state.card_index}"
)


# =========================================================
# 口說挑戰
# =========================================================
st.divider()

st.markdown("### 🎤 口說挑戰")

st.info(
    f"🇹🇼 情境：{current_data['challenge']}\n\n"
    "先不要看答案，直接用英文說出來。"
)


if st.button(
    "👀 我說完了，查看自然英文",
    key=f"show_answer_{current_data['day']}_{st.session_state.card_index}"
):

    st.session_state.show_answer = True


if st.session_state.show_answer:

    st.success(
        f"🇺🇸 自然英文：\n\n"
        f"{current_data['answer']}"
    )

    speak_text(
        current_data["answer"],
        f"answer_{current_data['day']}_{st.session_state.card_index}"
    )


# =========================================================
# 翻面：完整情境
# =========================================================
st.divider()

if st.button(
    "🔄 點擊翻面 / 查看完整情境對話",
    key=f"flip_{current_data['day']}_{st.session_state.card_index}"
):

    st.session_state.is_flipped = not st.session_state.is_flipped


if st.session_state.is_flipped:

    st.success(
        f"🇹🇼 中文意思：{current_data['meaning']}"
    )

    st.info(
        f"💡 使用方式：{current_data['usage']}"
    )

    # -----------------------------------------------------
    # 補充 Chunk
    # -----------------------------------------------------
    st.markdown("### 💡 補充 Chunk")

    st.caption(
        "這些也是實用語塊，但優先級低於今天的核心 Chunk。"
    )

    for i, supplement in enumerate(
        current_data.get("supplement", [])
    ):

        col_a, col_b = st.columns([5, 1])

        with col_a:
            st.markdown(
                f"**{supplement}**"
            )

        with col_b:
            speak_text(
                supplement,
                f"supplement_{current_data['day']}_{st.session_state.card_index}_{i}"
            )

    # -----------------------------------------------------
    # 情境對話
    # -----------------------------------------------------
    st.markdown("### 💬 母語情境對話")

    for i, (english, chinese) in enumerate(
        current_data["dialogue"]
    ):

        st.markdown(
            f"**🇺🇸 {english}**"
        )

        st.caption(
            f"🇹🇼 {chinese}"
        )

        speak_text(
            english,
            f"dialogue_{current_data['day']}_{st.session_state.card_index}_{i}"
        )


# =========================================================
# 底部操作
# =========================================================
st.divider()

col1, col2, col3 = st.columns(3)


# ---------------------------------------------------------
# 上一張
# ---------------------------------------------------------
with col1:

    if st.button(
        "⬅️ 上一張",
        use_container_width=True
    ):

        st.session_state.card_index -= 1

        if st.session_state.card_index < 0:
            st.session_state.card_index = len(filtered_db) - 1

        st.session_state.is_flipped = False
        st.session_state.show_answer = False

        st.rerun()


# ---------------------------------------------------------
# 隨機抽卡
# ---------------------------------------------------------
with col2:

    if st.button(
        "🎲 隨機抽卡",
        use_container_width=True
    ):

        if len(filtered_db) > 1:

            possible_indexes = [
                i
                for i in range(len(filtered_db))
                if i != st.session_state.card_index
            ]

            st.session_state.card_index = random.choice(
                possible_indexes
            )

        else:

            st.session_state.card_index = 0

        st.session_state.is_flipped = False
        st.session_state.show_answer = False

        st.rerun()


# ---------------------------------------------------------
# 下一張
# ---------------------------------------------------------
with col3:

    if st.button(
        "➡️ 下一張",
        use_container_width=True
    ):

        if st.session_state.card_index < len(filtered_db) - 1:

            st.session_state.card_index += 1

        else:

            st.session_state.card_index = 0

            if st.session_state.day != "全部 Chunk":

                st.balloons()

                st.success(
                    "🎉 今天 3 個 chunks 都完成了！"
                )

        st.session_state.is_flipped = False
        st.session_state.show_answer = False

        st.rerun()


# =========================================================
# 學習提示
# =========================================================
st.divider()

st.caption(
    "💡 建議：先看中文情境 → 自己說英文 → 查看答案 → 聽朗讀 → 再看完整對話。"
)

st.caption(
    "🚀 每天只練 3 個核心 chunks，不求一次背很多，重點是能真的說出口。"
)

st.caption(
    "📚 補充 Chunk 是額外素材，不需要當天全部背起來。"
)
