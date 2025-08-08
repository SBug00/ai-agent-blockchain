# phan_tich_token.py
import requests
from datetime import datetime

def phan_tich_co_ban_token(dia_chi):
    """
    Phân tích sơ: trả về dict với phát hiện cơ bản.
    Lưu ý: đây là phiên bản nhẹ dùng các API công khai hoặc heuristics.
    Bạn có thể tích hợp BscScan/Etherscan, DexScreener... để mở rộng.
    """
    ketqua = {
        "dia_chi": dia_chi,
        "contract_verified": None,
        "holder_count": None,
        "suspicious": False,
        "notes": []
    }

    # Ví dụ giả lập: nếu địa chỉ chứa nhiều số 0 -> coi là demo
    if dia_chi.endswith("0000"):
        ketqua["suspicious"] = True
        ketqua["notes"].append("Địa chỉ demo (kết thúc bằng 0000)")

    # Thêm thời gian
    ketqua["checked_at"] = datetime.utcnow().isoformat()
    return ketqua

