import flet as ft


class TitleText(ft.Text):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.theme_style = ft.TextThemeStyle.HEADLINE_SMALL


class BodyText(ft.Text):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.theme_style = ft.TextThemeStyle.BODY_LARGE


class ExplainContainer(ft.Container):
    def __init__(self, title, body):
        super().__init__()
        self.title = title
        self.body = body
        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=TitleText(value=self.title),
                    padding=ft.padding.all(5),
                    bgcolor=ft.Colors.BLUE_GREY_900,
                    border_radius=ft.border_radius.all(10),
                ),
                BodyText(value=self.body),
            ],
        )
