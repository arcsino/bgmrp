import flet as ft

from controls import BodyText


class VolumeTab(ft.Column):
    def __init__(self, volume):
        super().__init__()
        self.volume = volume

        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.slider = ft.Slider(
            value=self.volume,
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
