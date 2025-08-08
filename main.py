# main.py
import os
import time
import threading
from flask import Flask, request

from canh_bao_telegram import bot, gui_telegram_mau, reply_text
from phan_tich_token import phan_tich_co_ban_token
from bo_nho import them_item, danh_sach_tom_tat, gan_nhan, khoi_tao_bo_nho
from tro_ly_gpt import goi_gpt_phan_tich
from cau_hinh import DELAY_SECONDS, DUNG_GPT

# Danh sách quét mẫu
DANH_SACH_QUET = [
    "0x0000000000000000000000000000000000000000",
    "0x1111111111111111111111111111111111110000"
]

# Flask app cho Render
app = Flask(__name__)

def vong_quet():
    while True:
        try:
            for dia in DANH_SACH_QUET:
                ph = phan_tich_co_ban_token(dia)
                item_id = them_item("token", ph)
                gpt_kq = None
                if DUNG_GPT:
                    tomtat = f"Phân tích token: {ph}"
                    gpt_kq = goi_gpt_phan_tich(tomtat)
                msg = f"🔔 Phát hiện token mới (id={item_id})\nĐịa chỉ: {dia}\nPhân tích sơ: {ph['notes']}"
                if gpt_kq:
                    msg += f"\n\nGPT: {gpt_kq[:400]}"
                gui_telegram_mau(msg)
            time.sleep(DELAY_SECONDS)
        except Exception as e:
            print("Lỗi vòng quét:", e)
            time.sleep(30)

# Handlers
@bot.message_handler(commands=["report"])
def cmd_report(message):
    items = danh_sach_tom_tat(10)
    txt = "📋 Báo cáo ngắn — các item gần nhất:\n"
    for it in items:
        txt += f"- id:{it['id']} type:{it['type']} label:{it['label']} meta:{it['meta'].get('dia_chi','')}\n"
    reply_text(message, txt)

@bot.message_handler(commands=["memory"])
def cmd_memory(message):
    items = danh_sach_tom_tat(5)
    txt = "🧠 Bộ nhớ (5 item mới):\n"
    for it in items:
        txt += f"id:{it['id']} type:{it['type']} label:{it['label']} meta:{it['meta']}\n"
    reply_text(message, txt)

@bot.message_handler(commands=["learn"])
def cmd_learn(message):
    parts = message.text.split(" ", 2)
    if len(parts) < 3:
        reply_text(message, "Cú pháp: /learn <id> <kết luận>")
        return
    try:
        item_id = int(parts[1])
        label = parts[2].strip()
        ok = gan_nhan(item_id, label)
        if ok:
            reply_text(message, f"Đã gán nhãn id {item_id} => {label}")
        else:
            reply_text(message, "Không tìm thấy item id đó.")
    except:
        reply_text(message, "ID không hợp lệ.")

# Route webhook cho Telegram
@app.route(f"/{os.getenv('TELEGRAM_TOKEN')}", methods=["POST"])
def webhook():
    update = request.stream.read().decode("utf-8")
    bot.process_new_updates([bot._process_update(update)])
    return "OK", 200

@app.route("/")
def home():
    return "Bot AI Agent đang chạy trên Render!"

if __name__ == "__main__":
    khoi_tao_bo_nho()
    threading.Thread(target=vong_quet, daemon=True).start()

    PORT = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=PORT)
