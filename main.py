from os import environ
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest
    
app = Client(
    "Auto Approval Bot",
    bot_token = environ["BOT_TOKEN"],
    api_id = int(environ["API_ID"]),
    api_hash = environ["API_HASH"]
)


CHAT_ID = [int(app) for app in environ.get("CHAT_ID", None).split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour Auto Approved")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

@app.on_message(filters.private & filters.command(["start"]))
async def start(client: app, message: Message):
    approvedbot = await client.get_me() 
    button = [[ InlineKeyboardButton("🕹 Developer", url="https://t.me/CallmeLakshya"), InlineKeyboardButton("Updates 📢", url="t.me/Kristen_Updates") ],
              [ InlineKeyboardButton("➕️ Add Me To Your Chat ➕️", url=f"http://t.me/{approvedbot.username}?startgroup=botstart") ]]
    await client.send_message(chat_id=message.chat.id, text=f"**Hello {message.from_user.mention} Iam Auto Approver Join Request Bot Just Add Me To Your Group**", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@app.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client: app, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} Joined 🤝") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))
    #   print("Welcome....")

print("Auto Approved Bot")
app.run()
