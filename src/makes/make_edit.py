import flet as ft
from pathlib import Path

from controls import LabelText
from makes.make_rp import get_project_dict
from makes.tabs.name import NameTab
from makes.tabs.description import DescriptionTab
from makes.tabs.icon import IconTab
from makes.tabs.sounds import SoundsTab
from makes.tabs.volume import VolumeTab
from makes.tabs.version import VersionTab


class EditTabs(ft.Tabs):
    def __init__(self, project_obj):
        super().__init__()
        self.project_obj = project_obj
        self.expand = True
        self.scrollable = False
        self.selected_index = 0
        self.animation_duration = 0
        self.tab_alignment = ft.TabAlignment.FILL
        self.tabs = [
            ft.Tab(
                text="名前",
                icon=ft.Icons.SELL,
                content=NameTab(project_obj=self.project_obj),
            ),
            ft.Tab(
                text="説明",
                icon=ft.Icons.ARTICLE,
                content=DescriptionTab(project_obj=self.project_obj),
            ),
            ft.Tab(
                text="アイコン",
                icon=ft.Icons.IMAGE,
                content=IconTab(project_obj=self.project_obj),
            ),
            ft.Tab(
                text="音声",
                icon=ft.Icons.AUDIO_FILE,
                content=SoundsTab(project_obj=self.project_obj),
            ),
            ft.Tab(
                text="音量",
                icon=ft.Icons.VOLUME_UP,
                content=VolumeTab(project_obj=self.project_obj),
            ),
            ft.Tab(
                text="バージョン",
                icon=ft.Icons.NUMBERS,
                content=VersionTab(project_obj=self.project_obj),
            ),
        ]


class EditProject(ft.Column):
    def __init__(self, back_click, next_click, project_path):
        super().__init__()
        self.expand = True
        self.visible = False
        self.back_click = back_click
        self.next_click = next_click
        self.project_path = project_path
        self.project_title = LabelText(value=self.project_path.stem)
        self.controls = []

    def update_project(self, project_path):
        self.project_path = project_path
        self.project_title.value = (
            self.project_path.stem
            if len(self.project_path.stem) <= 20
            else self.project_path.stem[:20] + "..."
        )
        self.edit_tabs = EditTabs(project_obj=get_project_dict(self.project_path))
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
            self.edit_tabs,
        ]
        self.update()
