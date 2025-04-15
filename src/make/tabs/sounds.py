import flet as ft

from controls import BodyText, BorderContainer


class SoundsTab(ft.Column):
    def __init__(self, sounds):
        super().__init__()
        self.sounds = sounds

        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.sounds_column = ft.Column(
            expand=True,
            controls=[self.get_sound_item(path) for path in self.sounds],
        )
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            ft.Row(
                controls=[
                    ft.Container(
                        expand=True,
                        content=BodyText(
                            value="リソースパックの音声を選択してください。音声ファイルは拡張子.OGGです。"
                        ),
                    ),
                    ft.IconButton(
                        icon=ft.Icons.OPEN_IN_BROWSER,
                        icon_color=ft.Colors.WHITE,
                    ),
                    ft.VerticalDivider(width=1, color=ft.Colors.TRANSPARENT),  # margin
                ],
            ),
            self.sounds_column,
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
        ]

    def get_sound_item(self, path):
        return BorderContainer(
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.AUDIO_FILE),
                    ft.Container(expand=True, content=BodyText(value=path)),
                    ft.IconButton(
                        icon=ft.Icons.CLOSE,
                        icon_color=ft.Colors.WHITE,
                    ),
                ],
            )
        )
