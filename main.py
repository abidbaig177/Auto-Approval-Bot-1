from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
import random, asyncio
from configs import cfg
    
    API_ID="14055090"
    BOT_TOKEN="6235334259:AAFJLg1nCLYrBqoc8LtvsTDG_JOTIeMxK7I"
    API_HASH="a46f7b439d0afa45b7a69fc450f754e9"
    
app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

ABOUT = """ 
☃️**About This Bot**☃️
💠Commands : [Click Here](https://t.me/Kristen_Updates/15)
🍁Bot created by @Kristen_Updates+
📦Source Code : [Click Here](https://github.com/NomoreLakshya/Auto-Approval-Bot)
☘️Framework : [Pyrogram](docs.pyrogram.org)
🔰Language : [Python](www.python.org)
🧑‍💻Developer : @CallmeLakshya
🆘Support : [𝐊ʀɪ⃯֟𝐬ʈɜɴᥫ᭡](https://t.me/Kristen_Support)
"""


gif = [
    'https://telegra.ph/file/c4ea3761bb73bab726334.jpg',
    'https://telegra.ph/file/c4ea3761bb73bab726334.jpg',
    'https://telegra.ph/file/c4ea3761bb73bab726334.jpg',
    'https://telegra.ph/file/c4ea3761bb73bab726334.jpg',
    'https://telegra.ph/file/c4ea3761bb73bab726334.jpg'
]


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(_, m : Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        img = random.choice(gif)
        await app.send_video(kk.id,img, "✌**Hello {}!\n\n I m Auto Approve Bot.**\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\n⚡️Powerd By @Itzz_Mickey ".format(m.from_user.mention, m.chat.title))
        add_user(kk.id)
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))    
 
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ About ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("about"))
async def help(bot, message):
  await message.reply_photo("https://telegra.ph/file/c4ea3761bb73bab726334.jpg",caption=ABOUT,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="𝐊ʀɪ⃯֟𝐬ʈɜɴᥫ᭡", url="t.me/Kristen_Updates")]]))

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("start"))
async def op(_, m :Message):
    try:
        await app.get_chat_member(cfg.CHID, m.from_user.id) 
        if m.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗯 Channel", url="https://t.me/Kristen_Updates"),
                        InlineKeyboardButton("💬 Support", url="https://t.me/Kristen_Support")
                    ],
                    [
                        InlineKeyboardButton("🧩 Repo ", url="https://github.com/NomoreLakshya/Auto-Approval-Bot"),
                        InlineKeyboardButton("💻 Devoloper ", url=f"tg://user?id=5776889746")
                    ],
                    [
                        InlineKeyboardButton("➕ Add me to your Chat ➕", url="https://t.me/Ku_Approve_Bot?startgroup")
                    ]
                ]
            )
            add_user(m.from_user.id)
            await m.reply_photo("https://telegra.ph/file/c4ea3761bb73bab726334.jpg", caption="**🕊️ Hello {}!\nI'm an auto approve [Admin Join Requests]({}) Bot.\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\n 🔰 Powerd By [𝐊ʀɪ⃯֟𝐬ʈɜɴᥫ᭡](t.me/Kristen_Updates)**".format(m.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard)
    
        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💁‍♂️ Start me private 💁‍♂️", url="https://t.me/Ku_Approve_Bot?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text("**🦊 Hello {}!\n Write me private for more details**".format(m.from_user.first_name), reply_markup=keyboar)
        print(m.from_user.first_name +" Is started Your Bot!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Check Again 🍀", "chk")
                ]
            ]
        )
        await m.reply_text("**⚠️Access Denied!⚠️\n\nPlease Join @{} to use me.If you joined click check again button to confirm.** \n\n".format(cfg.FSUB), reply_markup=key)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb : CallbackQuery):
    try:
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗯 Channel", url="https://t.me/Kristen_Updates"),
                        InlineKeyboardButton("💬 Support", url="https://t.me/Kristen_Support")
                    ],
                    [
                        InlineKeyboardButton("🧩 Repo", url="https://github.com/NomoreLakshya/Auto-Approval-Bot"),
                        InlineKeyboardButton("💻 Devolopers", url=f"tg://user?id=5776889746")
                    ],
                    [
                        InlineKeyboardButton("➕ Add me to your Chat ➕", url="https://t.me/Ku_Approve_Bot?startgroup=true")
                    ]
                ]
            )
            add_user(cb.from_user.id)
            await cb.message.edit("**🦊 Hello {}!\n\nI m Auto Approve Bot.**\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\n⚡️Powerd By @Kristen_Updates**".format(cb.from_user.mention, "https://t.me/Kristen_Updates"), reply_markup=keyboard, disable_web_page_preview=True)
        print(cb.from_user.first_name +" Is started Your Bot!")
    except UserNotParticipant:
        await cb.answer("🙅‍♂️ You are not joined to channel join and try again. 🙅‍♂️")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users. \n\n ⚠️ Warning :- Don't Boardcast Everyday ")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Fcast Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

print("Starting..")
print("Checking Code Erorrs..!")
print("Bot Running..")
print("Bot Started")
app.run()
