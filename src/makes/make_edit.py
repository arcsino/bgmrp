import flet as ft

from controls import LabelText


class EditTabs(ft.Tabs):
    def __init__(self):
        super().__init__()
        self.scrollable = False
        self.selected_index = 0
        self.animation_duration = 300
        self.tab_alignment = ft.TabAlignment.FILL
        self.tabs = [
            ft.Tab(
                text="名前",
                icon=ft.Icons.SELL,
                content=ft.Text("This is Tab 1"),
            ),
            ft.Tab(
                text="説明",
                icon=ft.Icons.ARTICLE,
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="アイコン",
                icon=ft.Icons.IMAGE,
                content=ft.Text("This is Tab 3"),
            ),
            ft.Tab(
                text="音声",
                icon=ft.Icons.AUDIO_FILE,
                content=ft.Text("This is Tab 4"),
            ),
            ft.Tab(
                text="音量",
                icon=ft.Icons.VOLUME_UP,
                content=ft.Text("This is Tab 5"),
            ),
            ft.Tab(
                text="バージョン",
                icon=ft.Icons.NUMBERS,
                content=ft.Text("This is Tab 6"),
            ),
        ]


class EditProject(ft.Column):
    def __init__(self, back_click, next_click, project):
        super().__init__()
        self.visible = False
        self.back_click = back_click
        self.next_click = next_click
        self.project = project
        self.project_title = LabelText(value=self.project.stem)
        self.controls = [
            ft.Container(
                bgcolor=ft.Colors.BLUE_GREY_900,
                border_radius=ft.border_radius.all(5),
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            icon_color=ft.Colors.WHITE,
                            on_click=self.back_click,
                        ),
                        self.project_title,
                        ft.IconButton(
                            icon=ft.Icons.SAVE,
                            icon_color=ft.Colors.WHITE,
                            on_click=self.next_click,
                        ),
                    ],
                ),
            ),
            EditTabs(),
        ]
