from nltk.chat.util import Chat, reflections

# ChatBot'un adını tanımlayın
chatbot_name = "Nisa'nın ChatBot'u"

# Pairs is a list of patterns and responses.
pairs = [
    [
        r"merhaba|selam|hey",
        [f"Merhaba! Ben {chatbot_name}. Nasıl yardımcı olabilirim?", f"Selam! Ben {chatbot_name}. Size nasıl yardımcı olabilirim?"]
    ],
    [
        r"nasılsın|naber",
        [f"Ben bir chatbotum, bu yüzden duygularım yok. Size nasıl yardımcı olabilirim, {chatbot_name}?", f"{chatbot_name} burada! Size nasıl yardımcı olabilirim?"]
    ],

        [
            r"Nisanın en yakın arkadaşı kim|Nisa en çok kimi seviyor",
            [f"Tabi ki Helin! Aranızdaki bağ çok güzel. Siz örnek bir arkadaşlığa sahipsiniz. Kardeş gibi <3"]
        ],
    [
        r"adın ne|sen kimsin",
        [f"Ben bir chatbotum ve adım {chatbot_name}. Sizi nasıl destekleyebilirim?", f"Ben {chatbot_name}. Size nasıl yardımcı olabilirim?"]
    ],
    [
        r"çık|kapat|veda",
        [f"Güle güle! Başka bir sorunuz varsa sormaktan çekinmeyin, {chatbot_name}.", f"Çıkıyorum! Başka bir zaman görüşmek üzere, {chatbot_name}."]
    ],
    [
        r"hava nasıl",
        ["Hangi şehirde hava durumunu öğrenmek istersiniz?",
         "Lütfen hava durumunu öğrenmek istediğiniz şehri belirtin."]
    ],
    [
        r"(.*)(hava durumu)(.*)",
        ["Hava durumu sorgusu algılandı. Lütfen hangi şehirdeki hava durumunu öğrenmek istediğinizi belirtin."]
    ],
    [
        r"ne yapıyorsun|ne işe yararsın",
        ["Ben bir chatbotum ve size sorularınızı yanıtlamak için buradayım.", f"{chatbot_name}, size yardımcı olmak için burada."]
    ],
    # Daha fazla soru ve yanıt ekleyebilirsiniz
]

# default message at the start of chat
print(f"Merhaba, Ben {chatbot_name} ve sizinle sohbet etmeye hazırım. Çıkmak için 'çık' yazabilirsiniz.")

# Chat sınıfını oluşturun ve sohbeti başlatın
chat = Chat(pairs, reflections)
chat.converse()
