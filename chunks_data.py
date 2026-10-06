# 10個高頻語塊資料庫
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
            ("Ah, well, hair grows back!", "啊,好吧,頭髮會再長長嘛!"),
        ],
    },
    {
        "id": 3,
        "category": "狀況外 / 忘記了",
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
    {
        "id": 9,
        "category": "輕鬆看待 / 別緊張",
        "chunk": "take something with a grain of salt",
        "meaning": "半信半疑、聽聽就好、別太當真",
        "scenario": "當聽到網路傳聞、八卦或不可靠的來源時提醒別人。",
        "dialogues": [
            ("Did you hear that the company might cut bonuses?", "你有聽說公司可能會砍獎金嗎？"),
            (
                "I read it online, but I'm taking it with a grain of salt.",
                "我是上網看到的，但我抱持半信半疑的態度。",
            ),
            ("Better wait for an official announcement.", "最好等官方宣佈再說。"),
        ],
    },
    {
        "id": 10,
        "category": "全神貫注 / 專心",
        "chunk": "all ears",
        "meaning": "洗耳恭聽、全神貫注聽你說",
        "scenario": "當別人說「我有個好消息要跟你說」時表達高度興趣。",
        "dialogues": [
            ("I have a brilliant idea for our upcoming project.", "我對接下來的專案有個超棒的點子。"),
            ("Go ahead, I'm all ears!", "說吧，我洗耳恭聽！"),
            ("Let's hear what you've got.", "聽聽看你有什麼想法。"),
        ],
    },
]
