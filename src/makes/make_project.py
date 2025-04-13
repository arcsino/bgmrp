import flet as ft
import os
from pathlib import Path

from controls import ExplainContainer, CustomTextField, CustomBorderContainer


APP_DATA_PATH = Path(os.getenv("FLET_APP_STORAGE_DATA"))


class ProjectItem(ft.Column):
    def __init__(self, project_path, update_culumn, edit_project, delete_project):
        super().__init__()
        self.project_path = project_path
        self.project_name = ft.Text(
            value=self.project_path.stem, theme_style=ft.TextThemeStyle.TITLE_MEDIUM
        )
        self.update_culumn = update_culumn
        self.edit_project = edit_project
        self.delete_project = delete_project
        self.textfield = CustomTextField(label="変更後のプロジェクト名")
        self.display_view = CustomBorderContainer(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.Icons.DESCRIPTION),  # color=ft.Colors.WHITE
                            self.project_name,
                        ]
                    ),
                    ft.PopupMenuButton(
                        icon_color=ft.Colors.WHITE,
                        items=[
                            ft.PopupMenuItem(
                                text="名称変更",
                                icon=ft.Icons.EDIT,
                                on_click=self.rename_project,
                            ),
                            ft.PopupMenuItem(
                                text="編集",
                                icon=ft.Icons.TUNE,
                                on_click=self.edit_clicked,
                            ),
                            ft.PopupMenuItem(
                                text="削除",
                                icon=ft.Icons.DELETE,
                                on_click=self.delete_clicked,
                            ),
                        ],
                    ),
                ],
            ),
        )
        self.edit_view = CustomBorderContainer(
            visible=False,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    self.textfield,
                    ft.IconButton(
                        icon=ft.Icons.CHECK,
                        icon_color=ft.Colors.WHITE,
                        on_click=self.save_project,
                    ),
                ],
            ),
        )
        self.controls = [self.display_view, self.edit_view]

    def rename_project(self, e):
        self.textfield.value = self.project_path.stem
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_project(self, e):
        self.project_name.value = self.textfield.value
        self.project_path.rename(APP_DATA_PATH / f"{self.textfield.value}.json")
        self.textfield.value = ""
        self.edit_view.visible = False
        self.display_view.visible = True
        self.update()
        self.update_project_column()

    def update_project_column(self):
        self.update_culumn(self)

    def edit_clicked(self, e):
        self.edit_project(self)

    def delete_clicked(self, e):
        self.delete_project(self)


class ProjectColumn(ft.Column):
    def __init__(self, edit_project):
        super().__init__()
        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.edit_project = edit_project
        self.projects = self.get_projects()
        self.project_column = ft.Column()
        self.textfield = CustomTextField(label="新規プロジェクト")
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            ExplainContainer(
                title="プロジェクト一覧",
                body="プロジェクトに作成時の情報を保存しておくことで、追加の変更がしやすくなります。",
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            ft.Row(
                controls=[
                    self.textfield,
                    ft.IconButton(
                        icon=ft.Icons.ADD,
                        icon_color=ft.Colors.WHITE,
                        on_click=self.new_project,
                    ),
                ]
            ),
            self.project_column,
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
        ]
        self.project_column.controls = [
            ProjectItem(
                project_path=project,
                update_culumn=self.update_project_column,
                edit_project=self.edit_project,
                delete_project=self.delete_project,
            )
            for project in self.projects
        ]

    def get_projects(self):
        return list(APP_DATA_PATH.glob("*.json"))

    def update_project_column(self, e):
        self.projects = self.get_projects()
        self.project_column.controls = [
            ProjectItem(
                project_path=project,
                update_culumn=self.update_project_column,
                edit_project=self.edit_project,
                delete_project=self.delete_project,
            )
            for project in self.projects
        ]
        self.update()

    def new_project(self, e):
        new_project = APP_DATA_PATH / f"{self.textfield.value}.json"
        try:
            self.textfield.value = ""
            if new_project.name == ".json":
                raise Exception("プロジェクト名を入力してください。")
            new_project.touch(exist_ok=False)
            self.update_project_column(e)
        except Exception as ex:
            print(ex)

    def delete_project(self, e):
        delete_project = APP_DATA_PATH / f"{e.project_path.name}"
        delete_project.unlink(missing_ok=True)
        self.update_project_column(e)
