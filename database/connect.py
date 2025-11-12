from tortoise import Tortoise
from core.config import settings

class Connector:
    @staticmethod
    async def connect():
        await Tortoise.init(
            config=dict(
                connections=dict(default=settings.DATABASE_CONNECTION_URL),
                apps=dict(
                    models=dict(
                        models=[
                            "database.models",
                        ],
                        default_connection="default",
                    )
                )
            )
        )
        await Tortoise.generate_schemas(safe=True)

    @staticmethod
    async def disconnect():
        await Tortoise.close_connections()