import flet as ft


class TitleText(ft.Text):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.theme_style = ft.TextThemeStyle.HEADLINE_MEDIUM


class BodyText(ft.Text):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.theme_style = ft.TextThemeStyle.BODY_LARGE


class LabelText(ft.Text):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.theme_style = ft.TextThemeStyle.HEADLINE_SMALL


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
                    border_radius=ft.border_radius.all(5),
                ),
                BodyText(value=self.body),
            ],
        )


class CustomTextField(ft.TextField):
    def __init__(self, label):
        super().__init__()
        self.label = label
        self.bgcolor = ft.Colors.SURFACE
        self.border_color = ft.Colors.BLUE_GREY_200


class CustomBorderContainer(ft.Container):
    def __init__(self, content, visible=True):
        super().__init__()
        self.content = content
        self.visible = visible
        self.padding = ft.padding.all(10)
        self.bgcolor = ft.Colors.BLUE_GREY_900
        self.border = ft.border.all(1, ft.Colors.BLUE_GREY_200)
        self.border_radius = ft.border_radius.all(5)
