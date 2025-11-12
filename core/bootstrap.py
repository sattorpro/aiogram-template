from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage
from core.config import settings


bot = Bot(
    token=settings.TELEGRAM_BOT_TOKEN.get_secret_value(),
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML,
    )
)

storage = RedisStorage.from_url(settings.REDIS_CONNECTION_URL)
dispatcher = Dispatcher(storage=storage)