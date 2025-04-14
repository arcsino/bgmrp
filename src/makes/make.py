import flet as ft
from pathlib import Path

from makes.make_project import ProjectColumn
from makes.make_edit import EditProject


class MakeView(ft.Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.index_0 = ProjectColumn(edit_project=self.edit_project)
        self.index_1 = EditProject(
            back_click=self.project_list,
            next_click=self.save_project,
            project_path=Path(),
        )
        self.controls = [self.index_0, self.index_1]

    def project_list(self, e):
        for control in self.controls:
            control.visible = False
        self.index_0.visible = True
        self.index_1.controls = []
        self.update()

    def edit_project(self, e):
        for control in self.controls:
            control.visible = False
        self.index_1.visible = True
        self.index_1.update_project(e.project_path)
        self.update()

    def save_project(self, e):
        pass


def make_view():
    make = MakeView()
    make.visible = False
    return make
