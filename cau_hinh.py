# cau_hinh.py
import os

# === Telegram ===
# Mặc định dùng giá trị bạn cung cấp — khi deploy nên set biến môi trường BOT_TOKEN, CHAT_ID
BOT_TOKEN = os.getenv("BOT_TOKEN", "8499978096:AAEEbC7m0l81IxyIXmO9QFWs2neWivZW8HM")
CHAT_ID   = os.getenv("CHAT_ID", "7241660939")  # chat id bạn đã gửi

# === Etherscan API (dùng để query token/giao dịch) ===
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY", "69VNXYQWJVT9ZNZRRXE9MP9B8B4XNIEC7H")
# Base URL Etherscan (Ethereum mainnet). Nếu bạn muốn BSC, đổi sang BscScan URL.
ETHERSCAN_API_URL = os.getenv("ETHERSCAN_API_URL", "https://api.etherscan.io/api")

# === Thời gian quét (giây) ===
DELAY_SECONDS = int(os.getenv("DELAY_SECONDS", "300"))  # mặc định 5 phút

# === File lưu memory / watchlist ===
FILE_MEMORY = os.getenv("FILE_MEMORY", "memory.json")   # lưu items + watchlist

# === Dùng GPT? (hiện để False) ===
DUNG_GPT = os.getenv("DUNG_GPT", "false").lower() in ("1","true","yes")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
