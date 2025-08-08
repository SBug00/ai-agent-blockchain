# phan_tich_token.py
import requests
from cau_hinh import ETHERSCAN_API_KEY, ETHERSCAN_API_URL

def _call_etherscan(params: dict, timeout=10):
    p = params.copy()
    p["apikey"] = ETHERSCAN_API_KEY
    try:
        r = requests.get(ETHERSCAN_API_URL, params=p, timeout=timeout)
        return r.json()
    except Exception as e:
        return {"status":"0", "message": str(e)}

def thong_tin_token_contract(contract_address: str):
    """
    Lấy dữ liệu mẫu dựa trên tokentx (10 giao dịch gần nhất).
    Trả dict tóm tắt.
    """
    res = {"contract": contract_address, "name": None, "symbol": None, "decimals": None, "totalTransfers_sample": 0, "notes": []}
    params = {
        "module": "account",
        "action": "tokentx",
        "address": contract_address,
        "page": 1,
        "offset": 10,
        "sort": "desc"
    }
    data = _call_etherscan(params)
    if data.get("status") == "1" and data.get("result"):
        arr = data["result"]
        res["totalTransfers_sample"] = len(arr)
        first = arr[0]
        res["symbol"] = first.get("tokenSymbol")
        res["decimals"] = first.get("tokenDecimal")
        res["name"] = first.get("tokenName")
        res["notes"].append("Dữ liệu lấy từ tokentx (mẫu 10 tx gần nhất)")
    else:
        res["notes"].append("Không có tokentx dữ liệu hoặc lỗi API")
    return res

def phan_tich_co_ban_token(contract_address: str):
    info = thong_tin_token_contract(contract_address)
    suspicious = False
    reasons = []

    tot = info.get("totalTransfers_sample", 0)
    if tot == 0:
        suspicious = True
        reasons.append("Không có transfer mẫu → có thể mới hoặc không hoạt động")
    elif tot <= 3:
        reasons.append("Hoạt động rất thấp (<=3 transfers trong mẫu)")

    if not info.get("symbol"):
        suspicious = True
        reasons.append("Không lấy được symbol từ transaction -> khả năng bất thường")

    return {
        "dia_chi": contract_address,
        "name": info.get("name"),
        "symbol": info.get("symbol"),
        "decimals": info.get("decimals"),
        "totalTransfers_sample": tot,
        "suspicious": suspicious,
        "reasons": reasons,
        "notes": info.get("notes", [])
    }
    else:
        res["notes"].append("Không có tokentx dữ liệu hoặc lỗi API")
    return res

def phan_tich_co_ban_token(contract_address: str):
    info = thong_tin_token_contract(contract_address)
    suspicious = False
    reasons = []

    tot = info.get("totalTransfers_sample", 0)
    if tot == 0:
        suspicious = True
        reasons.append("Không có transfer mẫu → có thể mới hoặc không hoạt động")
    elif tot <= 3:
        reasons.append("Hoạt động rất thấp (<=3 transfers trong mẫu)")

    if not info.get("symbol"):
        suspicious = True
        reasons.append("Không lấy được symbol từ transaction -> khả năng bất thường")

    return {
        "dia_chi": contract_address,
        "name": info.get("name"),
        "symbol": info.get("symbol"),
        "decimals": info.get("decimals"),
        "totalTransfers_sample": tot,
        "suspicious": suspicious,
        "reasons": reasons,
        "notes": info.get("notes", [])
    }
            ket_qua["decimals"] = token_info.get("divisor")  # divisor ~ decimals
            ket_qua["total_supply"] = token_info.get("totalSupply")

            ket_qua["notes"] = f"{ket_qua['ten']} ({ket_qua['symbol']}), supply={ket_qua['total_supply']}, decimals={ket_qua['decimals']}"
        else:
            ket_qua["notes"] = "Không tìm thấy thông tin token trên Etherscan."
    except Exception as e:
        ket_qua["notes"] = f"Lỗi khi truy vấn API: {e}"

    return ket_qua


if __name__ == "__main__":
    # Test nhanh với token DAI
    dia_test = "0x6b175474e89094c44da98b954eedeac495271d0f"
    print(phan_tich_co_ban_token(dia_test))
