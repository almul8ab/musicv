

from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from handlers.play import cb_admin_check
from helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>✨ **مرحبا , {query.message.from_user.mention} !** \n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) يسمح لك بتشغيل الموسيقى على المجموعات من خلال الدردشات الصوتية في Telegram الجديدة!**

💡 **معرفة جميع الأوامر بوت وكيفية عملها من خلال النقر على » 📚 الأوامر زر!**

❔ **لمعرفة كيفية استخدام هذا بوت، يرجى الضغط على » ❓ زر الدليل الأساسي!**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ أضفني إلى مجموعتك ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "❓الدليل الأساسي ", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "📚 لاوامر", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "💝 Donate", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "👥 Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}")
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 مرحبا هناك، مرحبا بكم في قائمة المساعدة !</b>

**في هذه القائمة يمكنك فتح العديد من قوائم الأوامر المتاحة، في كل قائمة الأمر هناك أيضا شرح موجز لكل أمر**

⚡ __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 الأساسية الاوامر ", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 Cmd متقدمة ", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📗 Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📙 Owner Cmd", callback_data="cbowner"
                    )
                ],
              
                [
                    InlineKeyboardButton(
                        "🏡 Back to Help", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the basic commands</b>

🎧 [ GROUP VC CMD ]

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/vsong (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper
/vk (song name) - download song from inline mode

🎧 [ CHANNEL VC CMD ]

/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/admincache - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel

⚡ __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the advanced commands</b>

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/cache - refresh the admin cache
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other

⚡ __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮هنا هو أوامر المشرف </b>

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/stop - stop music streaming
/userbotjoin - invite assistant join to your group
/auth - authorized user for using music bot
/deauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/musicplayer (on / off) - disable / enable music player in your group
/b and /tb (ban / temporary ban) - banned permanently or temporarily banned user in group
/ub - to unbanned user you're banned from group
/m and /tm (mute / temporary mute) - mute permanently or temporarily muted user in group
/um - to unmute user you're muted in group


⚡ __Powered by {BOT_NAME} """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 هنا أوامر سودو </b>

/userbotleaveall - اطلب من المساعد المغادرة من جميع المجموعات
/gcast - إرسال رسالة بث trought المساعد
/stats - إظهار إحصائية البوت
/rmd - إزالة كافة الملفات التي تم تنزيلها

⚡ __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 هنا هو أوامر المالك</b>
/stats -- تبين إحصاءات بوت
/broadcast - إرسال رسالة بث من بوت
/block (معرف المستخدم -- مدة -- السبب) -- المستخدم كتلة لاستخدام بوت الخاص بك
/unblock إلغاء الحظر (معرف المستخدم - السبب) - إلغاء حظر المستخدم الذي قمت بحظره لاستخدام البوت الخاص بك
/blocklist -- تظهر لك قائمة المستخدم تم حظره لاستخدام بوت الخاص بك

📝 ملاحظة: يمكن تنفيذ جميع الأوامر التي يملكها هذا البوت من قبل مالك البوت دون أي استثناءات.


⚡ __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )



@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ كيفية استخدام هذا البوت:

1.) أولا، إضافة لي إلى مجموعتك.
2.) ثم ترقية لي كمسؤول وإعطاء جميع الأذونات باستثناء المشرف مجهول.
3.) إضافة @{ASSISTANT_NAME} إلى مجموعتك أو اكتب /userbotjoin لدعوتها.
4.) تشغيل الدردشة الصوتية أولا قبل البدء في تشغيل الموسيقى.

⚡ __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 الاوامر", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 ", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**💡 here is the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⏸ pause", callback_data="cbpause"),
                    InlineKeyboardButton("▶️ resume", callback_data="cbresume"),
                ],
                [
                    InlineKeyboardButton("⏩ skip", callback_data="cbskip"),
                    InlineKeyboardButton("⏹ end", callback_data="cbend"),
                ],
                [InlineKeyboardButton("⛔ anti cmd", callback_data="cbdelcmds")],
                [InlineKeyboardButton("🛄 group tools", callback_data="cbgtools")],
                [InlineKeyboardButton("🗑 Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>
💡 **Feature:** this feature contains functions that can ban, mute, unban, unmute users in your group.
and you can also set a time for the ban and mute penalties for members in your group so that they can be released from the punishment with the specified time.
❔ **usage:**
1️⃣ ban & temporarily ban user from your group:
   » type `/b username/reply to message` ban permanently
   » type `/tb username/reply to message/duration` temporarily ban user
   » type `/ub username/reply to message` to unban user
2️⃣ mute & temporarily mute user in your group:
   » type `/m username/reply to message` mute permanently
   » type `/tm username/reply to message/duration` temporarily mute user
   » type `/um username/reply to message` to unmute user
📝 note: cmd /b, /tb and /ub is the function to banned/unbanned user from your group, whereas /m, /tm and /um are commands to mute/unmute user in your group.
⚡ __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🏡 Go Back", callback_data="cbback")]]
        ),
    )



@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>هذه هي معلومات الميزة :</b>
        
**💡 الميزة:** حذف كل الأوامر المرسلة من قبل المستخدمين لتجنب البريد المزعج في مجموعات !

❔ مثال:**

 1️⃣لتشغيل الميزة :
     » `/delcmd on`
    
 2️⃣ لإيقاف تشغيل الميزة:
     »  `/delcmd off`
      
⚡ __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 ", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 Hello there, welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

⚡ __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Basic Cmd", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 Advanced Cmd", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📗 Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📙 Owner Cmd", callback_data="cbowner"
                    )
                ],
        
                [
                    InlineKeyboardButton(
                        "🏡 Go Back", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ كيفية استخدام هذا البوت:

1.) أولا، إضافة لي إلى مجموعتك.
2.) ثم ترقية لي كمسؤول وإعطاء جميع الأذونات باستثناء المشرف مجهول.
3.) إضافة @{ASSISTANT_NAME} إلى مجموعتك أو اكتب /userbotjoin لدعوتها.
4.) تشغيل الدردشة الصوتية أولا قبل البدء في تشغيل الموسيقى.

⚡ __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 ", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
