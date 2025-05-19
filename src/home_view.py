import flet as ft
from pathlib import Path

from controls import ExplainContainer, BodyText


class HomeView(ft.Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            ExplainContainer(
                title="Bgmrp v1.0.1",
                body="MinecraftにBGMを追加するリソースパックを簡単に作れるデスクトップアプリです。",
            ),
            BodyText(value="※Java版限定です。"),
            ft.Image(
                src=Path("images/wp.png"),
                border_radius=ft.border_radius.all(10),
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
        ]
