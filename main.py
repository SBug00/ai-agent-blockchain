# main.py
import os
import threading
import time
from flask import Flask

from cau_hinh import DELAY_SECONDS, FILE_MEMORY
from bo_nho import khoi_tao_bo_nho, lay_watchlist, them_item
from phan_tich_token import phan_tich_co_ban_token
from canh_bao_telegram import bot, gui_telegram

app = Flask(__name__)

def vong_quet():
    while True:
        try:
            wl = lay_watchlist()
            if not wl:
                # nếu ko có watch, ngủ rồi loop
                time.sleep(DELAY_SECONDS)
                continue
            for addr in wl:
                ph = phan_tich_co_ban_token(addr)
                item_id = them_item("watch_scan", ph)
                if ph.get("suspicious"):
                    msg = f"🔔 Phát hiện khả nghi (id={item_id})\nĐịa chỉ: {addr}\nLý do: {ph.get('reasons')}\nTên/Symbol: {ph.get('name')}/{ph.get('symbol')}"
                    gui_telegram(msg)
                else:
                    # debug log hoặc tắt
                    print(f"[INFO] Quét {addr}: không đáng ngại")
            time.sleep(DELAY_SECONDS)
        except Exception as e:
            print("Lỗi vòng quét:", e)
            time.sleep(30)

@app.route("/")
def home():
    return "AI Agent (Render) — alive"

@app.route("/scan/<addr>")
def scan(addr):
    ph = phan_tich_co_ban_token(addr)
    item_id = them_item("manual_scan", ph)
    txt = f"Scan id={item_id} addr={addr} suspicious={ph.get('suspicious')} reasons={ph.get('reasons')}"
    gui_telegram(txt)
    return txt, 200

if __name__ == "__main__":
    # khởi tạo memory file nếu chưa có
    khoi_tao_bo_nho()

    # start thread quét nền
    t = threading.Thread(target=vong_quet, daemon=True)
    t.start()

    # start bot polling trong thread khác
    def bot_thread():
        bot.infinity_polling(timeout=10, long_polling_timeout=5)

    pb = threading.Thread(target=bot_thread, daemon=True)
    pb.start()

    # run Flask app (Render cung cấp PORT env)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
