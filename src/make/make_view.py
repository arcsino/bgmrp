import flet as ft

from make.project_list import ProjectItem, ProjectList
from make.edit_project import EditProject
from make.making_rp import MakingRP


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
                back_clicking=self.project_list,
            )
        ]
        self.update()
