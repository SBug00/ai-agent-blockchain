# bo_nho.py
import json, os, time
from cau_hinh import FILE_MEMORY

def khoi_tao_bo_nho():
    if not os.path.exists(FILE_MEMORY):
        with open(FILE_MEMORY, "w") as f:
            json.dump({"items": []}, f)

def nap_bo_nho():
    khoi_tao_bo_nho()
    with open(FILE_MEMORY, "r") as f:
        return json.load(f)

def luu_bo_nho(data):
    with open(FILE_MEMORY, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def them_item(typ, meta):
    """
    typ: 'token' / 'alert' / 'gpt_query'
    meta: dict chứa thông tin tóm tắt (địa_chi, ten, notes, timestamp...)
    """
    data = nap_bo_nho()
    item = {
        "id": int(time.time()*1000),
        "type": typ,
        "meta": meta,
        "label": None,       # cho phép bạn gán nhãn (learn)
        "created_at": int(time.time())
    }
    data["items"].append(item)
    luu_bo_nho(data)
    return item["id"]

def danh_sach_tom_tat(limit=20):
    data = nap_bo_nho()
    items = data.get("items", [])
    # trả về ngược (mới trước)
    items = sorted(items, key=lambda x: x["created_at"], reverse=True)[:limit]
    summary = []
    for it in items:
        s = {
            "id": it["id"],
            "type": it["type"],
            "label": it.get("label"),
            "meta": it["meta"]
        }
        summary.append(s)
    return summary

def gan_nhan(item_id, label):
    data = nap_bo_nho()
    for it in data["items"]:
        if it["id"] == item_id:
            it["label"] = label
            luu_bo_nho(data)
            return True
    return False
