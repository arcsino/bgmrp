import json, os, zipfile
from datetime import datetime
from pathlib import Path

from data.blank_project import get_blank_project_obj


APP_DATA_PATH = Path(os.getenv("FLET_APP_STORAGE_DATA"))


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
        return info


def rename_project_file(filepath: Path, newname: str) -> Path:
    filepath.rename(APP_DATA_PATH / f"{newname}.json")
    return filepath


def get_project_files():
    return list(APP_DATA_PATH.glob("*.json"))


def new_project_file(filename):
    try:
        if filename == "":
            raise Exception("プロジェクト名を入力してください。")
        new_project = APP_DATA_PATH / f"{filename}.json"
        new_project.touch(exist_ok=False)
    except Exception as e:
        print(e)


def delete_project_file(filepath: Path) -> None:
    delete_project = filepath
    delete_project.unlink(missing_ok=True)


def get_sounds_dict(name, volume):
    return {"name": f"bgm/{name}", "stream": True, "volume": volume}


def get_sounds_json_dict(ary):
    with open(Path("json/sounds.json"), "r") as f:
        obj = json.dump(f)
        obj["bgm"] = {"sounds": ary}
        return obj
