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
    def __init__(self, label, value="", expand=False, on_change=None):
        super().__init__()
        self.label = label
        self.value = value
        self.expand = expand
        if on_change:
            self.on_change = on_change

        self.bgcolor = ft.Colors.SURFACE
        self.border_color = ft.Colors.BLUE_GREY_200


class MultiLineTextField(ft.TextField):
    def __init__(self, label, value="", expand=False, on_change=None):
        super().__init__()
        self.label = label
        self.value = value
        self.expand = expand
        if on_change:
            self.on_change = on_change

        self.min_lines = 1
        self.max_lines = 9
        self.multiline = True
        self.bgcolor = ft.Colors.SURFACE
        self.border_color = ft.Colors.BLUE_GREY_200


class CustomButton(ft.Container):
    def __init__(self, height, text, icon, on_click):
        super().__init__()
        self.height = height
        self.text = text
        self.icon = ft.Icon(name=icon, color=ft.Colors.WHITE)
        self.on_click = on_click

        self.ink = True
        self.bgcolor = ft.Colors.LIGHT_BLUE_900
        self.border_radius = ft.border_radius.all(5)
        self.padding = ft.padding.only(left=10, right=10)
        self.content = ft.Row(
            controls=[
                ft.Icon(name=ft.Icons.FOLDER_ZIP, color=ft.Colors.WHITE),
                ft.Text(value="作成する", theme_style=ft.TextThemeStyle.TITLE_SMALL),
            ]
        )
