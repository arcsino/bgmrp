import json, os
from pathlib import Path

from data.blank_project import get_blank_project_obj


class ProjectInfo:
    def __init__(self, name, description, icon, sounds, volume, version):
        self.name = name
        self.description = description
        self.icon = icon
        self.sounds = sounds
        self.volume = volume
        self.version = version


def get_project_dict(path):
    try:
        with open(path, "r") as f:
            obj = json.load(f)
            name = obj["name"]
            description = obj["description"]
            icon = obj["icon"]
            sounds = obj["sounds"]
            volume = obj["volume"]
            version = obj["version"]
            info = ProjectInfo(
                name=name,
                description=description,
                icon=icon,
                sounds=sounds,
                volume=volume,
                version=version,
            )
            return info
    except Exception as e:
        print(e)
        obj = get_blank_project_obj()
        name = obj["name"]
        description = obj["description"]
        icon = obj["icon"]
        sounds = obj["sounds"]
        volume = obj["volume"]
        version = obj["version"]
        info = ProjectInfo(
            name=name,
            description=description,
            icon=icon,
            sounds=sounds,
            volume=volume,
            version=version,
        )
        print(info.icon)
        return info


def get_sounds_dict(name, volume):
    return {"name": f"bgm/{name}", "stream": True, "volume": volume}


def get_sounds_json_dict(ary):
    with open(Path("json/sounds.json"), "r") as f:
        obj = json.dump(f)
        obj["bgm"] = {"sounds": ary}
        return obj
