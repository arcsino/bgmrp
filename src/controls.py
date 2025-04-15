import flet as ft


class HeadLineText(ft.Text):
    def __init__(self, value):
        super().__init__()
        self.value = value

        self.theme_style = ft.TextThemeStyle.HEADLINE_MEDIUM


class TitleText(ft.Text):
    def __init__(self, value):
        super().__init__()
        self.value = value

        self.theme_style = ft.TextThemeStyle.TITLE_MEDIUM


class BodyText(ft.Text):
    def __init__(self, value):
        super().__init__()
        self.value = value

        self.theme_style = ft.TextThemeStyle.BODY_MEDIUM


class BorderContainer(ft.Container):
    def __init__(self, content):
        super().__init__()
        self.content = content

        self.expand = True
        self.padding = ft.padding.all(10)
        self.bgcolor = ft.Colors.BLUE_GREY_900
        self.border = ft.border.all(1, ft.Colors.BLUE_GREY_200)
        self.border_radius = ft.border_radius.all(5)


class ExplainContainer(ft.Container):
    def __init__(self, title, body):
        super().__init__()
        self.title = title
        self.body = body

        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=HeadLineText(value=self.title),
                    padding=ft.padding.all(5),
                    bgcolor=ft.Colors.BLUE_GREY_900,
                    border_radius=ft.border_radius.all(5),
                ),
                BodyText(value=self.body),
            ],
        )


class CustomTextField(ft.TextField):
    def __init__(self, label, value="", expand=False):
        super().__init__()
        self.label = label
        self.value = value
        self.expand = expand

        self.bgcolor = ft.Colors.SURFACE
        self.border_color = ft.Colors.BLUE_GREY_200


class MultiLineTextField(ft.TextField):
    def __init__(self, label, value="", expand=False):
        super().__init__()
        self.label = label
        self.value = value
        self.expand = expand

        self.min_lines = 1
        self.max_lines = 9
        self.multiline = True
        self.bgcolor = ft.Colors.SURFACE
        self.border_color = ft.Colors.BLUE_GREY_200


class CustomButton(ft.FilledButton):
    def __init__(self, text, icon, on_click):
        super().__init__()
        self.text = text
        self.icon = icon
        self.on_click = on_click

        self.color = ft.Colors.WHITE
        self.bgcolor = ft.Colors.LIGHT_BLUE_900
        self.icon_color = ft.Colors.WHITE
        self.style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
