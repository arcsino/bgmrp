import json
from pathlib import Path


def get_sounds_dict(name, volume):
    return {"name": f"bgm/{name}", "stream": True, "volume": volume}


def get_sounds_json_dict(ary):
    with open(Path("json/sounds.json"), "r") as f:
        obj = json.dump(f)
        obj["bgm"] = {"sounds": ary}
        return obj
