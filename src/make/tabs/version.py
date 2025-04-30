import flet as ft

from controls import BodyText
from data.format_version import get_format_version


class VersionTab(ft.Column):
    def __init__(self, version):
        super().__init__()
        self.version = version

        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.format = get_format_version()
        self.options = [
            ft.DropdownOption(key=key, content=BodyText(value=key))
            for key in self.format.keys()
        ]
        self.dropdown = ft.Dropdown(
            value=self.version,
            options=self.options,
            border_color=ft.Colors.ON_SURFACE_VARIANT,
            on_change=self.changed_option,
        )
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            BodyText(value="Minecraftのバージョンを設定してください。"),
            self.dropdown,
        ]

    def changed_option(self, e: ft.ControlEvent):
        self.version = e.data
