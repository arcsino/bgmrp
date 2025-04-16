import flet as ft
from pathlib import Path

from controls import BodyText, BorderContainer
from make.make_rp import get_icon_image


class IconTab(ft.Column):
    def __init__(self, icon):
        super().__init__()
        self.icon = icon

        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.file_picker = ft.FilePicker(on_result=self.pickfile_result)
        self.input_controls()

    def input_controls(self):
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            BodyText(
                value="リソースパックのアイコンを選択してください。画像ファイルは拡張子.PNGです。"
            ),
            ft.Row(
                controls=[
                    BorderContainer(
                        content=ft.Row(
                            controls=[
                                ft.Image(
                                    src=get_icon_image(self.icon),
                                    border_radius=ft.border_radius.all(5),
                                    width=50,
                                ),
                                ft.Container(
                                    expand=True,
                                    content=BodyText(
                                        value=(
                                            self.icon
                                            if self.icon
                                            else "画像を選択してください。"
                                        )
                                    ),
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.OPEN_IN_BROWSER,
                                    icon_color=ft.Colors.WHITE,
                                    on_click=lambda _: self.file_picker.pick_files(
                                        dialog_title="画像を選択",
                                        initial_directory=Path.cwd(),
                                        allowed_extensions=["png", "PNG"],
                                    ),
                                ),
                            ],
                        )
                    ),
                    ft.VerticalDivider(width=1, color=ft.Colors.TRANSPARENT),  # margin
                ]
            ),
        ]

    def pickfile_result(self, icon: ft.FilePickerResultEvent):
        if icon.files:
            icon_path = icon.files[0].path
            self.icon = icon_path
            self.input_controls()
            self.update()

    # Adding a FilePicker to the page content
    def did_mount(self):
        self.page.overlay.append(self.file_picker)
        self.page.update()

    # Removing a FilePicker to the page content
    def will_unmount(self):
        self.page.overlay.remove(self.file_picker)
        self.page.update()
