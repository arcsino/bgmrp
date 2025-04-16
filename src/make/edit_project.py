import flet as ft

from controls import TitleText, CustomButton
from make.make_rp import ProjectInfo, get_project_dict, write_project_info
from make.tabs.name import NameTab
from make.tabs.description import DescriptionTab
from make.tabs.icon import IconTab
from make.tabs.sounds import SoundsTab
from make.tabs.volume import VolumeTab
from make.tabs.version import VersionTab


class EditHeader(ft.Row):
    def __init__(self, project_title, back_click, save_click, next_click):
        super().__init__()
        self.project_title = ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            content=TitleText(
                value=(
                    project_title
                    if len(project_title) <= 24
                    else project_title[:24] + "..."
                )
            ),
        )
        self.back_click = back_click
        self.save_click = save_click
        self.next_click = next_click

        self.controls = [
            ft.Container(
                height=40,
                expand=True,
                bgcolor=ft.Colors.BLUE_GREY_900,
                border_radius=ft.border_radius.all(5),
                content=ft.Row(
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
                    ],
                ),
            ),
            CustomButton(
                height=40,
                text="作成する",
                icon=ft.Icons.FOLDER_ZIP,
                on_click=self.next_clicked,
            ),
        ]

    def back_clicked(self, _):
        self.back_click()

    def save_clicked(self, _):
        self.save_click()

    def next_clicked(self, _):
        self.next_click()


class EditTabs(ft.Tabs):
    def __init__(self, project_obj: ProjectInfo):
        super().__init__()
        self.project_obj = project_obj

        self.expand = True
        self.scrollable = False
        self.selected_index = 0
        self.animation_duration = 0
        self.tab_alignment = ft.TabAlignment.FILL
        self.name_tab = NameTab(name=self.project_obj.name)
        self.description_tab = DescriptionTab(description=self.project_obj.description)
        self.icon_tab = IconTab(icon=self.project_obj.icon)
        self.sounds_tab = SoundsTab(sounds=self.project_obj.sounds)
        self.volume_tab = VolumeTab(volume=self.project_obj.volume)
        self.version_tab = VersionTab(version=self.project_obj.version)
        self.tabs = [
            ft.Tab(text="名前", icon=ft.Icons.SELL, content=self.name_tab),
            ft.Tab(text="説明", icon=ft.Icons.ARTICLE, content=self.description_tab),
            ft.Tab(text="アイコン", icon=ft.Icons.IMAGE, content=self.icon_tab),
            ft.Tab(text="音声", icon=ft.Icons.AUDIO_FILE, content=self.sounds_tab),
            ft.Tab(text="音量", icon=ft.Icons.VOLUME_UP, content=self.volume_tab),
            ft.Tab(text="バージョン", icon=ft.Icons.NUMBERS, content=self.version_tab),
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
            save_click=self.save_project,
            next_click=next_click,
        )
        self.tabs = EditTabs(project_obj=get_project_dict(self.project_path))
        self.controls = [self.header, self.tabs]

    def save_project(self):
        project_obj = ProjectInfo(
            name=self.tabs.name_tab.name,
            description=self.tabs.description_tab.description,
            icon=self.tabs.icon_tab.icon,
            sounds=self.tabs.sounds_tab.sounds,
            volume=self.tabs.volume_tab.volume,
            version=self.tabs.version_tab.version,
        )
        write_project_info(self.project_path, project_obj)
