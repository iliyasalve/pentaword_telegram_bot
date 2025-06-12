import os
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, ConversationHandler, filters
from handlers import start, handle_callback, handle_guess, cancel
from config import LANGUAGE, DIFFICULTY, GUESS

def main():
    from dotenv import load_dotenv
    load_dotenv()

    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        print("ERROR: TELEGRAM_BOT_TOKEN not set in environment")
        return

    app = Application.builder().token(token).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            LANGUAGE: [CallbackQueryHandler(handle_callback)],
            DIFFICULTY: [CallbackQueryHandler(handle_callback)],
            GUESS: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, handle_guess),
                CallbackQueryHandler(handle_callback)
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        allow_reentry=True
    )

    app.add_handler(conv_handler)
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
