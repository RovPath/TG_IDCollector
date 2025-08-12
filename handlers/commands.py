from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

router = Router()


@router.message(CommandStart())
async def start_bot(message: Message):
    text = "🆔 <b>Telegram ID-Collector</b>\n\n" "Привет! Я помогу тебе получить <b>ID</b> любого контента в Telegram\n"
    await message.answer(text=text, parse_mode="HTML")


# @router.message(Command("help"))
# async def myid_command(message: Message):
#     text = ""


@router.message(Command("myid"))
async def myid_command(message: Message):

    username = f"@{message.from_user.username}" if message.from_user.username else "❌ N/A"
    last_name = message.from_user.last_name if message.from_user.last_name else "❌ N/A"

    text = (
        "📋 <b>Ваши идентификаторы</b>\n"
        "┌──────────────────\n"
        f"│ 👤 <b>Ваш личный ID:</b> <code>{message.from_user.id}</code>\n"
        f"│ 👥 <b>Username:</b> {username}\n"
        f"│ 📝 <b>Имя:</b> {message.from_user.first_name}\n"
        f"│ 📝 <b>Фамилия:</b> {last_name}\n"
        f"│ 💬 <b>ID этого чата:</b> <code>{message.chat.id}</code>\n"
        f"│ 🏷 <b>Тип чата:</b> {message.chat.type}\n"
        f"│ ✉️ <b>ID сообщения:</b> <code>{message.message_id}</code>\n"
        "└──────────────────"
    )
    await message.answer(text=text, parse_mode="HTML")


@router.message(Command("chatid"))
async def chatid_command(message: Message):
    chat = message.chat
    chat_title = "❌ N/A"  # Значение по умолчанию
    if chat.type == "private":  # ниже объединяем имя и фамилию, удаляя лишние пробелы
        chat_title = f"{chat.first_name or ''} {chat.last_name or ''}".strip()

    # fmt: off
    #проверяем, есть ли у объекта chat атрибут title и проверяем, что title не пустой
    elif hasattr(chat, "title") and chat.title:
        chat_title = chat.title

    # проверяем, есть ли у чата атрибут username и проверяем, что username не пустой
    chat_username = "❌ N/A"  # Значение по умолчанию
    if hasattr(chat, "username") and chat.username:
        chat_username = f"@{chat.username}"
    # fmt: on

    text = (
        "📋 <b>Полная информация о чате</b>\n"
        "┌──────────────────\n"
        f"│ 💬 <b>ID чата:</b> <code>{chat.id}</code>\n"
        f"│ 🏷 <b>Тип чата:</b> {chat.type}\n"
        f"│ 📝 <b>Название:</b> {chat_title}\n"
        f"│ 👤 <b>Username:</b> {chat_username}\n"
        f"│ ✉️ <b>ID сообщения:</b> <code>{message.message_id}</code>\n"
        "└──────────────────"
    )

    await message.answer(text=text, parse_mode="HTML")
