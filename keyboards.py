from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


menu = [
    [InlineKeyboardButton(text="rus->en", callback_data="rus"),
    InlineKeyboardButton(text="en->rus", callback_data="en")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)


# exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
# iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])



# choose_lang = [
#     [InlineKeyboardButton(text="eng -> rus", callback_data="eng"),
#     InlineKeyboardButton(text="rus -> eng", callback_data="rus")],
#     [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
# ]
# choose_lang = InlineKeyboardMarkup(inline_keyboard=choose_lang)

# end = [
#     [InlineKeyboardButton(text="menu", callback_data="start"),
#     InlineKeyboardButton(text="back", callback_data="back")],
#     [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
# ]