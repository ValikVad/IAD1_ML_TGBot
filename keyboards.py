from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


menu = [
    [InlineKeyboardButton(text="Распознавание текста", callback_data="text_detector"),
    InlineKeyboardButton(text="Переводчик", callback_data="translate")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)


# exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
# iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])


translate_menu = [
    [InlineKeyboardButton(text="перефоткаем", callback_data="text_detector"),
    InlineKeyboardButton(text="Исправим текст сами", callback_data="get_text_from_user")],
    [InlineKeyboardButton(text="переводим", callback_data="translate")]
]
translate_menu = InlineKeyboardMarkup(inline_keyboard=translate_menu)

choose_lang = [
    [InlineKeyboardButton(text="eng -> rus", callback_data="eng"),
    InlineKeyboardButton(text="rus -> eng", callback_data="rus")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]
choose_lang = InlineKeyboardMarkup(inline_keyboard=choose_lang)

end = [
    [InlineKeyboardButton(text="menu", callback_data="start"),
    InlineKeyboardButton(text="back", callback_data="back")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]