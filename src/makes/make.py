import flet as ft

from makes.make_project import ProjectColumn


class MakeView(ft.Column):
    def __init__(self):
        super().__init__()
        self.index_0 = ProjectColumn(edit_project=self.edit_project)
        self.index_1 = ft.Column(controls=[ft.Text(value="index_1")], visible=False)
        self.controls = [self.index_0, self.index_1]

    def edit_project(self, e):
        for control in self.controls:
            control.visible = False
        self.index_1.visible = True
        self.update()
        print(e.project_path.name)


def make_view():
    make = MakeView()
    make.visible = False
    return make
