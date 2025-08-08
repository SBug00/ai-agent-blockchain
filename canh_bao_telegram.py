# canh_bao_telegram.py
import telebot
from cau_hinh import BOT_TOKEN, CHAT_ID
import json, os
from datetime import datetime

if not BOT_TOKEN:
    raise Exception("Bạn chưa cấu hình BOT_TOKEN trong biến môi trường.")

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="Markdown")

def gui_telegram(chat_id, text):
    try:
        bot.send_message(chat_id, text)
    except Exception as e:
        print("Lỗi gửi Telegram:", e)

# Hàm tiện ích: gửi tới chat id có sẵn (nếu không rỗng), hoặc dùng chat_id từ message
def gui_telegram_mau(text):
    if CHAT_ID:
        gui_telegram(CHAT_ID, text)
    else:
        print("CHAT_ID chưa cấu hình — in log thay vì gửi Telegram.")
        print(text)

# Đăng ký handler command cơ bản (các lệnh sẽ được xử lý trong main)
@bot.message_handler(commands=["start"])
def hanlde_start(message):
    bot.reply_to(message, "🤖 Bot đã khởi động. Gõ /help để xem lệnh.")

@bot.message_handler(commands=["help"])
def hanlde_help(message):
    txt = (
        "Các lệnh hỗ trợ:\n"
        "/help - Hiện menu\n"
        "/report - Yêu cầu báo cáo ngắn từ bot\n"
        "/memory - Xem tóm tắt bộ nhớ (history)\n"
        "/learn <id> <kết luận> - Dạy bot (gán nhãn 1 mục trong memory)\n"
    )
    bot.reply_to(message, txt)

# Hàm để bot phản hồi ngoại lệ, debug, ... bạn có thể mở rộng
def reply_text(message, text):
    bot.reply_to(message, text)

