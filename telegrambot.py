import telebot
from deep_translator import GoogleTranslator

bot = telebot.TeleBot('8506596674:AAFiuWUirEJrnmRvWnjnUPZP7-75WAao9GM')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
        "🌍 Привет! Я бот-переводчик\n"
        "Напиши текст и укажи язык через пробел:\n"
        "en Привет\n"
        "ru Hello\n"
        "de Good morning\n"
        "es How are you?\n\n"
        "Доступные языки: en, ru, de, fr, es, it, zh, ja")

@bot.message_handler(func=lambda message: True)
def translate(message):
    try:
        parts = message.text.split(' ', 1)
        if len(parts) < 2:
            bot.reply_to(message, 
                "❌ Укажи язык и текст, например:\n"
                "en Привет")
            return

        target_lang = parts[0].strip()
        text = parts[1].strip()

        # Перевод через deep_translator
        result = GoogleTranslator(source='auto', target=target_lang).translate(text)

        bot.reply_to(message,
            f"🌐 Перевод на {target_lang}:\n\n"
            f"📝 Было: {text}\n\n"
            f"✅ Стало: {result}")

    except Exception as e:
        bot.reply_to(message, f"❌ Ошибка: {str(e)}")

bot.infinity_polling()