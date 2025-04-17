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
        self.bgcolor = ft.Colors.ON_INVERSE_SURFACE
        self.border = ft.border.all(1, ft.Colors.ON_SURFACE_VARIANT)
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
                    bgcolor=ft.Colors.ON_INVERSE_SURFACE,
                    border_radius=ft.border_radius.all(5),
                ),
                BodyText(value=self.body),
            ],
        )


class SmallExplainContainer(ft.Container):
    def __init__(self, title, body):
        super().__init__()
        self.title = title
        self.body = body

        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(
                        value=self.title, theme_style=ft.TextThemeStyle.TITLE_LARGE
                    ),
                    padding=ft.padding.all(5),
                    bgcolor=ft.Colors.ON_INVERSE_SURFACE,
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
        self.border_color = ft.Colors.ON_SURFACE_VARIANT


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
        self.border_color = ft.Colors.ON_SURFACE_VARIANT


class CustomButton(ft.Container):
    def __init__(self, height, text, on_click, bgcolor=None):
        super().__init__()
        self.height = height
        self.text = text
        self.on_click = on_click
        if bgcolor:
            self.bgcolor = bgcolor
        else:
            self.bgcolor = ft.Colors.ON_INVERSE_SURFACE

        self.ink = True
        self.expand = False
        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(5)
        self.padding = ft.padding.only(left=10, right=10)
        self.content = ft.Text(
            value=self.text, theme_style=ft.TextThemeStyle.TITLE_SMALL
        )


class ShortButton(CustomButton):
    def __init__(self, height, text, on_click, bgcolor=None):
        super().__init__(height, text, on_click)
        self.width = 100
        if bgcolor:
            self.bgcolor = bgcolor
        else:
            self.bgcolor = ft.Colors.PRIMARY_CONTAINER


class CustomIconButton(CustomButton):
    def __init__(self, height, text, icon, on_click):
        super().__init__(height, text, on_click)
        self.text = ft.Text(value=text, theme_style=ft.TextThemeStyle.TITLE_SMALL)
        self.icon = ft.Icon(name=icon, color=ft.Colors.ON_SECONDARY_CONTAINER)

        self.content = ft.Row(controls=[self.icon, self.text])


class CustomDialog(ft.AlertDialog):
    def __init__(self, icon, icon_color, title, content, actions):
        super().__init__()
        self.icon = ft.Icon(name=icon, color=icon_color)
        self.title = ft.Text(value=title, text_align=ft.TextAlign.CENTER)
        self.content = content
        self.actions = actions

        self.modal = True
        self.shape = ft.RoundedRectangleBorder(radius=10)
        self.actions_alignment = ft.MainAxisAlignment.CENTER
