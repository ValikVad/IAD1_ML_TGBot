from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    start = State()
    text_recognition_only = State()
    await_pic_to_translate = State()
    await_pic_to_recognition = State()
    await_lang = State()
    translte_rus = State()
    translte_eng = State()