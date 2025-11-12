import asyncio
import logging


from core.bootstrap import bot, dispatcher
from database.connect import Connector

from middleware.register import RegisterMiddleware

from handler import start

async def main() -> None:
    try:
        await Connector.connect()

        dispatcher.update.middleware.register(RegisterMiddleware())

        dispatcher.include_router(start.router)
        await dispatcher.start_polling(bot)
    finally:
        await Connector.disconnect()
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    asyncio.run(main())