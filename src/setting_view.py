import flet as ft

from controls import ExplainContainer


class SettingView(ft.Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.visible = False
        self.scroll = ft.ScrollMode.AUTO
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            ExplainContainer(
                title="設定",
                body="テーマを切り替えることができます。",
            ),
            ft.Switch(
                label=" Light theme",
                on_change=self.theme_changed,
            ),
        ]

    def theme_changed(self, e):
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.page.update()
