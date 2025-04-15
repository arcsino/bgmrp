import flet as ft

from navigation import NavView
from home.home_view import HomeView
from make.make_view import MakeView
from help.help_view import HelpView
from setting.setting_view import SettingView


class MainView(ft.Row):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.navbar = NavView(item_clicked=self.item_clicked)
        self.views = [HomeView(), MakeView(), HelpView(), SettingView()]
        self.controls = [
            self.navbar,
            ft.VerticalDivider(width=10),
            ft.Column(
                controls=self.views,
                expand=True,
            ),
        ]

    def item_clicked(self, index):
        """when NavItem() is clicked"""
        for view in self.views:
            view.visible = False
        self.views[index].visible = True
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


if __name__ == "__main__":
    ft.app(target=main)
