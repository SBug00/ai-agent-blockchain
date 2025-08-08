import time
import schedule

from cau_hinh import CauHinh
from bo_nho import BoNho
from phan_tich_token import PhanTichToken
from canh_bao_telegram import CanhBaoTelegram

# Địa chỉ ví cần giám sát, bạn thay đổi nếu muốn
WATCH_ADDRESS = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"  # Ví dụ là ví của Binance

def job():
    print("Bắt đầu chạy kiểm tra giao dịch mới...")
    bo_nho = BoNho()
    ptt = PhanTichToken()
    telegram = CanhBaoTelegram()

    transactions = ptt.lay_giao_dich_moi(WATCH_ADDRESS)

    if not transactions:
        print("Không lấy được giao dịch mới.")
        return

    for tx in transactions:
        tx_hash = tx["hash"]
        if not bo_nho.has_transaction(tx_hash):
            ket_qua = ptt.phan_tich_giao_dich(tx)
            bo_nho.add_transaction(tx_hash)

            # Nếu giao dịch giá trị cao -> gửi cảnh báo
            if ket_qua["is_high_value"]:
                message = (
                    f"⚠️ Phát hiện giao dịch lớn!\n"
                    f"TxHash: {ket_qua['tx_hash']}\n"
                    f"Từ: {ket_qua['from']}\n"
                    f"Đến: {ket_qua['to']}\n"
                    f"Giá trị: {ket_qua['value_eth']:.2f} ETH"
                )
                telegram.gui_tin_nhan(message)
                print("Đã gửi cảnh báo Telegram.")
    print("Kiểm tra kết thúc.")

def main():
    print("AI agent bắt đầu chạy...")
    job()  # Chạy lần đầu
    schedule.every(CauHinh.POLL_INTERVAL_SECONDS).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
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
