from aiogram import Router, F
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
    # Handle optional fields
    username = f"@{message.from_user.username}" if message.from_user.username else "❌ Не указан"
    last_name = message.from_user.last_name if message.from_user.last_name else "❌ Не указана"

    text = (
        "📋 <b>Ваши идентификаторы</b>\n\n"
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
