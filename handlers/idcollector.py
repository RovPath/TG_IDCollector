from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.photo | F.video | F.document | F.audio | F.voice | F.video_note)
async def handle_media_files(message: Message):
    if message.photo:
        photo = message.photo[-1]
        text = (
            f"📸 <b>{message.content_type}</b>\n"
            f"🆔 <b>ID:</b> <code>{photo.file_id}</code>\n"
            f"📏 <b>Размер:</b> {photo.width}x{photo.height}"
        )
    elif message.video:
        text = (
            f"🎥 <b>{message.content_type}</b>\n"
            f"🆔 <b>ID:</b> <code>{message.video.file_id}</code>\n"
            f"⏱ <b>Длительность:</b> {message.video.duration} сек\n"
            f"📏 <b>Разрешение:</b> <code>{message.video.width}x{message.video.height}</code>"
        )
    elif message.document:
        text = (
            f"📄 <b>{message.content_type}</b>\n"
            f"🆔 <b>ID:</b> <code>{message.document.file_id}</code>\n"
            f"📝 <b>Имя файла:</b> {message.document.file_name or 'N/A'}"
        )
    elif message.audio:
        text = (
            f"🎵 <b>{message.content_type}</b>\n"
            f"🆔 <b>ID:</b> <code>{message.audio.file_id}</code>\n"
            f"⏱ <b>Длительность:</b> {message.audio.duration} сек\n"
            f"🎤 <b>Исполнитель:</b> {message.audio.performer or 'N/A'}\n"
            f"📝 <b>Название:</b> {message.audio.title or 'N/A'}"
            f"\n📁 <b>Имя файла:</b> {message.audio.file_name or 'N/A'}"
        )
    elif message.voice:
        text = (
            f"🎤 <b>{message.content_type}</b>\n"
            f"🆔 <b>ID:</b> <code>{message.voice.file_id}</code>\n"
            f"⏱ <b>Длительность:</b> {message.voice.duration} сек"
        )
    elif message.video_note:
        text = (
            f"🎬 <b>{message.content_type}</b>\n"
            f"🆔 <b>ID:</b> <code>{message.video_note.file_id}</code>\n"
            f"⏱ <b>Длительность:</b> {message.video_note.duration} сек\n"
            f"📏 <b>Размер:</b> {message.video_note.length}x{message.video_note.length}"
        )

    # Добавляем информацию о весе файла
    file_size = None
    if message.photo:
        file_size = message.photo[-1].file_size
    elif message.video:
        file_size = message.video.file_size
    elif message.document:
        file_size = message.document.file_size
    elif message.audio:
        file_size = message.audio.file_size
    elif message.voice:
        file_size = message.voice.file_size
    elif message.video_note:
        file_size = message.video_note.file_size

    if file_size:
        text += f"\n📦 <b>Вес:</b> {file_size // 1024} KB"

    # Добавляем подпись (если есть)
    if message.caption:
        text += f"\n📝 <b>Подпись:</b> {message.caption}"

    await message.reply(text=text, parse_mode="HTML")
