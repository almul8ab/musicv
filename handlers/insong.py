from pyrogram import Client
from config import BOT_USERNAME
from helpers.filters import command
from callsmusic.callsmusic import client as hama


@Client.on_message(command(["vk", f"vk@{BOT_USERNAME}"]))
async def songs(client, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("❗ **- لم يتم العثور على أغنية.**\n\n**ارجو اعطائي اسم الفنان ايضآ.**")
            return
        text = message.text.split(None, 1)[1]
        results = await hama.get_inline_bot_results(1873, f"music {text}")
        await hama.send_inline_bot_result(
            message.chat.id, results.query_id, results.results[0].id
        )
    except Exception:
        await message.reply_text("🎸 ** لم يتم العثور على الاغنيه**")
