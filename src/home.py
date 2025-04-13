import flet as ft
from pathlib import Path
from controls import TitleText, BodyText, ExplainContainer


def home_view():
    return ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            ExplainContainer(
                title="Bgm RP Maker v3.0.0",
                body="MinecraftのBGMを変更するリソースパックを簡単に作れるデスクトップアプリです。\n※Java版限定です。",
            ),
            ft.Image(
                src=Path("images/wp.png"),
                border_radius=ft.border_radius.all(10),
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            ExplainContainer(
                title="v3.0.0",
                body="[+] uiライブラリをcustomtkinterからfletに変更しました",
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
        ],
    )
