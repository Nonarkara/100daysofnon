# Chronos Biographer Bot Setup

To run the automated Telegram bot overnight:

1. **Install Dependencies**
   ```bash
   pip install python-telegram-bot
   ```

2. **Environment Variables**
   You need to set two environment variables:
   - `TELEGRAM_BOT_TOKEN`: The token from BotFather.
   - `TELEGRAM_CHAT_ID`: Your chat ID, so the bot can proactively push the daily question to you at 21:00 BKK time.

3. **Run the Bot**
   ```bash
   export TELEGRAM_BOT_TOKEN="your-bot-token"
   export TELEGRAM_CHAT_ID="your-chat-id"
   python3 biographer_bot.py
   ```

## What It Does
- **Schedules**: Automatically sends the daily question at exactly 21:00 Asia/Bangkok time.
- **Listens**: Any text or voice message you send to it is automatically appended to `diary/day-XXX/answer.md` for the current active day.
- **Telemetry**: It calculates `T0`, `T3`, and `T4` latencies and writes them into `telemetry.json`.
- **Pipeline Trigger**: Every time you send a message, it automatically runs `pipeline/intake.py` and `pipeline/analyze.py` to rebuild the HTML and the patterns log. You don't have to manually build the site anymore.
