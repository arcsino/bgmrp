import flet as ft

from navigation import NavigationItem
from home import home_view
from make import make_view
from help import help_view
from setting import setting_view


def main(page: ft.Page):

    def on_clicked(index):
        for view in views:
            view.visible = False
        for n in nav:
            n.bgcolor = ft.Colors.TRANSPARENT
        views[index].visible = True
        nav[index].bgcolor = ft.Colors.LIGHT_BLUE_900
        page.update()

    page.title = "Bgm RP Maker"
    page.window.min_width = 800
    page.window.min_height = 500
    page.window.width = 800
    page.window.height = 500
    page.theme_mode = ft.ThemeMode.DARK
    page.window.alignment = ft.alignment.center

    views = [home_view(), make_view(), help_view(), setting_view()]
    nav = [
        NavigationItem(
            label="Home",
            icon=ft.Icons.HOME,
            bgcolor=ft.Colors.LIGHT_BLUE_900,
            on_click=lambda _: on_clicked(0),
        ),
        NavigationItem(
            label="Make",
            icon=ft.Icons.CREATE_NEW_FOLDER,
            on_click=lambda _: on_clicked(1),
        ),
        NavigationItem(
            label="Help",
            icon=ft.Icons.HELP,
            on_click=lambda _: on_clicked(2),
        ),
        NavigationItem(
            label="Setting",
            icon=ft.Icons.SETTINGS,
            on_click=lambda _: on_clicked(3),
        ),
    ]
    page.add(
        ft.Row(
            controls=[
                ft.Column(controls=nav, width=150),
                ft.VerticalDivider(
                    width=10,
                ),
                ft.Column(
                    controls=views,
                    expand=True,
                ),
            ],
            expand=True,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
