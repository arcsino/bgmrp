import flet as ft
from pathlib import Path

from controls import TitleText, CustomIconButton, ShortButton, CustomDialog
from make.module import (
    ProjectInfo,
    get_project_obj,
    write_project_info,
    check_entry,
    make_rp,
)
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
                bgcolor=ft.Colors.ON_INVERSE_SURFACE,
                border_radius=ft.border_radius.all(5),
                content=ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            icon_color=ft.Colors.ON_PRIMARY_CONTAINER,
                            on_click=self.back_clicked,
                        ),
                        self.project_title,
                        ft.IconButton(
                            icon=ft.Icons.SAVE,
                            icon_color=ft.Colors.ON_PRIMARY_CONTAINER,
                            on_click=self.save_clicked,
                        ),
                    ],
                ),
            ),
            CustomIconButton(
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
            ft.Tab(text="BGM", icon=ft.Icons.AUDIO_FILE, content=self.sounds_tab),
            ft.Tab(text="音量", icon=ft.Icons.VOLUME_UP, content=self.volume_tab),
            ft.Tab(text="バージョン", icon=ft.Icons.NUMBERS, content=self.version_tab),
        ]


class EditProject(ft.Column):
    def __init__(self, project_path, back_clicking):
        super().__init__()
        self.project_path = project_path
        self.back_clicking = back_clicking

        self.expand = True
        self.file_picker = ft.FilePicker(on_result=self.pickfile_result)
        self.header = EditHeader(
            project_title=self.project_path.stem,
            back_click=self.back_click,
            save_click=self.save_project_with_dlg,
            next_click=self.next_click,
        )
        self.tabs = EditTabs(project_obj=get_project_obj(self.project_path))
        self.controls = [self.header, self.tabs]

    def get_edited_project_obj(self):
        return ProjectInfo(
            name=self.tabs.name_tab.name,
            description=self.tabs.description_tab.description,
            icon=self.tabs.icon_tab.icon,
            sounds=self.tabs.sounds_tab.sounds,
            volume=self.tabs.volume_tab.volume,
            version=self.tabs.version_tab.version,
        )

    def back_click(self):
        if not get_project_obj(self.project_path) == self.get_edited_project_obj():
            self.dialog_open(
                icon=ft.Icons.WARNING,
                icon_color=ft.Colors.AMBER,
                title="変更を保存してません！",
                content="保存してプロジェクト一覧へ戻りますか？",
                actions=[
                    ShortButton(
                        height=32,
                        text="Save",
                        bgcolor=ft.Colors.BLUE,
                        on_click=self.dialog_close_back_btn_yes,
                    ),
                    ShortButton(
                        height=32,
                        text="No",
                        bgcolor=ft.Colors.RED,
                        on_click=self.dialog_close_back_btn_no,
                    ),
                ],
            )
        else:
            self.back_clicking()

    def save_project(self):
        project_obj = self.get_edited_project_obj()
        write_project_info(self.project_path, project_obj)

    def save_project_with_dlg(self):
        self.save_project()
        self.dialog_open(
            icon=ft.Icons.INFO,
            icon_color=ft.Colors.BLUE,
            title="プロジェクトを保存しました",
            content="ドキュメントにあるfletフォルダを削除すると、データが消えます。",
            actions=[ShortButton(height=32, text="OK", on_click=self.dialog_close)],
        )

    def next_click(self):
        self.save_project()
        project_obj = get_project_obj(self.project_path)
        check = check_entry(project_obj)
        if not check:  # if not error
            self.file_picker.save_file(
                dialog_title="リソースパックの保存先",
                file_name=f"{project_obj.name}.zip",
                initial_directory=Path.cwd(),
                allowed_extensions=["zip", "ZIP"],
            )
        else:
            self.dialog_open(
                icon=ft.Icons.ERROR,
                icon_color=ft.Colors.RED,
                title="エラー",
                content=check,
                actions=[ShortButton(height=32, text="OK", on_click=self.dialog_close)],
            )

    def pickfile_result(self, rp: ft.FilePickerResultEvent):
        if rp.path:
            rp_path = rp.path
            project_obj = get_project_obj(self.project_path)
            self.dialog_open(
                icon=ft.Icons.HOURGLASS_TOP,
                icon_color=ft.Colors.GREEN,
                title="リソースパックを作成中...",
                content="音声ファイルの数やサイズによっては、時間がかかる場合があります。",
                actions=[],
            )
            making = make_rp(rp_path, project_obj)
            self.dialog_close(0)
            if not making:  # if not error
                self.dialog_open(
                    icon=ft.Icons.INFO,
                    icon_color=ft.Colors.BLUE,
                    title="リソースパックを作成しました",
                    content=f"BGMリソースパックを{project_obj.name}.zipとして{rp.path}に保存しました。",
                    actions=[
                        ShortButton(height=32, text="OK", on_click=self.dialog_close)
                    ],
                )
            else:
                self.dialog_open(
                    icon=ft.Icons.ERROR,
                    icon_color=ft.Colors.RED,
                    title="エラー",
                    content=making,
                    actions=[
                        ShortButton(height=32, text="OK", on_click=self.dialog_close)
                    ],
                )

    def dialog_open(self, icon, icon_color, title, content, actions):
        self.dlg = CustomDialog(
            icon=icon,
            icon_color=icon_color,
            title=title,
            content=ft.Text(value=content, text_align=ft.TextAlign.CENTER),
            actions=actions,
        )
        self.page.open(self.dlg)

    def dialog_close(self, _):
        self.page.close(self.dlg)

    def dialog_close_back_btn_yes(self, _):
        self.save_project()
        self.page.close(self.dlg)
        self.back_clicking()

    def dialog_close_back_btn_no(self, _):
        self.page.close(self.dlg)
        self.back_clicking()

    # Adding a FilePicker to the page content
    def did_mount(self):
        self.page.overlay.append(self.file_picker)
        self.page.update()

    # Removing a FilePicker to the page content
    def will_unmount(self):
        self.page.overlay.remove(self.file_picker)
        self.page.update()
