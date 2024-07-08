from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters
import time
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

toke = ""

async def start(update: Update, context: CallbackContext):
    user = update.message.from_user.first_name
    text = f'''
Hello {user}! I am a bot designed to assist you in gaining insights into your mental well-being. Through a series of questions, you can explore whether you may be experiencing symptoms of conditions like depression or ADHD.

It's important to note that I am not a medical professional, and I cannot provide an official diagnosis. My responses are based on your answers, and for a precise diagnosis, I recommend consulting a qualified healthcare professional. Your mental health is valuable, and I encourage you to seek professional guidance if needed. Please use this information as a supportive resource rather than a definitive assessment.
'''
    await update.message.reply_text(text)
    time.sleep(2)
    await update.message.reply_text("Let's get started! I will ask you a series of questions, and you can respond with a number from 1 to 5, where 1 means 'not at all' and 5 means 'extremely'.")
    await update.message.reply_text("Do you agree? (yes/no)")

async def answers(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data="1"),
            InlineKeyboardButton("2", callback_data="2"),
            InlineKeyboardButton("3", callback_data="3"),
            InlineKeyboardButton("4", callback_data="4"),
            InlineKeyboardButton("5", callback_data="5")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose a number:", reply_markup=reply_markup)

def main():
    app = Application.builder().token(toke).build()
    try:
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & filters.regex("^(yes|no)$"), answers))
        app.run_polling(1)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()

