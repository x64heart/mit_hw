import asyncio
import traceback
import aiogram
from aiogram.enums import ParseMode
from aiogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup
import json

async def amain():
    config={}    
    with open('config.json','tr',encoding='utf-8') as fp:
        config=json.load(fp)
    start=InlineKeyboardMarkup(
        inline_keyboard=[
           [
             InlineKeyboardButton(text='Info',callback_data='info'),
             InlineKeyboardButton(text='Docs',url='https://docs.python.org/3/'),
           ]
        ]
    )
    token=config['token']#
    bot=aiogram.Bot(token=token,parse_mode=ParseMode.HTML)
    dp=aiogram.Dispatcher()
    @dp.message()
    async def on_text_msg(message:Message):
        await message.reply(text='Text',reply_markup=start)

    @dp.callback_query()
    async def _info(message:Message):
        await message.answer("Info: ....")
    await dp.start_polling(bot)

def main():
    asyncio.run(amain())


if __name__=="__main__":
    try:
        main()
    except:
        print(traceback.format_exc())
