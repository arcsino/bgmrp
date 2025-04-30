import flet as ft
from pathlib import Path

from controls import BodyText, BorderContainer


class SoundsTab(ft.Column):
    def __init__(self, sounds: list):
        super().__init__()
        self.sounds = sounds

        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.file_picker = ft.FilePicker(on_result=self.pickfiles_result)
        self.input_controls()

    def input_controls(self):
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            ft.Row(
                controls=[
                    ft.Container(
                        expand=True,
                        content=BodyText(
                            value="追加するBGMを選択してください。オーディオファイルは拡張子.OGGです。"
                        ),
                    ),
                    ft.IconButton(
                        icon=ft.Icons.OPEN_IN_BROWSER,
                        icon_color=ft.Colors.ON_PRIMARY_CONTAINER,
                        on_click=lambda _: self.file_picker.pick_files(
                            dialog_title="音声ファイルを選択",
                            initial_directory=Path.cwd(),
                            allowed_extensions=["ogg", "OGG"],
                            allow_multiple=True,
                        ),
                    ),
                    ft.VerticalDivider(width=1, color=ft.Colors.TRANSPARENT),  # margin
                ],
            ),
            ft.Column(
                expand=True,
                controls=[
                    self.get_sound_item(path, index)
                    for index, path in enumerate(self.sounds)
                ],
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
        ]

    def get_sound_item(self, path, index):
        return BorderContainer(
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.AUDIO_FILE),
                    ft.Container(expand=True, content=BodyText(value=path)),
                    ft.IconButton(
                        icon=ft.Icons.CLOSE,
                        icon_color=ft.Colors.ON_PRIMARY_CONTAINER,
                        on_click=lambda _: self.delete_sound(index),
                    ),
                ],
            )
        )

    def pickfiles_result(self, sounds: ft.FilePickerResultEvent):
        if sounds.files:
            sounds_path = [file.path for file in sounds.files]
            for path in sounds_path:
                self.sounds.append(path)
            self.sounds = list(set(self.sounds))
            self.sounds.sort()
            self.input_controls()
            self.update()

    def delete_sound(self, index):
        self.sounds.remove(self.sounds[index])
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
