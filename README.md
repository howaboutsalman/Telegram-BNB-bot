# 📊 Telegram-BNB-Bot (Study Case)

This is a simple Telegram bot built for educational and experimental purposes. It connects to the Binance API and allows users to check their crypto balances directly from a Telegram chat.

> ⚠️ **Disclaimer:**  
> This bot is a **study case project** created for learning and demonstration purposes only. It is **not secure** or production-ready and should **not** be used with real funds or deployed publicly without proper improvements.

---

## 💡 Features

- ✅ Get your **total Binance spot balance** in USDT  
- ✅ Request the balance of specific coins (like BTC, ETH, BNB, etc.)
- ✅ Simple Telegram commands and natural text handling
- ✅ Works via polling using `python-telegram-bot`

---

## ⚙️ Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/Telegram-BNB-bot.git
   cd Telegram-BNB-bot
   ```

2. Install dependencies:
   ```bash
   pip install python-telegram-bot binance
   ```

3. Edit the `config.py` file:
   ```python
   bot_key = "Your Telegram Bot Token"
   Pkey = "Your Binance Public API Key"
   Skey = "Your Binance Secret API Key"
   ```

4. Run the bot:
   ```bash
   python server.py
   ```

---

## 📩 Usage

Once the bot is running, you can interact via Telegram:

- `/start` – shows basic instructions  
- `/spot` – returns your total Binance wallet in USDT  
- Send coin names like `BTC`, `ETH`, `BNB` – to get the balance and value in USDT

---

## 🛑 Limitations

- No error handling for API failures
- No logging or debugging tools
- Keys are stored in plain text (do **not** use real accounts)
- Coin list is hardcoded and limited
- No support for futures or margin wallets

---

## 🔒 Security Notice

> Do **not** use this bot with your actual Binance account unless you've fully secured it.  
> Always use test accounts or demo environments for experiments like this.

---

## 📚 License

This project is open for study and learning.  
Use it, break it, improve it — just don't use it for real trading.

---

## ✌️ Made for Learning

Created as a minimal hands-on project to understand:
- Telegram Bot API
- Binance API integration
- Basic Python scripting and architecture
