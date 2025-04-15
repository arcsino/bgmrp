import flet as ft

from controls import HeadLineText, CustomButton
from make.make_rp import get_project_dict
from make.tabs.name import NameTab
from make.tabs.description import DescriptionTab
from make.tabs.icon import IconTab
from make.tabs.sounds import SoundsTab
from make.tabs.volume import VolumeTab
from make.tabs.version import VersionTab


class EditHeader(ft.Container):
    def __init__(self, project_title, back_click, next_click):
        super().__init__()
        self.project_title = ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            content=HeadLineText(
                value=(
                    project_title
                    if len(project_title) <= 20
                    else project_title[:20] + "..."
                )
            ),
        )
        self.back_click = back_click
        self.next_click = next_click

        self.bgcolor = ft.Colors.BLUE_GREY_900
        self.border_radius = ft.border_radius.all(5)
        self.content = ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    icon_color=ft.Colors.WHITE,
                    on_click=self.back_clicked,
                ),
                self.project_title,
                ft.IconButton(
                    icon=ft.Icons.SAVE,
                    icon_color=ft.Colors.WHITE,
                    on_click=self.save_clicked,
                ),
                CustomButton(
                    text="作成する",
                    icon=ft.Icons.FOLDER_ZIP,
                    on_click=self.next_clicked,
                ),
                ft.VerticalDivider(width=1, color=ft.Colors.TRANSPARENT),  # margin
            ],
        )

    def back_clicked(self, e):
        self.back_click()

    def save_clicked(self, e):
        pass

    def next_clicked(self, e):
        self.next_click()


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
                content=NameTab(name=self.project_obj.name),
            ),
            ft.Tab(
                text="説明",
                icon=ft.Icons.ARTICLE,
                content=DescriptionTab(description=self.project_obj.description),
            ),
            ft.Tab(
                text="アイコン",
                icon=ft.Icons.IMAGE,
                content=IconTab(icon=self.project_obj.icon),
            ),
            ft.Tab(
                text="音声",
                icon=ft.Icons.AUDIO_FILE,
                content=SoundsTab(sounds=self.project_obj.sounds),
            ),
            ft.Tab(
                text="音量",
                icon=ft.Icons.VOLUME_UP,
                content=VolumeTab(volume=self.project_obj.volume),
            ),
            ft.Tab(
                text="バージョン",
                icon=ft.Icons.NUMBERS,
                content=VersionTab(version=self.project_obj.version),
            ),
        ]


class EditProject(ft.Column):
    def __init__(self, project_path, back_click, next_click):
        super().__init__()
        self.project_path = project_path
        self.back_click = back_click
        self.next_click = next_click

        self.expand = True
        self.header = EditHeader(
            project_title=self.project_path.stem,
            back_click=self.back_click,
            next_click=next_click,
        )
        self.tabs = EditTabs(project_obj=get_project_dict(self.project_path))
        self.controls = [self.header, self.tabs]
