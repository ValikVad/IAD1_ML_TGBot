from aiogram import F, Router, types, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.methods import SendPhoto
from aiogram import flags
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
import numpy as np


import utils
from states import Gen
from aiogram.types.callback_query import CallbackQuery
from PIL import Image
from aiogram.filters import Filter
import keyboards
import text

router = Router()

"""
Main part fith start menu and change state to translate or something else

"""
@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    await state.set_state(Gen.start)
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=keyboards.menu)

@router.callback_query(Gen.start,F.data == "text_detector")
async def text_detector( clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.await_pic_to_recognition)
    await clbck.message.edit_text(text.text_recognition_only)


@router.callback_query(Gen.start, F.data == "translate")
async def translate_start( clbck: CallbackQuery, state: FSMContext):
    await clbck.message.edit_text(text=text.text_recognition_only)
    await state.set_state(Gen.await_pic_to_translate)
    # await state.update_data()


@router.callback_query(F.data == "help")
async def translate_help( clbck: CallbackQuery, state: FSMContext):
    await clbck.message.edit_text(text.help)






@router.message(Gen.await_pic_to_recognition, F.photo)
async def req5(msg: Message, state: FSMContext, bot: Bot):

    content = await bot.download(msg.photo[-1])
    text = utils.text_recognise(msg.photo[-1])
    await msg.answer(text=text, reply_markup=keyboards.menu)


@router.message(Gen.await_pic_to_translate, F.photo)
async def req4(msg: Message, state: FSMContext, bot: Bot):


    content = await bot.download(msg.photo[-1])

    text_for_tr = utils.text_recognise(msg.photo[-1])
    await state.set_data({"pic": content, "text_for_tr": text_for_tr})
    await state.set_state(Gen.await_lang)
    await msg.answer(text=text.translate_menu, reply_markup=keyboards.translate_menu)


@router.message(Gen.await_pic_to_translate, F.data == "eng")
async def req3(msg: Message, state: FSMContext, bot: Bot):
    await state.set_state(Gen.translte_eng)

    


@router.message(Gen.await_pic_to_translate, F.data == "rus")
async def req2(msg: Message, state: FSMContext, bot: Bot):
    await state.set_state(Gen.translte_rus)

    



@router.message(Gen.await_lang, F.data == "translate")
async def req(msg: Message, state: FSMContext, bot: Bot):

    await msg.answer(text=text.translate_menu, reply_markup=keyboards.choose_lang)


    # w = msg.photo[-1].width
    # h = msg.photo[-1].height
    # print(w, h)
#     PILimage = Image.open(content)
#     PILimage.save('result.png')

#     text_recognize.shutdown()
#     # if F.text == "text":
#     #     F.text == "t"

#     #     utils.text_recognise()
#     #     print(F.text == "text")
        
        
        
        
#     # if F.text == "translate":
#     #     print('translate', F.text )
#     #     F.text == "t"
#     #     print('translate', F.text )


# @router.callback_query(F.data == "ready_to_translate")
# async def translate_text(clbck: CallbackQuery, state: FSMContext):
#     utils.text_translate()
#     # await clbck.message.edit_text("")
#     # print(F.data) 
