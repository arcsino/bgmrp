import flet as ft

from controls import BodyText, CustomTextField


class NameTab(ft.Column):
    def __init__(self, project_obj):
        super().__init__()
        self.project_obj = project_obj
        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.textfield = CustomTextField(
            label="リソースパック名", value=self.project_obj.name, expand=True
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
