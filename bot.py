import os
import time
import requests
from telegram import Bot
from dotenv import load_dotenv

# Load env khi chạy local
load_dotenv()

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
ETHERSCAN_API_KEY = os.environ.get("ETHERSCAN_API_KEY")

if not TELEGRAM_TOKEN or not CHAT_ID or not ETHERSCAN_API_KEY:
    raise ValueError("❌ Thiếu biến môi trường cần thiết!")

bot = Bot(token=TELEGRAM_TOKEN)

# Danh sách ví
watched_wallets = {
    "0x742d35Cc6634C0532925a3b844Bc454e4438f44e": "Whale BTC→ETH",
    "0xDC76CD25977E0a5Ae17155770273aD58648900D3": "Whale USDT"
}

last_tx_hash = {}

def check_wallet(address, name):
    """Kiểm tra giao dịch mới"""
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
