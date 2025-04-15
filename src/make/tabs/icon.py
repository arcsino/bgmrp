import flet as ft
from pathlib import Path

from controls import BodyText, BorderContainer


class IconTab(ft.Column):
    def __init__(self, icon):
        super().__init__()
        self.icon = icon

        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.image = ft.Image(
            src=(self.icon if self.icon else Path("images/square.png")),
            border_radius=ft.border_radius.all(5),
            width=50,
        )
        self.body_path = ft.Container(
            expand=True,
            content=BodyText(
                value=(self.icon if self.icon else "画像を選択してください。")
            ),
        )
        self.select_field = BorderContainer(
            content=ft.Row(
                controls=[
                    self.image,
                    self.body_path,
                    ft.IconButton(
                        icon=ft.Icons.OPEN_IN_BROWSER,
                        icon_color=ft.Colors.WHITE,
                    ),
                ],
            )
        )
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            BodyText(
                value="リソースパックのアイコンを選択してください。画像ファイルは拡張子.PNGです。"
            ),
            ft.Row(
                controls=[
                    self.select_field,
                    ft.VerticalDivider(width=1, color=ft.Colors.TRANSPARENT),  # margin
                ]
            ),
        ]
