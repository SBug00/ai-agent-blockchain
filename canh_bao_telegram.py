from telegram import Bot
from cau_hinh import CauHinh

class CanhBaoTelegram:
    def __init__(self):
        self.bot = Bot(token=CauHinh.TELEGRAM_BOT_TOKEN)
        self.chat_id = CauHinh.TELEGRAM_CHAT_ID

    def gui_tin_nhan(self, message):
        try:
            self.bot.send_message(chat_id=self.chat_id, text=message)
        except Exception as e:
            print(f"Lỗi gửi tin nhắn Telegram: {e}")
        "/remove <address> - xóa watch\n"
        "/list - xem watchlist\n"
        "/scan <address> - quét thủ công 1 address\n"
        "/report - báo cáo ngắn\n"
        "/memory - xem history\n"
        "/learn <id> <label> - gán nhãn item\n"
    )
    bot.reply_to(message, txt)

@bot.message_handler(commands=["add"])
def handle_add(message):
    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, "Cú pháp: /add <địa_chỉ_token_or_wallet>")
        return
    addr = parts[1].strip()
    if them_watch(addr):
        bot.reply_to(message, f"Đã thêm watch: {addr}")
    else:
        bot.reply_to(message, f"Địa chỉ đã tồn tại: {addr}")

@bot.message_handler(commands=["remove"])
def handle_remove(message):
    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, "Cú pháp: /remove <địa_chỉ>")
        return
    addr = parts[1].strip()
    if xoa_watch(addr):
        bot.reply_to(message, f"Đã xóa: {addr}")
    else:
        bot.reply_to(message, f"Địa chỉ không tồn tại: {addr}")

@bot.message_handler(commands=["list"])
def handle_list(message):
    wl = lay_watchlist()
    if not wl:
        bot.reply_to(message, "Watchlist trống.")
        return
    txt = "🔎 Watchlist:\n" + "\n".join(wl)
    bot.reply_to(message, txt)

@bot.message_handler(commands=["scan"])
def handle_scan(message):
    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, "Cú pháp: /scan <address>")
        return
    addr = parts[1].strip()
    # import ở runtime để tránh vòng lặp import
    from phan_tich_token import phan_tich_co_ban_token
    ph = phan_tich_co_ban_token(addr)
    item_id = them_item("manual_scan", ph)
    txt = f"Scan id={item_id}\nĐC: {addr}\nSuspicious: {ph.get('suspicious')}\nLý do: {ph.get('reasons')}"
    bot.reply_to(message, txt)

@bot.message_handler(commands=["report"])
def handle_report(message):
    items = danh_sach_tom_tat(10)
    txt = "📋 Báo cáo (10 item mới):\n"
    for it in items:
        txt += f"- id:{it['id']} type:{it['type']} label:{it['label']} meta:{it['meta'].get('dia_chi','')}\n"
    bot.reply_to(message, txt)

@bot.message_handler(commands=["memory"])
def handle_memory(message):
    items = danh_sach_tom_tat(10)
    txt = "🧠 Memory (10 item mới):\n"
    for it in items:
        txt += f"id:{it['id']} type:{it['type']} label:{it['label']} meta:{it['meta']}\n"
    bot.reply_to(message, txt)

@bot.message_handler(commands=["learn"])
def handle_learn(message):
    parts = message.text.strip().split(" ", 2)
    if len(parts) < 3:
        bot.reply_to(message, "Cú pháp: /learn <id> <label>")
        return
    try:
        item_id = int(parts[1])
        label = parts[2].strip()
        if gan_nhan(item_id, label):
            bot.reply_to(message, f"Đã gán nhãn id {item_id} => {label}")
        else:
            bot.reply_to(message, "Không tìm thấy id.")
    except Exception:
        bot.reply_to(message, "ID không hợp lệ.")
        "/memory - Xem tóm tắt bộ nhớ (history)\n"
        "/learn <id> <kết luận> - Dạy bot (gán nhãn 1 mục trong memory)\n"
    )
    bot.reply_to(message, txt)

# Hàm để bot phản hồi ngoại lệ, debug, ... bạn có thể mở rộng
def reply_text(message, text):
    bot.reply_to(message, text)

