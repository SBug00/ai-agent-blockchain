import requests
from CauHinh import BLOCKCHAIN_API_URL, BLOCKCHAIN_API_KEY

class PhanTichToken:

    def __init__(self):
        self.api_url = BLOCKCHAIN_API_URL
        self.api_key = BLOCKCHAIN_API_KEY

    def lay_giao_dich_moi(self, address, start_block=0):
        params = {
            "module": "account",
            "action": "txlist",
            "address": address,
            "startblock": start_block,
            "endblock": 99999999,
            "sort": "asc",
            "apikey": self.api_key
        }
        try:
            response = requests.get(self.api_url, params=params, timeout=10)
            data = response.json()
            if data["status"] == "1":
                return data["result"]
            else:
                print("API blockchain trả về lỗi:", data.get("message"))
                return []
        except Exception as e:
            print("Lỗi khi gọi API blockchain:", e)
            return []

    def phan_tich_giao_dich(self, tx):
        if tx is None:
            return {"notes": ["Không có tokentx dữ liệu hoặc lỗi API"]}

        value_eth = int(tx.get("value", 0)) / 1e18
        result = {
            "tx_hash": tx.get("hash"),
            "from": tx.get("from"),
            "to": tx.get("to"),
            "value_eth": value_eth,
            "is_high_value": value_eth > 10
        }
        return result

def thong_tin_token_contract(contract_address):
    url = BLOCKCHAIN_API_URL
    params = {
        "module": "token",
        "action": "tokeninfo",
        "contractaddress": contract_address,
        "apikey": BLOCKCHAIN_API_KEY
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        if data.get("status") == "1":
            result = data.get("result", [{}])[0]
            return {
                "name": result.get("tokenName"),
                "symbol": result.get("symbol"),
                "decimals": int(result.get("decimals", 0)),
                "totalTransfers_sample": int(result.get("totalTransfers", 0)),
                "notes": []
            }
        else:
            return {"notes": [data.get("message", "Lỗi API")]}
    except Exception as e:
        return {"notes": [f"Lỗi khi gọi API token info: {e}"]}

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

if __name__ == "__main__":
    dia_test = "0x6b175474e89094c44da98b954eedeac495271d0f"
    print(phan_tich_co_ban_token(dia_test))
