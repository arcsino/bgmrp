import flet as ft

from controls import BodyText, CustomBorderContainer


class SoundsTab(ft.Column):
    def __init__(self, project_obj):
        super().__init__()
        self.project_obj = project_obj
        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.sounds = self.project_obj.sounds
        self.sounds_column = ft.Column(
            expand=True,
            controls=[self.get_sound_item(path) for path in self.sounds],
        )
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            ft.Row(
                controls=[
                    BodyText(
                        value="リソースパックの音声を選択してください。音声ファイルは拡張子.OGGです。",
                        expand=True,
                    ),
                    ft.VerticalDivider(width=5, color=ft.Colors.TRANSPARENT),  # margin
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
        return CustomBorderContainer(
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.AUDIO_FILE),
                    BodyText(value=path, expand=True),
                    ft.IconButton(
                        icon=ft.Icons.CLOSE,
                        icon_color=ft.Colors.WHITE,
                    ),
                ],
            )
        )
