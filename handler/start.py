from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, StateFilter

router = Router()

@router.message(StateFilter("*"), Command("help"))
async def start_command_handler(message: Message) -> None:
    await message.reply(
        text="Xush kelibsiz! Siz allaqachon tizimga kirgansiz."
    )
