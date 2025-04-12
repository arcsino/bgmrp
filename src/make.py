import flet as ft
import os
from pathlib import Path

from controls import ExplainContainer


APP_DATA_PATH = Path(os.getenv("FLET_APP_STORAGE_DATA"))


class NewProject(ft.Column):
    def __init__(self, project_path, update_culumn, delete_project):
        super().__init__()
        self.project_path = project_path
        self.project_name = ft.Text(value=self.project_path.stem)
        self.update_culumn = update_culumn
        self.delete_project = delete_project
        self.textfield = ft.TextField(
            label="Edit Project Name", border_color=ft.Colors.BLUE_GREY_100
        )
        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(name=ft.Icons.FOLDER, color=ft.Colors.WHITE),
                        self.project_name,
                    ]
                ),
                ft.PopupMenuButton(
                    icon_color=ft.Colors.WHITE,
                    items=[
                        ft.PopupMenuItem(
                            text="Edit",
                            icon=ft.Icons.EDIT,
                            on_click=self.edit_project,
                        ),
                        ft.PopupMenuItem(
                            text="Delete",
                            icon=ft.Icons.DELETE,
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )
        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                self.textfield,
                ft.IconButton(
                    icon=ft.Icons.CHECK,
                    icon_color=ft.Colors.WHITE,
                    on_click=self.save_project,
                ),
            ],
        )
        self.controls = [self.display_view, self.edit_view]

    def edit_project(self, e):
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

    def delete_clicked(self, e):
        self.delete_project(self)


class MakeView(ft.Column):
    def __init__(self):
        super().__init__()
        self.projects = self.get_projects()
        self.project_column = ft.Column()
        self.textfield = ft.TextField(
            label="New Project", border_color=ft.Colors.BLUE_GREY_100
        )
        self.index_0 = ft.Column(
            controls=[
                ExplainContainer(
                    title="Projects", body="プロジェクトを選択してください。"
                ),
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
            ]
        )
        self.controls = [self.index_0]
        self.project_column.controls = [
            NewProject(
                project_path=project,
                update_culumn=self.update_project_column,
                delete_project=self.delete_project,
            )
            for project in self.projects
        ]

    def get_projects(self):
        return list(APP_DATA_PATH.glob("*.json"))

    def update_project_column(self, e):
        self.projects = self.get_projects()
        self.project_column.controls = [
            NewProject(
                project_path=project,
                update_culumn=self.update_project_column,
                delete_project=self.delete_project,
            )
            for project in self.projects
        ]
        self.update()

    def new_project(self, e):
        new_project = APP_DATA_PATH / f"{self.textfield.value}.json"
        try:
            self.textfield.value = ""
            new_project.touch(exist_ok=False)
            self.update_project_column(e)
        except Exception as ex:
            print(ex)

    def delete_project(self, e):
        delete_project = APP_DATA_PATH / f"{e.project_path.name}"
        delete_project.unlink(missing_ok=True)
        self.update_project_column(e)


def make_view():
    make = MakeView()
    make.visible = False
    return make
