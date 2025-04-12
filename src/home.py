import flet as ft

from controls import TitleText, BodyText, ExplainContainer


def home_view():
    return ft.Column(
        controls=[
            ExplainContainer(
                title="Bgm RP Maker",
                body="Bgmrp is a desktop app that enables you to easily create resource pack that change the BGM of Minecraft.",
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),
            ExplainContainer(
                title="v3.0.0",
                body="[+] Changed UI library from customtkinter to flet\n[+] No commands are required to play BGM. (You can listen to BGM in survival mode.)",
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        scroll=ft.ScrollMode.AUTO,
    )
