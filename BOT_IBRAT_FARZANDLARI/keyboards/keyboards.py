from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton



start_menu = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="Inglesh tili 🇬🇧"),
        ],
        [
            KeyboardButton(text="AELTS 🇺🇸"),  
        ]
        [
          KeyboardButton(text="Pashtu tili 🇦🇫")  
        ],    
    ],
    resize_keyboard=True
)





tugma_holati_pashtu1 = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="Birinchi dars 🇦🇫📚¹"),
            KeyboardButton(text="Ikkinchi dars 🇦🇫📚²"),
            KeyboardButton(text="Uchinchi dars 🇦🇫📚³"),   
        ],
        [
            KeyboardButton(text="To'rinchi dars 🇦🇫📚⁴"),
            KeyboardButton(text="Beshinchi dars 🇦🇫📚⁵"),
            KeyboardButton(text="Oltinchi dars 🇦🇫📚⁶"),
        ],
        [
            KeyboardButton(text="Yettinchi dars 🇦🇫📚⁷"),
            KeyboardButton(text="Sakkizinchi dars 🇦🇫📚⁸"),
            KeyboardButton(text="To'qqizzinchi dars 🇦🇫📚⁹"),
        ],
        [
            KeyboardButton(text="🔙 Orqaga")  
        ],
    ],
    resize_keyboard=True
)

tugma_holati_vyetnam = ReplyKeyboardMarkup







you_tube_inline = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text="You tube kanalimiz ", callback_data="you_t"),
            InlineKeyboardButton(text="instagram kanalimiz ", callback_data="inst")
        ],
    ]
)