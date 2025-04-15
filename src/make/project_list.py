import flet as ft

from controls import BorderContainer, CustomTextField, ExplainContainer, TitleText
from make.make_rp import (
    rename_project_file,
    get_project_files,
    new_project_file,
    delete_project_file,
)


class NewProject(ft.Column):
    def __init__(self, new_project):
        super().__init__()
        self.new_project = new_project
        self.textfield = CustomTextField(label="新規プロジェクト")
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            ExplainContainer(
                title="プロジェクト一覧",
                body="プロジェクトに作成時の情報を保存しておくことで、追加の変更がしやすくなります。",
            ),
            ft.Row(
                controls=[
                    self.textfield,
                    ft.IconButton(
                        icon=ft.Icons.ADD,
                        icon_color=ft.Colors.WHITE,
                        on_click=self.new_clicked,
                    ),
                ]
            ),
            ft.Divider(color=ft.Colors.BLUE_GREY),
        ]

    def new_clicked(self, e):
        self.new_project()


class ProjectItem(ft.Column):
    def __init__(self, project_path, update_list, edit_project, delete_project):
        super().__init__()
        self.project_path = project_path
        self.update_list = update_list
        self.edit_project = edit_project
        self.delete_project = delete_project

        self.project_name = TitleText(value=self.project_path.stem)
        self.textfield = CustomTextField(label="変更後のプロジェクト名")
        self.change_default_view()

    def change_default_view(self):
        self.controls = [
            BorderContainer(
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row(
                            expand=True,
                            controls=[
                                ft.Icon(name=ft.Icons.DESCRIPTION),
                                self.project_name,
                            ],
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
        ]

    def change_edit_view(self):
        self.controls = [
            BorderContainer(
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
        ]

    def rename_project(self, e):
        self.textfield.value = self.project_path.stem
        self.change_edit_view()
        self.update()

    def save_project(self, e):
        self.project_name.value = self.textfield.value
        self.project_path = rename_project_file(self.project_path, self.textfield.value)
        self.textfield.value = ""
        self.index = self.change_default_view()
        self.update_list()  # update()

    def edit_clicked(self, e):
        self.edit_project(self)

    def delete_clicked(self, e):
        self.delete_project(self)


class ProjectList(ft.Column):
    def __init__(self, edit_project):
        super().__init__()
        self.edit_project = edit_project

        self.expand = True
        self.projects = get_project_files()
        self.new = NewProject(new_project=self.new_project)
        self.project_items = ft.Column(expand=True, scroll=ft.ScrollMode.AUTO)
        self.controls = [self.new, self.project_items]
        self.project_items.controls = [
            ProjectItem(
                project_path=project,
                update_list=self.update_project_items,
                edit_project=self.edit_project,
                delete_project=self.delete_project,
            )
            for project in self.projects
        ]

    def update_project_items(self):
        self.projects = get_project_files()
        self.project_items.controls = [
            ProjectItem(
                project_path=project,
                update_list=self.update_project_items,
                edit_project=self.edit_project,
                delete_project=self.delete_project,
            )
            for project in self.projects
        ]
        self.update()

    def new_project(self):
        new_project_file(self.new.textfield.value)
        self.new.textfield.value = ""
        self.update_project_items()

    def delete_project(self, item):
        delete_project_file(item.project_path)
        self.update_project_items()
