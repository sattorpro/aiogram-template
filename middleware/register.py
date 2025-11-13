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
        obj = event.message if event.message else event.callback_query.message if event.callback_query else event.my_chat_member if event.my_chat_member else None
        if not obj:
            return await handler(event, data)
        
        user_id = obj.from_user.id
        chat_type = obj.chat.type
        user = await User.get_or_none(user_id=user_id)
        if not user:
            user = await User.create(
                user_id=user_id,
                chat_type=chat_type
            )

        data['user'] = user
        return await handler(event, data)
