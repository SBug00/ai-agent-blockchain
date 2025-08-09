import os
import time
import threading
import requests
from flask import Flask
from telegram import Bot
from dotenv import load_dotenv

# Load biến môi trường khi chạy local
load_dotenv()

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
ETHERSCAN_API_KEY = os.environ.get("ETHERSCAN_API_KEY")
PORT = int(os.environ.get("PORT", 10000))

if not TELEGRAM_TOKEN or not CHAT_ID or not ETHERSCAN_API_KEY:
    raise ValueError("❌ Thiếu biến môi trường cần thiết!")

bot = Bot(token=TELEGRAM_TOKEN)
last_tx_hash = {}
status_message = "Bot chưa chạy"

# Đọc ví từ file wallets.txt
def load_wallets(filename="wallets.txt"):
    wallets = {}
    if not os.path.exists(filename):
        print(f"⚠️ Không tìm thấy file {filename}")
        return wallets
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or "|" not in line:
                continue
            address, name = line.split("|", 1)
            wallets[address.strip()] = name.strip()
    return wallets

watched_wallets = load_wallets()

app = Flask(__name__)

@app.route("/")
def home():
    return f"<h1>🐋 Whale Alert Bot</h1><p>{status_message}</p><p>Đang theo dõi {len(watched_wallets)} ví</p>"

def check_wallet(address, name):
    global status_message
    url = (
        "https://api.etherscan.io/api"
        f"?module=account&action=txlist&address={address}"
        "&startblock=0&endblock=99999999&sort=desc"
        f"&apikey={ETHERSCAN_API_KEY}"
    )

    try:
        resp = requests.get(url, timeout=10).json()
    except Exception as e:
        print(f"[Lỗi API] {e}")
        return

    if resp.get("status") != "1" or not resp.get("result"):
        return

    latest_tx = resp["result"][0]
    tx_hash = latest_tx["hash"]
    value_eth = int(latest_tx["value"]) / 10**18

    if last_tx_hash.get(address) != tx_hash and value_eth >= 100:
        last_tx_hash[address] = tx_hash
        msg = (
            f"🚨 Giao dịch lớn từ {name}\n"
            f"💰 {value_eth} ETH\n"
            f"🔗 https://etherscan.io/tx/{tx_hash}"
        )
        try:
            bot.send_message(chat_id=CHAT_ID, text=msg)
            print(f"[Cảnh báo] {msg}")
            status_message = f"Đã gửi cảnh báo: {value_eth} ETH từ {name}"
        except Exception as e:
            print(f"[Lỗi gửi Telegram] {e}")

def run_bot():
    global status_message
    status_message = "Bot đang chạy..."
    while True:
        for addr, name in watched_wallets.items():
            check_wallet(addr, name)
        time.sleep(60)  # kiểm tra mỗi phút

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    app.run(host="0.0.0.0", port=PORT)
        resp = requests.get(url, timeout=10).json()
    except Exception as e:
        print(f"[Lỗi API] {e}")
        return

    if resp.get("status") != "1" or not resp.get("result"):
        return

    latest_tx = resp["result"][0]
    tx_hash = latest_tx["hash"]
    value_eth = int(latest_tx["value"]) / 10**18

    if last_tx_hash.get(address) != tx_hash and value_eth >= 100:
        last_tx_hash[address] = tx_hash
        msg = (
            f"🚨 Giao dịch lớn từ {name}\n"
            f"💰 {value_eth} ETH\n"
            f"🔗 https://etherscan.io/tx/{tx_hash}"
        )
        try:
            bot.send_message(chat_id=CHAT_ID, text=msg)
            print(f"[Cảnh báo] {msg}")
        except Exception as e:
            print(f"[Lỗi gửi Telegram] {e}")

if __name__ == "__main__":
    print("✅ Bot đang chạy (Python-Telegram-Bot v20+)...")
    while True:
        for addr, name in watched_wallets.items():
            check_wallet(addr, name)
        time.sleep(60)
        resp = requests.get(url, timeout=10).json()
    except Exception as e:
        print(f"[Lỗi API] {e}")
        return

    if resp.get("status") != "1" or not resp.get("result"):
        return

    latest_tx = resp["result"][0]
    tx_hash = latest_tx["hash"]
    value_eth = int(latest_tx["value"]) / 10**18

    # Cảnh báo nếu giao dịch mới và >= 100 ETH
    if last_tx_hash.get(address) != tx_hash and value_eth >= 100:
        last_tx_hash[address] = tx_hash
        msg = (
            f"🚨 Giao dịch lớn từ {name}\n"
            f"💰 {value_eth} ETH\n"
            f"🔗 https://etherscan.io/tx/{tx_hash}"
        )
        try:
            bot.send_message(chat_id=CHAT_ID, text=msg)
            print(f"[Cảnh báo] {msg}")
        except Exception as e:
            print(f"[Lỗi gửi Telegram] {e}")

if __name__ == "__main__":
    print("✅ Bot cảnh báo ví cá voi đang chạy...")
    while True:
        for addr, name in watched_wallets.items():
            check_wallet(addr, name)
        time.sleep(60)  # kiểm tra mỗi phút
