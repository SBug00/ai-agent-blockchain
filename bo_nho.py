import json
import os

class BoNho:
    FILE_PATH = "memory.json"

    def __init__(self):
        self.data = {
            "checked_transactions": set(),
            "learned_phrases": []
        }
        self.load()

    def load(self):
        if os.path.exists(self.FILE_PATH):
            try:
                with open(self.FILE_PATH, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    # Lưu checked_transactions dưới dạng list, convert lại thành set
                    self.data["checked_transactions"] = set(data.get("checked_transactions", []))
                    self.data["learned_phrases"] = data.get("learned_phrases", [])
            except Exception as e:
                print(f"Load bộ nhớ lỗi: {e}")

    def save(self):
        try:
            with open(self.FILE_PATH, "w", encoding="utf-8") as f:
                # Convert set sang list để json được
                data_to_save = {
                    "checked_transactions": list(self.data["checked_transactions"]),
                    "learned_phrases": self.data["learned_phrases"]
                }
                json.dump(data_to_save, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Lưu bộ nhớ lỗi: {e}")

    def add_transaction(self, tx_hash):
        self.data["checked_transactions"].add(tx_hash)
        self.save()

    def has_transaction(self, tx_hash):
        return tx_hash in self.data["checked_transactions"]

    def add_learned_phrase(self, phrase):
        self.data["learned_phrases"].append(phrase)
        self.save()

    def get_learned_phrases(self):
        return self.data["learned_phrases"]
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
