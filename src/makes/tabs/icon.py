import flet as ft
from pathlib import Path

from controls import BodyText, CustomBorderContainer


class IconTab(ft.Column):
    def __init__(self, project_obj):
        super().__init__()
        self.project_obj = project_obj
        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.select_field = CustomBorderContainer(
            content=ft.Row(
                controls=[
                    ft.Image(
                        src=(
                            self.project_obj.icon
                            if self.project_obj.icon
                            else Path("images/square.png")
                        ),
                        border_radius=ft.border_radius.all(5),
                        width=50,
                    ),
                    BodyText(
                        value=(
                            self.project_obj.icon
                            if self.project_obj.icon
                            else "画像を選択してください。"
                        ),
                        expand=True,
                    ),
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
