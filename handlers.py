from aiogram import F, Router, types, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.methods import SendPhoto
from aiogram import flags
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
import numpy as np
import aiogram
import re


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
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=keyboards.menu)

@router.callback_query(F.data == "en" )
async def text_detector( clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.eng)
    await clbck.message.edit_text(text.text_recognition_only)

@router.callback_query(F.data == "rus" )
async def text_detecto_r( clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.rus)
    await clbck.message.edit_text(text.text_recognition_only)

@router.callback_query(F.data == "help")
async def translate_help( clbck: CallbackQuery, state: FSMContext):
    await clbck.message.edit_text(text.help, reply_markup=keyboards.menu)


@router.message(Gen.eng, F.photo)
async def req4(msg: Message, state: FSMContext, bot: Bot):
    content = await bot.download(msg.photo[-1])
    text_for_tr = utils.text_recognise(Image.open(content), "en")
    # aiogram.methods.send_message.SendMessage(text=re.sub('\W+',' ', text_for_tr))
    # text_for_tr = re.sub('\W+\,\.',' ', text_for_tr)
    await msg.answer(text=re.sub('\W+',' ', text_for_tr))

    t = utils.text_translate(text_for_tr, "en")
    await msg.answer(text= re.sub('\W+\.\,',' ', t))

    await msg.answer(text=text.text_recognition_only, reply_markup=keyboards.menu)


@router.message(Gen.rus, F.photo)
async def req4___(msg: Message, state: FSMContext, bot: Bot):


    content = await bot.download(msg.photo[-1])

    text_for_tr = utils.text_recognise(Image.open(content), "rus")
    # text_for_tr =  
    # print(text_for_tr)
    await msg.answer(text=re.sub('\W+',' ', text_for_tr))
    
    t = utils.text_translate(text_for_tr, "rus")
    # t =  re.sub('\W+',' ', t)
    await msg.answer(text=re.sub('\W+\.\,',' ', t))
    await msg.answer(text=text.text_recognition_only, reply_markup=keyboards.menu)


        
        
        
    
