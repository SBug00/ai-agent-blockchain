# bo_nho.py
import json, os, time
from cau_hinh import FILE_MEMORY

def khoi_tao_bo_nho():
    if not os.path.exists(FILE_MEMORY):
        data = {"watchlist": [], "items": []}
        _luu(data)

def _doc():
    khoi_tao_bo_nho()
    with open(FILE_MEMORY, "r", encoding="utf-8") as f:
        return json.load(f)

def _luu(data):
    with open(FILE_MEMORY, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def them_watch(address: str) -> bool:
    data = _doc()
    if address not in data["watchlist"]:
        data["watchlist"].append(address)
        _luu(data)
        return True
    return False

def xoa_watch(address: str) -> bool:
    data = _doc()
    if address in data["watchlist"]:
        data["watchlist"].remove(address)
        _luu(data)
        return True
    return False

def lay_watchlist():
    data = _doc()
    return data.get("watchlist", [])

def them_item(type_, meta: dict):
    data = _doc()
    item = {
        "id": int(time.time() * 1000),
        "type": type_,
        "meta": meta,
        "label": None,
        "ts": int(time.time())
    }
    data["items"].append(item)
    _luu(data)
    return item["id"]

def danh_sach_tom_tat(limit=20):
    data = _doc()
    items = sorted(data.get("items", []), key=lambda x: x["ts"], reverse=True)
    return items[:limit]

def gan_nhan(item_id: int, label: str) -> bool:
    data = _doc()
    for it in data["items"]:
        if it["id"] == item_id:
            it["label"] = label
            _luu(data)
            return True
    return False
