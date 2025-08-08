import os
from dotenv import load_dotenv

load_dotenv()

class CauHinh:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    BLOCKCHAIN_API_KEY = os.getenv("BLOCKCHAIN_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Cấu hình thêm
    BLOCKCHAIN_API_URL = "https://api.etherscan.io/api"  # ví dụ Etherscan
    POLL_INTERVAL_SECONDS = 300  # 5 phút kiểm tra 1 lần
