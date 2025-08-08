# cau_hinh.py
# Cấu hình lấy từ environment (Render sẽ set trong Settings > Environment)
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")          # BẮT BUỘC: token bot Telegram
CHAT_ID = os.getenv("CHAT_ID")              # BẮT BUỘC: chat id nơi nhận cảnh báo

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")  # BẮT BUỘC: Etherscan API key
ETHERSCAN_API_URL = os.getenv("ETHERSCAN_API_URL", "https://api.etherscan.io/api")

# Thời gian chờ giữa các vòng quét (giây)
DELAY_SECONDS = int(os.getenv("DELAY_SECONDS", "300"))

# File lưu memory/watchlist (mặc định trong folder app)
FILE_MEMORY = os.getenv("FILE_MEMORY", "memory.json")

# Bật GPT (nếu sau này bạn thêm OpenAI key)
DUNG_GPT = os.getenv("DUNG_GPT", "false").lower() in ("1","true","yes")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
