# phan_tich_token.py
import requests

# API key của bạn (có thể đổi sang biến môi trường khi deploy)
ETHERSCAN_API_KEY = "69VNXYQWJVT9ZNZRRXE9MP9B8B4XNIEC7H"

def phan_tich_co_ban_token(dia_chi_token: str) -> dict:
    """
    Lấy thông tin cơ bản của token từ Etherscan API.
    Không tải blockchain, chỉ truy vấn API trực tiếp.
    """
    ket_qua = {
        "dia_chi": dia_chi_token,
        "notes": "",
        "ten": None,
        "symbol": None,
        "decimals": None,
        "total_supply": None
    }

    try:
        # Gọi API lấy thông tin token (ERC20)
        url = "https://api.etherscan.io/api"
        params = {
            "module": "token",
            "action": "tokeninfo",
            "contractaddress": dia_chi_token,
            "apikey": ETHERSCAN_API_KEY
        }
        resp = requests.get(url, params=params, timeout=10)
        data = resp.json()

        if data.get("status") == "1" and data.get("result"):
            token_info = data["result"][0]
            ket_qua["ten"] = token_info.get("tokenName")
            ket_qua["symbol"] = token_info.get("symbol")
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
