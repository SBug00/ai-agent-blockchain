import requests
from cau_hinh import CauHinh

class PhanTichToken:

    def __init__(self):
        self.api_url = CauHinh.BLOCKCHAIN_API_URL
        self.api_key = CauHinh.BLOCKCHAIN_API_KEY

    def lay_giao_dich_moi(self, address, start_block=0):
        """
        Lấy giao dịch mới của 1 địa chỉ ví trên Ethereum (Etherscan API)
        """
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
        """
        Phân tích giao dịch đơn lẻ
        Trả về dict kết quả phân tích hoặc cảnh báo
        """
        # Ví dụ giả lập: nếu giao dịch có giá trị lớn hơn 10 ETH thì cảnh báo
        value_eth = int(tx["value"]) / 1e18
        result = {
            "tx_hash": tx["hash"],
            "from": tx["from"],
            "to": tx["to"],
            "value_eth": value_eth,
            "is_high_value": value_eth > 10
        }
        return result
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
