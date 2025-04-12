import flet as ft


class NavigationItem(ft.Container):
    def __init__(self, label, icon, on_click, bgcolor=ft.Colors.TRANSPARENT):
        super().__init__()
        self.content = ft.Row(
            controls=[
                ft.Icon(name=icon, color=ft.Colors.WHITE),
                ft.Text(value=label),
            ]
        )
        self.padding = 20
        self.bgcolor = bgcolor
        self.border_radius = ft.border_radius.all(10)
        self.ink = True
        self.on_click = on_click


class NavigationBar(ft.Column):
    def __init__(self, on_click):
        super().__init__()
        self.width = 150
        self.on_clicked = on_click
        self.controls = [
            NavigationItem(
                label="Home",
                icon=ft.Icons.HOME,
                bgcolor=ft.Colors.LIGHT_BLUE_900,
                on_click=lambda _: self.on_clicked(0),
            ),
            NavigationItem(
                label="Make",
                icon=ft.Icons.CREATE_NEW_FOLDER,
                on_click=lambda _: self.on_clicked(1),
            ),
            NavigationItem(
                label="Help",
                icon=ft.Icons.HELP,
                on_click=lambda _: self.on_clicked(2),
            ),
            NavigationItem(
                label="Setting",
                icon=ft.Icons.SETTINGS,
                on_click=lambda _: self.on_clicked(3),
            ),
        ]
