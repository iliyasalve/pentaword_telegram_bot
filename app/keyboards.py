from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils import t

def lang_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("English 🇬🇧", callback_data="lang_en")],
        [InlineKeyboardButton("Русский 🇷🇺", callback_data="lang_ru")],
        [InlineKeyboardButton("Français 🇫🇷", callback_data="lang_fr")]
    ])

def diff_buttons(lang_code):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🟢 " + t(lang_code, "easy"), callback_data="diff_easy")],
        [InlineKeyboardButton("🟡 " + t(lang_code, "medium"), callback_data="diff_medium")],
        [InlineKeyboardButton("🔴 " + t(lang_code, "hard"), callback_data="diff_hard")],
    ])

def post_game_buttons(lang_code):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔁 " + t(lang_code, "play_again"), callback_data="restart")],
        [InlineKeyboardButton("🌍 " + t(lang_code, "change_lang"), callback_data="change_lang")]
    ])

def guess_buttons(lang_code):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(t(lang_code, "cancel"), callback_data="cancel")]
    ])
