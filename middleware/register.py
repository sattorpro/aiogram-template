from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Update
from typing import Callable, Awaitable, Any, Dict
from database.models import User

class RegisterMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any]
    ) -> Any:
        user_object = event.message.from_user if event.message else event.callback_query.from_user if event.callback_query else event.my_chat_member.from_user if event.my_chat_member else None
        if not user_object:
            return await handler(event, data)
        
        user_id = user_object.id
        user = await User.get_or_none(user_id=user_id)
        if not user:
            user = await User.create(
                user_id=user_id,
                defaults=dict(
                    authorized=False,
                    authorization_token=None
                )
            )

        data['user'] = user
        return await handler(event, data)