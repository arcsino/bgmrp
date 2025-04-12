import flet as ft

from navigation import NavigationBar
from home import home_view
from make import make_view
from help import help_view
from setting import setting_view


class MainView(ft.Row):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.nav = NavigationBar(on_click=self.on_clicked)
        self.views = [home_view(), make_view(), help_view(), setting_view()]
        self.controls = [
            self.nav,
            ft.VerticalDivider(width=10),
            ft.Column(
                controls=self.views,
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            ),
        ]

    def on_clicked(self, index):
        for view in self.views:
            view.visible = False
        for n in self.nav.controls:
            n.bgcolor = ft.Colors.TRANSPARENT
        self.views[index].visible = True
        self.nav.controls[index].bgcolor = ft.Colors.LIGHT_BLUE_900
        self.update()


def main(page: ft.Page):

    page.title = "Bgm RP Maker"
    page.window.min_width = 800
    page.window.min_height = 500
    page.window.width = 800
    page.window.height = 500
    page.theme_mode = ft.ThemeMode.DARK
    page.window.alignment = ft.alignment.center
    page.add(MainView())

    page.client_storage.set("key", "value")
    page.client_storage.clear()


if __name__ == "__main__":
    ft.app(target=main)
