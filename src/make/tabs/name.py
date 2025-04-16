import flet as ft

from controls import BodyText, CustomTextField


class NameTab(ft.Column):
    def __init__(self, name):
        super().__init__()
        self.name = name

        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.textfield = CustomTextField(
            label="リソースパック名",
            value=self.name,
            expand=True,
            on_change=self.changed_value,
        )
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            BodyText(value="リソースパックの名前を入力してください。"),
            ft.Row(
                controls=[
                    self.textfield,
                    ft.VerticalDivider(width=1, color=ft.Colors.TRANSPARENT),  # margin
                ]
            ),
        ]

    def changed_value(self, e: ft.ControlEvent):
        self.name = e.data
