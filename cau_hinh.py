import os

# Telegram
BOT_TOKEN = os.getenv("8499978096:AAEEbC7m0l81IxyIXmO9QFWs2neWivZW8HM")     # Token bot lấy từ @BotFather
# Nếu muốn gửi trực tiếp tới 1 chat cụ thể, có thể dùng CHAT_ID nhưng bot polling không cần
CHAT_ID = os.getenv("CHAT_ID", "7241660939")

# Blockchain RPC (mặc định BSC)
RPC_BSC = os.getenv("RPC_BSC", "https://bsc-dataseed.binance.org/")
RPC_ETH = os.getenv("RPC_ETH", "https://eth.llamarpc.com")

# OpenAI (nếu dùng)
DUNG_GPT = os.getenv("DUNG_GPT", "false").lower() in ("1","true","yes")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Delay giữa 2 vòng quét (giây)
DELAY_SECONDS = int(os.getenv("DELAY_SECONDS", "300"))

# File lưu memory (bot sẽ ghi/đọc ở đây)
FILE_MEMORY = os.getenv("FILE_MEMORY", "memory.json")
