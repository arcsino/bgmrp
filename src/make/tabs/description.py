import flet as ft

from controls import BodyText, MultiLineTextField


class DescriptionTab(ft.Column):
    def __init__(self, description):
        super().__init__()
        self.description = description

        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.textfield = MultiLineTextField(
            label="リソースパックの説明",
            value=self.description,
            expand=True,
        )
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            BodyText(value="リソースパックの説明を入力してください。"),
            ft.Row(
                controls=[
                    self.textfield,
                    ft.VerticalDivider(width=1, color=ft.Colors.TRANSPARENT),  # margin
                ]
            ),
        ]
