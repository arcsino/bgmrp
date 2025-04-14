import flet as ft


class NavigationItem(ft.Container):
    def __init__(
        self,
        label,
        icon,
        on_click,
        bgcolor=ft.Colors.TRANSPARENT,
        icon_color=ft.Colors.PRIMARY,
    ):
        super().__init__()
        self.bgcolor = bgcolor
        self.on_click = on_click
        self.padding = 20
        self.border_radius = ft.border_radius.all(5)
        self.ink = True
        self.icon = ft.Icon(name=icon, color=icon_color)
        self.content = ft.Row(
            controls=[
                self.icon,
                ft.Text(value=label, theme_style=ft.TextThemeStyle.TITLE_SMALL),
            ]
        )


class NavigationBar(ft.Column):
    def __init__(self, on_click):
        super().__init__()
        self.width = 150
        self.on_clicked = on_click
        self.controls = [
            NavigationItem(
                label="ホーム",
                icon=ft.Icons.HOME,
                bgcolor=ft.Colors.LIGHT_BLUE_900,
                icon_color=ft.Colors.WHITE,
                on_click=lambda _: self.on_clicked(0),
            ),
            NavigationItem(
                label="作成",
                icon=ft.Icons.CREATE_NEW_FOLDER,
                on_click=lambda _: self.on_clicked(1),
            ),
            NavigationItem(
                label="ヘルプ",
                icon=ft.Icons.HELP,
                on_click=lambda _: self.on_clicked(2),
            ),
            NavigationItem(
                label="設定",
                icon=ft.Icons.SETTINGS,
                on_click=lambda _: self.on_clicked(3),
            ),
        ]
