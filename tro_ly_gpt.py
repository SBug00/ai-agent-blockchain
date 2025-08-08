# tro_ly_gpt.py
import openai
from cau_hinh import OPENAI_API_KEY, DUNG_GPT

if DUNG_GPT:
    openai.api_key = OPENAI_API_KEY

def goi_gpt_phan_tich(tom_tat):
    """
    tom_tat: string tóm tắt token/ví để gửi GPT
    Trả về chuỗi phân tích (text) hoặc None nếu không bật GPT.
    """
    if not DUNG_GPT:
        return None
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content": tom_tat}],
            max_tokens=300
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"Lỗi gọi GPT: {e}"
