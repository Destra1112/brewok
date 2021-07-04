#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>• Owner : <a href='tg://user?id={OWNER_ID}'>OWNER CAKEP</a>\n○ BAHASA : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n• Tutorial Clone : <a href='https://t.me/LEOANGKASAAA'>TEKAN DISINI</a>\n• CHANNEL ASUPAN : <a href='https://t.me/desahannsange'>ASUPAN DISINI</a>\n• SUPPORT CHANNEL : <a href='https://t.me/storyangkasa'>SUPPORT CHANNEL</a>\n• OWNER REPO: @LEOANGKASAAA</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("❌ Keluar", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
