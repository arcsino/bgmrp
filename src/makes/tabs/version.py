import flet as ft

from controls import BodyText
from data.format_version import get_format_version


class VersionTab(ft.Column):
    def __init__(self, project_obj):
        super().__init__()
        self.project_obj = project_obj
        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.format = get_format_version()
        self.options = [
            ft.DropdownOption(key=key, content=BodyText(value=key))
            for key in self.format.keys()
        ]
        self.dropdown = ft.Dropdown(
            value=self.project_obj.version,
            options=self.options,
            border_color=ft.Colors.BLUE_GREY_200,
        )
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            BodyText(value="Minecraftのバージョンを設定してください。"),
            self.dropdown,
        ]
