import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import ChatJoinRequest, Message
from aiogram.filters import Command

API_TOKEN = "8212258017:AAHpCj1bQdzLtezuHs2sCAO83wqkTBoXFmw"
ADMIN_ID = 1860816111

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.chat_join_request()
async def approve_request(join_request: ChatJoinRequest):
    user = join_request.from_user

    await join_request.approve()

    await bot.send_message(
        ADMIN_ID,
        f"✅ Принят пользователь\n"
        f"👤 {user.full_name}\n"
        f"🆔 {user.id}\n"
        f"🔗 @{user.username if user.username else 'нет'}"
    )

@dp.message(F.text.lower() == "пров")
async def check_bot(message: Message):
    await message.answer("Бот работает ✅")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())