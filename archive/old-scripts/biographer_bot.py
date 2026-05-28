import os
import json
import asyncio
import logging
from datetime import datetime, timezone, timedelta
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
BKK_TZ = timezone(timedelta(hours=7))
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

def get_current_day():
    # Helper to find which day we are currently on based on empty answer.md
    for day in range(1, 101):
        day_str = str(day).zfill(3)
        ans_path = f"diary/day-{day_str}/answer.md"
        if os.path.exists(ans_path):
            with open(ans_path, "r") as f:
                content = f.read().strip()
                if not content:
                    return day
    return 101

def load_question(day):
    day_str = str(day).zfill(3)
    q_path = f"diary/day-{day_str}/question.md"
    if os.path.exists(q_path):
        return open(q_path, "r").read().strip()
    return "Question pending."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Chronos Biographer initialized. I am tracking the 100 days.\n"
        "I will push the daily question at 21:00 Bangkok time.\n"
        "You can also type /question to get today's question immediately."
    )
    context.job_queue.run_repeating(
        daily_push, 
        interval=timedelta(days=1), 
        first=datetime.now(BKK_TZ).replace(hour=21, minute=0, second=0, microsecond=0)
    )

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    day = get_current_day()
    if day > 100:
        await update.message.reply_text("The 100 days are complete.")
        return
        
    question = load_question(day)
    
    # Log T0
    day_str = str(day).zfill(3)
    t_path = f"diary/day-{day_str}/telemetry.json"
    if os.path.exists(t_path):
        telemetry = json.load(open(t_path))
        if not telemetry.get("T0_approx"):
            telemetry["T0_approx"] = datetime.now(timezone.utc).isoformat()
            with open(t_path, "w") as f:
                json.dump(telemetry, f, indent=2)
                
    await update.message.reply_text(f"**Day {day}**\n\n{question}", parse_mode="Markdown")

async def daily_push(context: ContextTypes.DEFAULT_TYPE):
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not chat_id:
        logger.warning("No TELEGRAM_CHAT_ID set for daily push.")
        return
        
    day = get_current_day()
    if day <= 100:
        question = load_question(day)
        
        # Log T0
        day_str = str(day).zfill(3)
        t_path = f"diary/day-{day_str}/telemetry.json"
        if os.path.exists(t_path):
            telemetry = json.load(open(t_path))
            telemetry["T0_approx"] = datetime.now(timezone.utc).isoformat()
            with open(t_path, "w") as f:
                json.dump(telemetry, f, indent=2)
                
        await context.bot.send_message(chat_id=chat_id, text=f"**Day {day}**\n\n{question}", parse_mode="Markdown")

async def receive_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    day = get_current_day()
    if day > 100:
        return
        
    day_str = str(day).zfill(3)
    ans_path = f"diary/day-{day_str}/answer.md"
    t_path = f"diary/day-{day_str}/telemetry.json"
    
    message_text = update.message.text
    if update.message.voice:
        message_text = "[Voice Note Received - Awaiting Transcription]"
    
    # Append to answer.md
    with open(ans_path, "a") as f:
        f.write(message_text + "\n\n")
        
    # Update telemetry T3 and T4
    if os.path.exists(t_path):
        telemetry = json.load(open(t_path))
        now_iso = datetime.now(timezone.utc).isoformat()
        
        if not telemetry.get("T3_approx"):
            telemetry["T3_approx"] = now_iso
            # calculate latency if T0 exists
            if telemetry.get("T0_approx"):
                t0 = datetime.fromisoformat(telemetry["T0_approx"])
                telemetry["latency_ms_approx"] = int((datetime.now(timezone.utc) - t0).total_seconds() * 1000)
                
        telemetry["T4_approx"] = now_iso
        if telemetry.get("T3_approx"):
            t3 = datetime.fromisoformat(telemetry["T3_approx"])
            telemetry["composition_ms_approx"] = int((datetime.now(timezone.utc) - t3).total_seconds() * 1000)
            
        telemetry["answer_message_count"] = telemetry.get("answer_message_count", 0) + 1
        
        # very rough word count
        ans_content = open(ans_path, "r").read()
        telemetry["answer_word_count"] = len(ans_content.split())
        
        with open(t_path, "w") as f:
            json.dump(telemetry, f, indent=2)
            
    # Trigger pipeline
    os.system("python3 pipeline/intake.py")
    os.system("python3 pipeline/analyze.py")
    
    await update.message.reply_text(f"Logged to Day {day}. Pipeline rebuilt.")

def main():
    if not TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN environment variable not set.")
        return
        
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("question", send_question))
    
    # Catch all non-command text and voice messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_answer))
    application.add_handler(MessageHandler(filters.VOICE, receive_answer))
    
    logger.info("Chronos Biographer started.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
