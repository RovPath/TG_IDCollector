from typing import Dict
from aiogram.types import Message

last_messages_cache: Dict[int, Message] = {}  # {chat_id: last_message}
