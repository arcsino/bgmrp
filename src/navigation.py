import flet as ft


class NavItem(ft.Container):
    def __init__(
        self,
        label,
        icon,
        on_click,
        bgcolor=ft.Colors.TRANSPARENT,
        icon_color=ft.Colors.PRIMARY,
    ):
        super().__init__()
        self.label = label
        self.icon = ft.Icon(name=icon, color=icon_color)
        self.on_click = on_click
        self.bgcolor = bgcolor

        self.ink = True
        self.padding = 20
        self.border_radius = ft.border_radius.all(5)
        self.content = ft.Row(
            controls=[
                self.icon,
                ft.Text(value=self.label, theme_style=ft.TextThemeStyle.TITLE_SMALL),
            ]
        )


class NavView(ft.Column):
    def __init__(self, item_clicked):
        super().__init__()
        self.item_clicked = item_clicked

        self.width = 150
        self.controls = [
            NavItem(
                label="ホーム",
                icon=ft.Icons.HOME,
                bgcolor=ft.Colors.PRIMARY_CONTAINER,
                icon_color=ft.Colors.ON_PRIMARY_CONTAINER,
                on_click=lambda _: self.on_clicked(0),
            ),
            NavItem(
                label="作成",
                icon=ft.Icons.CREATE_NEW_FOLDER,
                on_click=lambda _: self.on_clicked(1),
            ),
            NavItem(
                label="ヘルプ",
                icon=ft.Icons.HELP,
                on_click=lambda _: self.on_clicked(2),
            ),
            NavItem(
                label="設定",
                icon=ft.Icons.SETTINGS,
                on_click=lambda _: self.on_clicked(3),
            ),
        ]

    def on_clicked(self, index):
        for nav in self.controls:
            nav.bgcolor = ft.Colors.TRANSPARENT
            nav.icon.color = ft.Colors.PRIMARY
        self.controls[index].bgcolor = ft.Colors.PRIMARY_CONTAINER
        self.controls[index].icon.color = ft.Colors.ON_PRIMARY_CONTAINER
        self.item_clicked(index)
