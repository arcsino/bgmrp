import flet as ft

from make.project_list import ProjectItem, ProjectList
from make.edit_project import EditProject


class MakeView(ft.Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.visible = False
        self.controls = [ProjectList(self.edit_project)]

    def project_list(self):
        self.controls = [ProjectList(self.edit_project)]
        self.update()

    def edit_project(self, item: ProjectItem):
        self.controls = [
            EditProject(
                project_path=item.project_path,
                back_click=self.project_list,
                next_click=self.making_rp,
            )
        ]
        self.update()

    def making_rp(self):
        pass
