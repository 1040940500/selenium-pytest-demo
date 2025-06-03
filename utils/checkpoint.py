import os, json

def save_checkpoint(file, page, finished):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump({"page": page, "finished": finished}, f)

def load_checkpoint(file):
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"page": 1, "finished": False}
