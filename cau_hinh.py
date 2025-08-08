import os

# Thông tin Telegram bot
BOT_TOKEN = os.getenv("BOT_TOKEN", "8499978096:AAEEbC7m0l81IxyIXmO9QFWs2neWivZW8HM")
CHAT_ID   = os.getenv("CHAT_ID", "7241660939")

# API Blockchain của bạn
BLOCKCHAIN_API_KEY = os.getenv("BLOCKCHAIN_API_KEY", "69VNXYQWJVT9ZNZRRXE9MP9B8B4XNIEC7H")

# URL API
BLOCKCHAIN_API_URL = "https://api.blockchair.com/ethereum"  # Ví dụ, tùy loại chain bạn muốn
