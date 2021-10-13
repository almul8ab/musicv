from pyrogram import Client
import asyncio
from config import SUDO_USERS, PMPERMIT, OWNER_NAME, BOT_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from pyrogram import filters
from pyrogram.types import Message
from callsmusic.callsmusic import client as USER

PMSET = True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
            f"✨ مرحبًا {message.from_user.mention} ، أنا مساعد موسيقى رسمي ** لـ {BOT_NAME}. ** \ n \ n❗️ ** ملاحظات: ** \ n \ n⫸ لا ترسل رسائل غير مرغوب فيها. \ n ⫸ لا ترسل لي أي شيء سري \ n \ n⨀ انضم إلى @ {UPDATES_CHANNEL} \ n⨀ انضم إلى @ {GROUP_SUPPORT} \ n \ n👩🏻‍💻 Dev: @ {OWNER_NAME} \ n \ n👩🏻‍🔧 إذا كنت تريد مني الانضمام إلى مجموعتك ، فأرسل هنا ارتباط المجموعة الخاص بك ، وسألتحق في أقرب وقت ممكن. \ n \ n",
            )
            return

    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("✅ PMpermit قيد التشغيل
")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("❎ إيقاف PMpermit
")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("تمت الموافقة عليه للمساء بسبب الرسائل الصادرة")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("yes", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("✅ وافق مساء.")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("no", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("❌ مرفوض حتى مساء..")
        return
    message.continue_propagation()
