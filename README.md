# 🌍 Telegram Bot

Welcome to the **Telegram Bot** project! This bot leverages the
power of [Hugging Face Transformers](https://huggingface.co/transformers/) to
provide multilingual NLP services directly through Telegram. 🤖

## 📜 Table of Contents

- [About](#about)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)

## 📖 About

This project combines the Telegram API with cutting-edge language models to
create an interactive and multilingual experience for users. The bot can be
easily deployed using Docker, making it suitable even for devices like
a Raspberry Pi! 🥧

## ✨ Features

- Multilingual text classification using BERT-based models 🌐
- Seamless integration with Telegram's messaging platform 📱
- Lightweight and portable with Docker support 🐳
- Customizable and extendable to include more NLP tasks 🔄

## 🚀 Setup

### Prerequisites

- Docker installed 🐳
- Python 3.9 and virtual environment tools
- Telegram bot token (get it from
  [@BotFather](https://core.telegram.org/bots#botfather)) 🔑

### Instructions

1. **Clone this repository**

   ```bash
   git clone https://github.com/EHER/telegram_bot.git
   cd telegram_bot
   ```

2. **Setup the environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Environment Variables**

   Rename `.env.dist` to `.env` in the root directory and add your Telegram API token:

   `.env.dist` example:

   ```
   TELEGRAM_TOKEN=your_telegram_bot_token
   ```

4. **Build and Run Docker Container**

   ```bash
   docker build -t telegram-bot .
   docker run --env-file .env telegram-bot
   ```

## 🎯 Usage

- Start the bot with `/start` and send any message to receive information
  processed by our multilingual AI model! 💬
- The command-line interface lets you test the AI responses directly by
  running:

  ```bash
  python model.py "Your text here"
  ```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE)
file for details. 📄

## 🤝 Contributing

Contributions are what make the community such an amazing place to learn,
inspire, and create. Any contributions you make are **greatly appreciated**.
Please feel free to fork the project and submit pull requests. 🔧
