import flet as ft

from controls import BodyText


class VolumeTab(ft.Column):
    def __init__(self, project_obj):
        super().__init__()
        self.project_obj = project_obj
        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.slider = ft.Slider(
            value=self.project_obj.volume,
            min=0,
            max=100,
            divisions=10,
            label="{value}%",
        )
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            BodyText(value="BGMの音量を設定してください。"),
            self.slider,
        ]
