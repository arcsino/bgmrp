import flet as ft

from controls import ShortButton, CustomDialog


class MakingRP(ft.Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.scroll = ft.ScrollMode.AUTO

        self.dlg = CustomDialog(
            icon=ft.Icons.HOURGLASS_TOP,
            title="リソースパックを作成中...",
            content=ft.Text(
                value="音声ファイルの数やサイズによっては、時間がかかる場合があります。",
                text_align=ft.TextAlign.CENTER,
            ),
            actions=[],
        )
        self.controls = [
            ft.ElevatedButton(
                "Open modal dialog", on_click=lambda e: self.page.open(self.dlg)
            )
        ]

    def handle_close(self, _):
        self.page.close(self.dlg)
