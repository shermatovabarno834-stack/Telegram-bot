import logging
from aiogram import Bot, Dispatcher, executor, types

# Siz bergan yangi token
TOKEN = "9050259079:AAH5xhCPSnDZf9nAGD-TSRq-ZwVeRIEAOeE"

# Siz bergan ID (Admin ID)
ADMIN_ID = 1130978177

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# /start buyrug'i
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Bot va admin panel muvaffaqiyatli ishga tushdi! 🚀")

# Admin panelni ochish buyrug'i (/admin)
@dp.message_handler(commands=['admin'])
async def open_admin_panel(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        # Admin uchun maxsus klaviatura tugmalari
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton("📊 Statistika"), types.KeyboardButton("📢 Xabar tarqatish"))
        keyboard.add(types.KeyboardButton("⬅️ Asosiy menyu"))
        
        await message.answer("Xush kelibsiz, Admin! Kerakli bo'limni tanlang:", reply_markup=keyboard)
    else:
        await message.reply("Kechirasiz, sizda bu buyruqdan foydalanish huquqi yo'q. ❌")

# Admin tugmalari uchun matnli handlerlar
@dp.message_handler(text="📊 Statistika")
async def admin_stats(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("👥 Botdagi jami foydalanuvchilar: 1 ta (test rejimida)")

@dp.message_handler(text="📢 Xabar tarqatish")
async def admin_broadcast(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("Tarqatmoqchi bo'lgan xabaringizni yuboring (hozircha ishlab chiqilmoqda).")

@dp.message_handler(text="⬅️ Asosiy menyu")
async def back_to_main(message: types.Message):
    # Klaviaturani yopish
    remove_kb = types.ReplyKeyboardRemove()
    await message.answer("Asosiy menyuga qaytdingiz.", reply_markup=remove_kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
  
