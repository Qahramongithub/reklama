from aiogram.types import InlineKeyboardButton, KeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def promo_button():
    ikb = InlineKeyboardBuilder()
    ikb.add(
        *[
            InlineKeyboardButton(text="✅Promo cod", callback_data="promo"),
            InlineKeyboardButton(text="🏢Biz haqimizda", callback_data="bizhaqimizda"),
        ]
    )
    ikb.adjust(1,1)
    return ikb.as_markup()
def menu_button(pege):
    ikb = InlineKeyboardBuilder()
    ikb.add(
        *[
            InlineKeyboardButton(text="⬅️", callback_data=f"product_{pege - 1}"),
            InlineKeyboardButton(text="➡️", callback_data=f"product_{pege + 1}"),
            InlineKeyboardButton(text="Qullanma", callback_data=f"qullanma"),
        ]
    )
    ikb.adjust(2, 1)
    return ikb.as_markup()
def back_button():
    ikb = InlineKeyboardBuilder()
    ikb.add(*[
        InlineKeyboardButton(text="🔙Ortga", callback_data="back"),
    ])
    return ikb.as_markup()
def instagram_button():
    rkb=ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text="Instagram 🔊",web_app=WebAppInfo(url='https://www.instagram.com/pramokod_uz?igsh=MXJscmd0bTVkMzkwOA=='))
    ])
    return rkb.as_markup(resize_keyboard=True)
