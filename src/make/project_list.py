import flet as ft

from controls import (
    BorderContainer,
    CustomTextField,
    ExplainContainer,
    TitleText,
    CustomDialog,
    ShortButton,
)
from make.module import (
    get_project_obj,
    get_icon_image,
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
                        icon_color=ft.Colors.ON_PRIMARY_CONTAINER,
                        on_click=self.new_clicked,
                    ),
                ]
            ),
            ft.Divider(height=5),
        ]

    def new_clicked(self, _):
        self.new_project()


class ProjectItem(ft.Column):
    def __init__(self, project_path, update_list, edit_project, delete_project):
        super().__init__()
        self.project_path = project_path
        self.update_list = update_list
        self.edit_project = edit_project
        self.delete_project = delete_project

        self.project_obj = get_project_obj(self.project_path)
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
                                ft.Image(
                                    src=get_icon_image(self.project_obj.icon),
                                    border_radius=ft.border_radius.all(5),
                                    width=50,
                                ),
                                self.project_name,
                            ],
                        ),
                        ft.PopupMenuButton(
                            icon_color=ft.Colors.ON_PRIMARY_CONTAINER,
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
                            icon_color=ft.Colors.ON_PRIMARY_CONTAINER,
                            on_click=self.save_project,
                        ),
                    ],
                ),
            )
        ]

    def rename_project(self, _):
        self.textfield.value = self.project_path.stem
        self.change_edit_view()
        self.update()

    def save_project(self, _):
        self.project_name.value = self.textfield.value
        self.project_path = rename_project_file(self.project_path, self.textfield.value)
        self.textfield.value = ""
        self.index = self.change_default_view()
        self.update_list()  # update()

    def edit_clicked(self, _):
        self.edit_project(self)

    def delete_clicked(self, _):
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
                delete_project=self.confilm_delete_project,
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
                delete_project=self.confilm_delete_project,
            )
            for project in self.projects
        ]
        self.update()

    def new_project(self):
        new = new_project_file(self.new.textfield.value)
        if new:  # if new is Error
            self.dialog_open(
                icon=ft.Icons.ERROR,
                icon_color=ft.Colors.RED,
                title="エラー",
                content=new,
                actions=[ShortButton(height=32, text="OK", on_click=self.dialog_close)],
            )
        else:
            self.dialog_open(
                icon=ft.Icons.INFO,
                icon_color=ft.Colors.BLUE,
                title="プロジェクトを作成しました",
                content=str(self.new.textfield.value),
                actions=[ShortButton(height=32, text="OK", on_click=self.dialog_close)],
            )
        self.new.textfield.value = ""
        self.update_project_items()

    def confilm_delete_project(self, item: ProjectItem):
        self.dialog_open(
            icon=ft.Icons.WARNING,
            icon_color=ft.Colors.AMBER,
            title="本当に削除しますか？",
            content=f"削除すると二度と元に戻りません。\n{item.project_name.value}",
            actions=[
                ShortButton(
                    height=32,
                    text="No",
                    bgcolor=ft.Colors.BLUE,
                    on_click=self.dialog_close,
                ),
                ShortButton(
                    height=32,
                    text="Delete",
                    bgcolor=ft.Colors.RED,
                    on_click=lambda _: self.delete_project(item),
                ),
            ],
        )

    def delete_project(self, item: ProjectItem):
        delete_project_file(item.project_path)
        self.update_project_items()
        self.dialog_close(item)

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
