# PentaWord Telegram Bot

[English](#english) | [Français](#français) | [Русский](#русский)

---

## English

### 🎯 Description

Telegram bot — a word guessing game supporting three languages and multiple difficulty levels.

The player tries to guess a word of a given length within a limited number of attempts.
Each guess is evaluated and the bot responds with emoji hints:

* 🟩 — letter in the correct position
* 🟨 — letter is in the word but in a different position
* ⬜ — letter is not in the word

The user selects the interface language and dictionary (English, Russian, or French), as well as the difficulty level (easy, medium, hard).

---

### 🚀 Installation and Running

1. Clone the repository and navigate to the project root folder:

   ```bash
   git clone <repo-url>
   cd PentaWord_Telegram_Bot
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Prepare word lists for required languages:

   ```bash
   python app/generate_wordlists.py ru
   python app/generate_wordlists.py en
   python app/generate_wordlists.py fr
   ```

5. Create a `.env` file in the root of `PentaWord_Telegram_Bot` and add your Telegram bot token:

   ```
   TELEGRAM_BOT_TOKEN=your_bot_token
   ```

6. Run the bot:

   ```bash
   python app/main.py
   ```

---

### 🎮 Usage

* Send the `/start` command in Telegram to begin the game.
* Choose the interface language.
* Choose the difficulty level.
* Enter a guess word of the required length.
* Follow hints and try to guess the word within limited attempts.
* After winning or losing, you can play again or change language.
* At any time, press the **Cancel** button to abort the current session.

---

### 🗂 Project Structure

```
PentaWord_Telegram_Bot/
├── app/
│   ├── main.py
│   ├── handlers.py
│   ├── keyboards.py
│   ├── utils.py
│   ├── config.py
│   ├── generate_wordlists.py
│   └── ...
├── data/
│   ├── words/
│   │   ├── en/
│   │   ├── ru/
│   │   └── fr/
│   └── translations.json
├── .env
├── requirements.txt
└── README.md
```

---

### 📚 Word Sources

Word lists for English, Russian, and French were generated using data from the [HermitDave/FrequencyWords](https://github.com/hermitdave/FrequencyWords) project, which provides frequency word lists based on large-scale text analysis. The 2018 versions were used:

* 🇷🇺 Russian: [`ru_50k.txt`](https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/ru/ru_50k.txt)
* 🇬🇧 English: [`en_50k.txt`](https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/en/en_50k.txt)
* 🇫🇷 French: [`fr_50k.txt`](https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/fr/fr_50k.txt)

The frequency word data is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
Original content author: [HermitDave](https://github.com/hermitdave).

In this project, words were filtered and categorized by length and difficulty to fit the game mechanics.

---

### ✅ Planned Improvements

* ⏱ **Turn timer** — automatic session termination if the player does not respond for a long time (e.g., 5 minutes).
* 💬 **`/help` command** — a brief game guide with examples and commands.
* 📊 **Player statistics storage** — total wins and losses, average attempts.
* 🏆 **Achievements system** — rewards for special results (e.g., "Guessed on first try," "3 wins in a row").
* 🚀 **In-memory caching of word lists on startup** — loading all dictionaries once for better performance.
* 📦 **Storing words in SQLite or JSON** — speeding up searching and filtering by length, difficulty, and language.

---

### License

* The project source code is licensed under the MIT License.
* Word lists and frequency data are provided by the [HermitDave/FrequencyWords](https://github.com/hermitdave/FrequencyWords) project and distributed under the [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) license.
* Use of the data requires compliance with the CC BY-SA 4.0 terms, including attribution and license preservation on redistribution.

---

## Français

### 🎯 Description

Bot Telegram — un jeu de devinettes de mots avec prise en charge de trois langues et plusieurs niveaux de difficulté.

Le joueur doit deviner un mot d’une longueur donnée en un nombre limité de tentatives.
Chaque proposition est évaluée et le bot répond avec des indices sous forme d’émojis :

* 🟩 — lettre à la bonne position
* 🟨 — lettre présente dans le mot, mais à une autre position
* ⬜ — lettre absente du mot

L’utilisateur choisit la langue de l’interface et du dictionnaire (anglais, russe ou français), ainsi que le niveau de difficulté (facile, moyen, difficile).

---

### 🚀 Installation et lancement

1. Clonez le dépôt et allez dans le dossier racine du projet :

   ```bash
   git clone <url-du-dépôt>
   cd PentaWord_Telegram_Bot
   ```

2. Créez et activez un environnement virtuel (recommandé) :

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

4. Préparez les listes de mots pour les langues nécessaires :

   ```bash
   python app/generate_wordlists.py ru
   python app/generate_wordlists.py en
   python app/generate_wordlists.py fr
   ```

5. Créez un fichier `.env` à la racine de `PentaWord_Telegram_Bot` et ajoutez votre token Telegram :

   ```
   TELEGRAM_BOT_TOKEN=votre_token_bot
   ```

6. Lancez le bot :

   ```bash
   python app/main.py
   ```

---

### 🎮 Utilisation

* Envoyez la commande `/start` dans Telegram pour commencer la partie.
* Choisissez la langue de l’interface.
* Choisissez le niveau de difficulté.
* Entrez un mot à deviner de la longueur requise.
* Suivez les indices et essayez de deviner le mot en un nombre limité de tentatives.
* Après une victoire ou une défaite, vous pouvez rejouer ou changer de langue.
* À tout moment, appuyez sur le bouton **Annuler** pour interrompre la session en cours.

---

### 🗂 Structure du projet

```
PentaWord_Telegram_Bot/
├── app/
│   ├── main.py
│   ├── handlers.py
│   ├── keyboards.py
│   ├── utils.py
│   ├── config.py
│   ├── generate_wordlists.py
│   └── ...
├── data/
│   ├── words/
│   │   ├── en/
│   │   ├── ru/
│   │   └── fr/
│   └── translations.json
├── .env
├── requirements.txt
└── README.md
```

---

### 📚 Sources des listes de mots

Les listes de mots en anglais, russe et français ont été générées à partir des données du projet [HermitDave/FrequencyWords](https://github.com/hermitdave/FrequencyWords), qui fournit des listes de fréquence de mots basées sur une analyse textuelle à grande échelle. Les versions de 2018 ont été utilisées :

* 🇷🇺 Russe : [`ru_50k.txt`](https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/ru/ru_50k.txt)
* 🇬🇧 Anglais : [`en_50k.txt`](https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/en/en_50k.txt)
* 🇫🇷 Français : [`fr_50k.txt`](https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/fr/fr_50k.txt)

Les données de fréquence sont sous licence [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
Auteur original du contenu : [HermitDave](https://github.com/hermitdave).

Les mots ont été filtrés et classés par longueur et difficulté afin de correspondre à la mécanique du jeu.

---

### ✅ Améliorations prévues

* ⏱ **Minuteur par tour** — fin automatique de la session si le joueur ne répond pas pendant longtemps (par exemple 5 minutes).
* 💬 **Commande `/help`** — instructions brèves avec exemples et commandes.
* 📊 **Statistiques joueur sauvegardées** — total des victoires et défaites, nombre moyen d’essais.
* 🏆 **Système de succès** — récompenses pour des résultats particuliers (ex. « Deviné du premier coup », « 3 victoires d’affilée »).
* 🚀 **Mise en cache des mots en mémoire au démarrage** — chargement unique des dictionnaires pour améliorer les performances.
* 📦 **Stockage des mots en SQLite ou JSON** — accélération de la recherche et du filtrage par longueur, difficulté et langue.

---

### Licence

* Le code source du projet est sous licence MIT.
* Les listes de mots et données de fréquence sont fournies par le projet [HermitDave/FrequencyWords](https://github.com/hermitdave/FrequencyWords) et distribuées sous licence [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
* L’utilisation des données requiert le respect des conditions CC BY-SA 4.0, notamment la mention d’auteur et la conservation de la licence lors de la redistribution.

---

## Русский

### 🎯 Описание

Telegram-бот — игра в угадывание слов с поддержкой трёх языков и нескольких уровней сложности.

Игроку предлагается угадать слово заданной длины за ограниченное число попыток.  
Каждая догадка оценивается и бот отвечает подсказками в виде эмодзи:  
- 🟩 — буква на правильном месте  
- 🟨 — буква есть в слове, но в другой позиции  
- ⬜ — буква отсутствует в слове  

Пользователь выбирает язык интерфейса и словаря (английский, русский или французский), а также уровень сложности (лёгкий, средний, сложный).  

---

### 🚀 Установка и запуск

1. Клонируйте репозиторий и перейдите в корневую папку проекта:

   ```bash
   git clone <repo-url>
   cd PentaWord_Telegram_Bot
  ````

2. Создайте и активируйте виртуальное окружение (рекомендуется):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Подготовьте словари слов для нужных языков:

   ```bash
   python app/generate_wordlists.py ru
   python app/generate_wordlists.py en
   python app/generate_wordlists.py fr
   ```

5. Создайте файл `.env` в корне `PentaWord_Telegram_Bot` и добавьте в него токен Telegram-бота:

   ```
   TELEGRAM_BOT_TOKEN=ваш_токен_бота
   ```

6. Запустите бота:

   ```bash
   python app/main.py
   ```

---

### 🎮 Использование

* Отправьте команду `/start` в Telegram, чтобы начать игру.
* Выберите язык интерфейса.
* Выберите уровень сложности.
* Введите слово-угадку нужной длины.
* Следуйте подсказкам и попробуйте угадать слово за ограниченное число попыток.
* После победы или поражения можно сыграть снова или сменить язык.
* В любой момент игры нажмите на кнопку **Отмена**, чтобы прервать текущую сессию.

---

### 🗂 Структура проекта

```
PentaWord_Telegram_Bot/
├── app/
│   ├── main.py
│   ├── handlers.py
│   ├── keyboards.py
│   ├── utils.py
│   ├── config.py
│   ├── generate_wordlists.py
│   └── ...
├── data/
│   ├── words/
│   │   ├── en/
│   │   ├── ru/
│   │   └── fr/
│   └── translations.json
├── .env
├── requirements.txt
└── README.md
```

---

### 📚 Источники словарей

Списки слов для английского, русского и французского языков были сгенерированы с использованием данных из проекта [HermitDave/FrequencyWords](https://github.com/hermitdave/FrequencyWords), который предоставляет частотные словари на основе масштабного анализа текстов. Использованы версии 2018 года:

* 🇷🇺 Русский: [`ru_50k.txt`](https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/ru/ru_50k.txt)
* 🇬🇧 Английский: [`en_50k.txt`](https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/en/en_50k.txt)
* 🇫🇷 Французский: [`fr_50k.txt`](https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/fr/fr_50k.txt)

Данные по частотности слов лицензированы под [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
Автор оригинального контента: [HermitDave](https://github.com/hermitdave).

В проекте слова отфильтрованы и классифицированы по длине и уровню сложности для соответствия механике игры.

---

### ✅ Запланированные улучшения

* ⏱ **Таймер на ход** — автоматическое завершение сессии, если игрок долго не отвечает (например, 5 минут).
* 💬 **Команда `/help`** — краткая инструкция по игре с примерами и командами.
* 📊 **Сохраняемая статистика игрока** — общее количество побед и поражений, среднее число попыток.
* 🏆 **Система достижений** — награды за особые результаты (например, «Угадал с первой попытки», «3 победы подряд»).
* 🚀 **Кэширование слов в память при запуске** — загрузка всех словарей один раз для повышения производительности.
* 📦 **Хранение слов в SQLite или JSON** — ускорение поиска и фильтрации по длине, сложности и языку.

---

### Лицензия

- Исходный код проекта лицензирован под MIT License.
- Словари и частотные данные слов предоставлены проектом [HermitDave/FrequencyWords](https://github.com/hermitdave/FrequencyWords) и распространяются под лицензией [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
- Использование данных требует соблюдения условий CC BY-SA 4.0, включая указание авторства и сохранение лицензии при распространении.