import json
import os

class BoNho:
    FILE_PATH = "memory.json"

    def __init__(self):
        self.data = {"checked_transactions": {}}
        self.load()

    def load(self):
        if os.path.exists(self.FILE_PATH):
            try:
                with open(self.FILE_PATH, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
            except Exception as e:
                print(f"Lỗi load bộ nhớ: {e}")

    def save(self):
        try:
            with open(self.FILE_PATH, "w", encoding="utf-8") as f:
                json.dump(self.data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Lỗi lưu bộ nhớ: {e}")

    def has_transaction(self, tx_hash):
        return tx_hash in self.data["checked_transactions"]

    def add_transaction(self, tx_hash, analysis_text):
        self.data["checked_transactions"][tx_hash] = analysis_text
        self.save()

    def get_analysis(self, tx_hash):
        return self.data["checked_transactions"].get(tx_hash)
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
