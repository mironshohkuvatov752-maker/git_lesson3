from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

menu_inline=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📕Kurslar",callback_data="kurs")
        ],
        [
            InlineKeyboardButton(text="📚Kitoblar",callback_data="kitob")
        ],
        [
            InlineKeyboardButton(text="👨‍💻Biz haqimizda",callback_data="biz"),
            InlineKeyboardButton(text="🖌Kursga yozilish",callback_data="registar"),
        ]
    ]
)

kurslar_inline=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🕹IT",callback_data="it"),
            InlineKeyboardButton(text="▶️Backend", callback_data="bak")
        ],
        [
            InlineKeyboardButton(text="🏓CMM", callback_data="cmm"),
            InlineKeyboardButton(text="🎮Frontend", callback_data="fron")
        ],
        [
            InlineKeyboardButton(text="🔙Ortga",callback_data="ortga")
        ]
    ]
)

kitob_inline=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📘Sof Kod",callback_data="sof"),
            InlineKeyboardButton(text="😎Dasturchining yo‘li",callback_data="das")
        ],
        [
            InlineKeyboardButton(text="😎Algoritmlarni tushunish",callback_data="algo"),
            InlineKeyboardButton(text="☠️Python asoslari",callback_data="py")
        ],
        [
            InlineKeyboardButton(text="🧠JavaScript va Node.js asoslari",callback_data="java")
        ],
        [
            InlineKeyboardButton(text="🔙Ortga",callback_data="ortga")
        ]
    ]
)

biz_inline=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙Ortga",callback_data="ortga")
        ]
    ]
)

yozilish_inline=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙Ortga",callback_data="ortga")
        ]
    ]
)

it_menu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙Ortga",callback_data="ortga")
        ]
    ]
)

bac_menu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙Ortga",callback_data="ortga")
        ]
    ]
)

cmm_menu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙Ortga",callback_data="ortga")
        ]
    ]
)

fron_menu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙Ortga",callback_data="ortga")
        ]
    ]
)

ortga_inline=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙Ortga",callback_data="orqaga")
        ]
    ]
)

