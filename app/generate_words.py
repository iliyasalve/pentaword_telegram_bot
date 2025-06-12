import requests
import os

# Path to the project root
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


"""
This script downloads frequency-based word lists from the HermitDave/FrequencyWords project,
licensed under CC BY-SA 4.0. See https://github.com/hermitdave/FrequencyWords
"""
LANG_CONFIGS = {
    "ru": {
        "freq_url": "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/ru/ru_50k.txt",
        "encoding": "utf-8"
    },
    "en": {
        "freq_url": "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/en/en_50k.txt",
        "encoding": "utf-8"
    },
    "fr": {
        "freq_url": "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/fr/fr_50k.txt",
        "encoding": "utf-8"
    }
}

def download_freq_list(url, filename, encoding="utf-8"):
    print(f"Downloading {filename}...")
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, "w", encoding=encoding) as f:
        f.write(response.text)

def load_freq(filename, word_length, encoding="utf-8"):
    words = []
    with open(filename, encoding=encoding) as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                word = parts[0].lower()
                if len(word) == word_length and word.isalpha():
                    words.append((word, int(parts[1])))
    return words

def generate_wordlists(lang_code, word_length=5):
    if lang_code not in LANG_CONFIGS:
        raise ValueError(f"Language '{lang_code}' is not supported.")
    
    config = LANG_CONFIGS[lang_code]

    # Create directory for the wordlists if it doesn't exist
    #dir_path = os.path.join("words", lang_code)
    dir_path = os.path.join(BASE_DIR, "data", "words", lang_code)
    os.makedirs(dir_path, exist_ok=True)

    freq_filename = os.path.join(dir_path, f"{lang_code}_freq.txt")
    download_freq_list(config["freq_url"], freq_filename, encoding=config["encoding"])

    words_with_freq = load_freq(freq_filename, word_length, encoding=config["encoding"])
    total_words = len(words_with_freq)
    print(f"Total {word_length}-letter words for language '{lang_code}': {total_words}")

    # Sort words by descending frequency
    sorted_words = sorted(words_with_freq, key=lambda x: x[1], reverse=True)

    easy_cutoff = int(total_words * 0.3)
    medium_cutoff = int(total_words * 0.6)

    easy = [w for w, c in sorted_words[:easy_cutoff]]
    medium = [w for w, c in sorted_words[easy_cutoff:medium_cutoff]]
    hard = [w for w, c in sorted_words[medium_cutoff:]]

    # Save lists to appropriate folder
    with open(os.path.join(dir_path, f"{lang_code}_easy.txt"), "w", encoding=config["encoding"]) as f:
        f.write("\n".join(easy))
    with open(os.path.join(dir_path, f"{lang_code}_medium.txt"), "w", encoding=config["encoding"]) as f:
        f.write("\n".join(medium))
    with open(os.path.join(dir_path, f"{lang_code}_hard.txt"), "w", encoding=config["encoding"]) as f:
        f.write("\n".join(hard))

    print(f"Wordlists for language '{lang_code}' have been successfully created in folder '{dir_path}'!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script.py <language_code>")
        print("Supported languages:", ", ".join(LANG_CONFIGS.keys()))
        sys.exit(1)

    language = sys.argv[1]
    generate_wordlists(language)
