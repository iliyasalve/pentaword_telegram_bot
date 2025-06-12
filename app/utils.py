import os
import json
import random

# Path to the project root
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Load translations once
TRANSLATIONS_PATH = os.path.join(BASE_DIR, "data", "translations.json")
with open(TRANSLATIONS_PATH, encoding="utf-8") as f:
    TRANSLATIONS = json.load(f)

def t(lang_code, key, **kwargs):
    lang = lang_code if lang_code in TRANSLATIONS else "en"
    return TRANSLATIONS[lang].get(key, f"[{key}]").format(**kwargs)

def load_word_list(language, difficulty):
    levels = []

    if difficulty == "easy":
        levels = ["easy"]
    elif difficulty == "medium":
        levels = ["easy", "medium"]
    elif difficulty == "hard":
        levels = ["easy", "medium", "hard"]
    else:
        raise ValueError(f"Unknown difficulty level: {difficulty}")

    words = []
    for level in levels:
        path = os.path.join(BASE_DIR, "data", "words", language, f"{language}_{level}.txt")
        if not os.path.exists(path):
            raise FileNotFoundError(f"Word list not found: {path}")
        with open(path, encoding="utf-8") as f:
            words += [line.strip().lower() for line in f if line.strip()]
    
    return words

def evaluate_guess(secret, guess):
    result = ["⬜"] * len(secret)
    secret_chars = list(secret)  # List of letters of the secret word

    # First, mark the correct letters (green)
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            result[i] = "🟩"
            secret_chars[i] = None  # "Remove" the letter so it’s not counted twice

    # Then check the yellow letters (letters present but in a different position)
    for i in range(len(secret)):
        if result[i] == "⬜":  # if not already marked
            if guess[i] in secret_chars:
                result[i] = "🟨"
                # Remove the first encountered letter from secret_chars to avoid counting it again
                secret_chars[secret_chars.index(guess[i])] = None

    return "".join(result)