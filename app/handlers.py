from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from utils import t, load_word_list, evaluate_guess
from keyboards import lang_buttons, diff_buttons, post_game_buttons, guess_buttons
from config import LANGUAGE, DIFFICULTY, GUESS, MAX_ATTEMPTS
import random

sessions = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang_code = (update.effective_user.language_code or "en").lower()
    if lang_code not in ['en', 'ru', 'fr']:
        lang_code = "en"
    context.user_data["lang_code"] = lang_code
    await update.message.reply_text(t(lang_code, "welcome"), reply_markup=lang_buttons())
    return LANGUAGE

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang_code = context.user_data.get("lang_code", "en")
    user_id = query.from_user.id

    # Cancel button
    if query.data == "cancel":
        if user_id in sessions:
            del sessions[user_id]
        context.user_data.clear()
        context.user_data["lang_code"] = lang_code
        await query.edit_message_text(t(lang_code, "cancelled"), reply_markup=lang_buttons())
        return LANGUAGE

    # Language selection
    if query.data.startswith("lang_"):
        language = query.data.split("_")[1]
        context.user_data["language"] = language
        context.user_data["lang_code"] = language  # sync interface language
        if user_id in sessions:
            del sessions[user_id]
        await query.edit_message_text(t(language, "choose_difficulty"), reply_markup=diff_buttons(language))
        return DIFFICULTY

    # Difficulty selection
    if query.data.startswith("diff_"):
        difficulty = query.data.split("_")[1]
        context.user_data["difficulty"] = difficulty
        language = context.user_data.get("language", "en")

        words = load_word_list(language, difficulty)
        secret_word = random.choice(words)
        sessions[user_id] = {
            "word": secret_word,
            "attempts": 0,
            "max_attempts": MAX_ATTEMPTS,
            "words": words
        }
        await query.edit_message_text(t(language, "word_length_info", n=len(secret_word)), reply_markup=guess_buttons(language))
        return GUESS

    # Play again
    if query.data == "restart":
        if user_id in sessions:
            del sessions[user_id]
        lang = context.user_data.get("lang_code", "en")
        await query.message.reply_text(t(lang, "choose_difficulty"), reply_markup=diff_buttons(lang))
        return DIFFICULTY

    # Change language
    if query.data == "change_lang":
        if user_id in sessions:
            del sessions[user_id]
        lang = context.user_data.get("lang_code", "en")
        context.user_data.clear()
        context.user_data["lang_code"] = lang
        await query.message.reply_text(t(lang, "welcome"), reply_markup=lang_buttons())
        return LANGUAGE

    # Unknown callback fallback
    await query.answer()
    return ConversationHandler.END

async def handle_guess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang_code = context.user_data.get("lang_code", "en")
    session = sessions.get(user_id)

    if not session:
        await update.message.reply_text(t(lang_code, "cancelled"))
        return ConversationHandler.END

    guess = update.message.text.strip().lower()
    word_length = len(session["word"])

    if len(guess) != word_length:
        await update.message.reply_text(t(lang_code, "wrong_length", n=word_length), reply_markup=guess_buttons(lang_code))
        return GUESS
    if guess not in session["words"]:
        await update.message.reply_text(t(lang_code, "not_in_dict"), reply_markup=guess_buttons(lang_code))
        return GUESS

    session["attempts"] += 1
    result = evaluate_guess(session["word"], guess)
    await update.message.reply_text(result)

    if guess == session["word"]:
        await update.message.reply_text(t(lang_code, "correct"), reply_markup=post_game_buttons(lang_code))
        del sessions[user_id]
        return LANGUAGE
    elif session["attempts"] >= session["max_attempts"]:
        await update.message.reply_text(t(lang_code, "game_over", word=session["word"]), reply_markup=post_game_buttons(lang_code))
        return LANGUAGE
    else:
        remaining = session["max_attempts"] - session["attempts"]
        await update.message.reply_text(t(lang_code, "attempts_left", n=remaining), reply_markup=guess_buttons(lang_code))
        return GUESS

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang_code = context.user_data.get("lang_code", "en")
    await update.message.reply_text(t(lang_code, "cancelled"))
    return ConversationHandler.END
