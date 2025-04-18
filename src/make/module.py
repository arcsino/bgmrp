import flet as ft
import json, os, zipfile
from dataclasses import dataclass
from pathlib import Path

from data.blank_project import get_blank_project_obj
from data.blank_sounds import get_blank_sounds_obj
from data.blank_pack_mcmeta import get_blank_pack_mcmeta
from data.format_version import get_format_version


APP_DATA_PATH = Path(os.getenv("FLET_APP_STORAGE_DATA"))


@dataclass
class ProjectInfo:
    name: str
    description: str
    icon: Path
    sounds: list[Path]
    volume: float
    version: str


def get_project_obj(path: Path) -> ProjectInfo:
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


def write_project_info(path, project_obj: ProjectInfo):
    obj = get_blank_project_obj()
    obj["name"] = project_obj.name
    obj["description"] = project_obj.description
    obj["icon"] = project_obj.icon
    obj["sounds"] = project_obj.sounds
    obj["volume"] = project_obj.volume
    obj["version"] = project_obj.version
    with open(path, "w") as f:
        json.dump(obj, f)


def get_icon_image(filepath):
    if not filepath == "":
        if Path(filepath).exists():
            return Path(filepath)
        else:
            return Path("images/square.png")
    else:
        return Path("images/square.png")


def rename_project_file(filepath: Path, newname: str) -> Path:
    filepath.rename(APP_DATA_PATH / f"{newname}.json")
    return filepath


def get_project_files():
    projects = list(APP_DATA_PATH.glob("*.json"))
    projects.sort()
    return projects


def new_project_file(filename):
    try:
        if filename == "":
            raise Exception("プロジェクト名を入力してください！")
        new_project = APP_DATA_PATH / f"{filename}.json"
        new_project.touch(exist_ok=False)

    except Exception as e:
        return e


def delete_project_file(filepath: Path):
    delete_project = filepath
    delete_project.unlink(missing_ok=True)


def check_entry(obj: ProjectInfo):
    entrys = [obj.name, obj.description, obj.icon, obj.sounds, obj.volume, obj.version]
    empty_error = [
        "リソースパックの名前を入力してください。",
        "リソースパックの説明を入力してください。",
        "リソースパックのアイコンを選択してください。",
        "追加するBGMを選択してください。",
        "BGMの音量を設定してください。",
        "Minecraftのバージョンを設定してください。",
    ]
    try:
        for entry, error in zip(entrys, empty_error):
            if not entry:
                raise Exception(error)
        if not Path(obj.icon).exists():
            raise Exception(f"{obj.icon}が見つかりません。")
        for sound in obj.sounds:
            if not Path(sound).exists():
                raise Exception(f"{sound}が見つかりません。")
    except Exception as e:
        return e


def get_pack_mcmeta(description, version):
    format_version = get_format_version()
    pack = get_blank_pack_mcmeta()
    pack["pack"]["pack_format"] = format_version[version]
    pack["pack"]["supported_formats"] = [
        format_version[version],
        format_version[version],
    ]
    pack["pack"]["description"] = description
    return pack


def get_sounds_list(sounds, volume):
    s_list = []
    for i in range(len(sounds)):
        s_list.append({"name": f"bgm/{i}", "stream": True, "volume": volume / 100})
    return s_list


def get_sounds_json(sounds, volume):
    s_list = get_sounds_list(sounds, volume)
    s_json = get_blank_sounds_obj()
    s_json["bgm"] = {"sounds": s_list}
    return s_json


def make_rp(rp_path, obj: ProjectInfo):
    try:
        rp_path = Path(rp_path)
        if rp_path.exists():
            rp_path.unlink(missing_ok=True)

        # *.zip
        with zipfile.ZipFile(
            rp_path, "a", compression=zipfile.ZIP_DEFLATED, compresslevel=9
        ) as zf:

            # pack.mcmeta
            with zf.open("pack.mcmeta", "w") as f:
                pack = get_pack_mcmeta(obj.description, obj.version)
                f.write(json.dumps(pack).encode("utf-8"))

            # sounds.json
            with zf.open("assets/minecraft/sounds.json", "w") as f:
                s_json = get_sounds_json(obj.sounds, obj.volume)
                f.write(json.dumps(s_json).encode("utf-8"))

            # pack.png
            zf.write(obj.icon, arcname="pack.png")

            # *.ogg
            for i, sound in enumerate(obj.sounds):
                zf.write(sound, arcname=f"assets/minecraft/sounds/bgm/{i}.ogg")

    except Exception as e:
        return e
