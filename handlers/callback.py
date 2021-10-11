

from handlers.play import cb_admin_check
from helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)



@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🗼 **مرحبا , {query.message.from_user.mention} !** \n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) يسمح لك بتشغيل الموسيقى على المجموعات من خلال الدردشات الصوتية في Telegram الجديدة!**

🗼 **معرفة جميع الأوامر بوت وكيفية عملها من خلال النقر على زر » 📚 الأوامر !**

❔ **لمعرفة كيفية استخدام هذا بوت، يرجى الضغط على » ❓ زر الدليل الأساسي!**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        " أضفني إلى مجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        " دليل المستخدم   ", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "📚 لاوامر", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "المطور", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        " قناه  الملفات", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "قناه لبسورس", url=f"https://t.me/{UPDATES_CHANNEL}")
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🗼 مرحبا هناك، مرحبا بكم في قائمة المساعدة !</b>

**في هذه القائمة يمكنك فتح العديد من قوائم الأوامر المتاحة، في كل قائمة الأمر هناك أيضا شرح موجز لكل أمر**

🗼 __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📍︙الاوامر الاساسيه", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "🗽︙الاوامر المتقدمه ", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🦹🏻︙اومر الادمنيه", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "🐉︙اومر المطورين", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🐉︙اومر المالك", callback_data="cbowner"
                    )
                ],
              
                [
                    InlineKeyboardButton(
                        "🏡 الرجوع الى المساعده", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>📍 هنا الأوامر الأساسية</b>
- تشغيل الأغنية من اليوتيوب
/play اسم الاغنيه :
- تشغيل الأغنية مباشرة من اليوتيوب
/ytp اسم الاغنيه: 
دفق (الرد على الصوت) - تشغيل الأغنية باستخدام ملف صوتي /stream
قائمة التشغيل - إظهار أغنية القائمة في قائمة الانتظار /playlist
/song أغنية (اسم الأغنية) - تنزيل أغنية من youtube
/search البحث (اسم الفيديو) - ابحث عن مقطع فيديو من youtube بالتفصيل
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
/vsong (اسم الفيديو) - تنزيل الفيديو من youtube مفصل
/ غنائي - (اسم الأغنية) مكشطة كلمات
/vk (اسم الأغنية) - تنزيل الأغنية من الوضع المضمَّن
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
/play - دفق الموسيقى على قناة الدردشة الصوتية
/cplayer - إظهار الأغنية أثناء البث
/cpause - إيقاف الموسيقى المتدفقة مؤقتًا
/cresume - استئناف توقف البث مؤقتًا
/cskip - تخطي التدفق إلى الأغنية التالية
/cend - قم بإنهاء تدفق الموسيقى
/admincache - قم بتحديث ذاكرة التخزين المؤقت للمسؤول
/ubjoinc - قم بدعوة المساعد للانضمام إلى قناتك

🎪 __ by {BOT_NAME} __""",
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
        f"""<b>🦹🏻︙ ها هي الأوامر المتقدمة</b>

 ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
/start : (في المجموعة) - انظر حالة الروبوت على قيد الحياة
/cache : أعد تحميل البوت وقم بتحديث قائمة الإدارة
/cache : تحديث ذاكرة التخزين المؤقت للمسؤول
/ping : تحقق من حالة البوت بينغ
/uptime : تحقق من حالة وقت تشغيل الروبوت
/id : إظهار المجموعة / هوية المستخدم وغيرها""",
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
        f"""<b>🎸︙هنا هو أوامر المشرف </b>

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
/player مشغل - عرض حالة تشغيل الموسيقى
/ pause - إيقاف تدفق الموسيقى مؤقتًا
/pause استئناف - استئناف تم إيقاف الموسيقى مؤقتًا
/skip تخطي - انتقل إلى الأغنية التالية
/stop - إيقاف تدفق الموسيقى
/userbotjoin - دعوة المساعد للانضمام إلى مجموعتك
/auth - المستخدم المصرح له باستخدام برنامج Music bot
/deauth - غير مصرح به لاستخدام برنامج تتبع الموسيقى
/control التحكم - افتح لوحة إعدادات المشغل
/delcmd (on | off) - تمكين / تعطيل ميزة del cmd
/musicplayer مشغل الموسيقى (تشغيل إيقاف) - تعطيل / تمكين مشغل الموسيقى في مجموعتك
/b و /tb (الحظر / الحظر المؤقت) - مستخدم محظور بشكل دائم أو مؤقت في المجموعة
/ub - إلى مستخدم غير محظور تم حظرك من المجموعة
/m و /tm (كتم الصوت / كتم الصوت المؤقت) - كتم صوت المستخدم في المجموعة بشكل دائم أو مؤقت
/um - لإلغاء كتم صوت المستخدم الذي تم كتمه في المجموعة""",
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
        f"""<b>🐉 هنا أوامر المطور </b>

/userbotleaveall - اطلب من المساعد المغادرة من جميع المجموعات
/gcast - إرسال رسالة بث trought المساعد
/stats - إظهار إحصائية البوت
/rmd - إزالة كافة الملفات التي تم تنزيلها""",
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
        f"""<b>🦹🏻 هنا هو أوامر المالك</b>
/stats -- تبين إحصاءات بوت
/broadcast - إرسال رسالة بث من بوت
/block (معرف المستخدم -- مدة -- السبب) -- المستخدم كتلة لاستخدام بوت الخاص بك
/unblock إلغاء الحظر (معرف المستخدم - السبب) - إلغاء حظر المستخدم الذي قمت بحظره لاستخدام البوت الخاص بك
/blocklist -- تظهر لك قائمة المستخدم تم حظره لاستخدام بوت الخاص بك

📝 ملاحظة: يمكن تنفيذ جميع الأوامر التي يملكها هذا البوت من قبل مالك البوت دون أي استثناءات. _""",
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
        f""" كيفية استخدام هذا البوت:

1.) أولا، إضافة لي إلى مجموعتك.
2.) ثم ترقية لي كمسؤول وإعطاء جميع الأذونات باستثناء المشرف مجهول.
3.) إضافة @{ASSISTANT_NAME} إلى مجموعتك أو اكتب /join لدعوتها.
4.) تشغيل الدردشة الصوتية أولا قبل البدء في تشغيل الموسيقى. _""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 الاوامر", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔻 ", callback_data="close"
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
        "**🎸هنا قائمة التحكم في البوت :**",
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
                [InlineKeyboardButton("🗼 group tools", callback_data="cbgtools")],
                [InlineKeyboardButton("🔻 Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>هذه هي ميزة المعلوماتn :</b>
🗼 ** الميزة: ** تحتوي هذه الميزة على وظائف يمكنها حظر وكتم الصوت وإلغاء الحظر وإلغاء كتم صوت المستخدمين في مجموعتك.
ويمكنك أيضًا تحديد وقت للحظر وعقوبات كتم الصوت لأعضاء مجموعتك بحيث يمكن تحريرهم من العقوبة في الوقت المحدد.
❔ ** الاستخدام: **
1️⃣ حظر المستخدم وحظره مؤقتًا من مجموعتك:
   »اكتب` / b اسم المستخدم / الرد على الرسالة` حظر بشكل دائم
   اكتب `/ tb username / الرد على الرسالة / المدة` حظر المستخدم مؤقتًا
   »اكتب` / ub username / رد على الرسالة` لمستخدم غير محظور
2️⃣ كتم وكتم المستخدم مؤقتًا في مجموعتك:
   »اكتب` / m اسم المستخدم / الرد على الرسالة` كتم الصوت بشكل دائم
   اكتب `/ tm اسم المستخدم / الرد على الرسالة / المدة` كتم المستخدم مؤقتًا
   »اكتب` / um اسم المستخدم / رد على الرسالة` لإلغاء كتم صوت المستخدم
📝 ملاحظة: cmd / b و / tb و / ub هي وظيفة للمستخدم المحظور / غير المحظور من مجموعتك ، بينما / m و / tm و / um هي أوامر لكتم / إلغاء كتم صوت المستخدم في مجموعتك""",
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
        f"""<b>مرحبًا بكم ، مرحبًا بكم في قائمة المساعدة !</b>

**في هذه القائمة ، يمكنك فتح العديد من قوائم الأوامر المتاحة ، وفي كل قائمة أوامر يوجد أيضًا شرح موجز لكل أمر **""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📍︙الاوامر الاساسيه", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "🗽︙الاوامر المتقدمه", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🦹🏻︙اومر الادمنيه", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "🐉︙اومر المطورين", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🐉︙اومر المالك", callback_data="cbowner"
                    )
                ],
        
                [
                    InlineKeyboardButton(
                        "🏡 الرجوع", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" كيفية استخدام هذا البوت:

1.) أولا، إضافة لي إلى مجموعتك.
2.) ثم ترقية لي كمسؤول وإعطاء جميع الأذونات باستثناء المشرف مجهول.
3.) إضافة @{ASSISTANT_NAME} إلى مجموعتك أو اكتب /userbotjoin لدعوتها.
4.) تشغيل الدردشة الصوتية أولا قبل البدء في تشغيل الموسيقى.""",
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
