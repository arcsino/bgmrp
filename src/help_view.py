import flet as ft
from pathlib import Path

from controls import BodyText, ExplainContainer, SmallExplainContainer


class HelpView(ft.Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.visible = False
        self.scroll = ft.ScrollMode.AUTO
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            ExplainContainer(
                title="リソースパックの作り方",
                body="以下にリソースパックを作り方、作る上での注意点などを説明します。",
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.1
            SmallExplainContainer(
                title="1. アイコンを用意する",
                body="リソースパックのアイコン、画像を用意します。画像ファイルの拡張子は.PNGで、サイズは1:1にしておいてください。",
            ),
            ft.Image(
                src=Path("images/help1.png"),
                border_radius=ft.border_radius.all(10),
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.2
            SmallExplainContainer(
                title="2. BGMを用意する",
                body="リソースパックのBGM、オーディオを用意します。オーディオファイルの拡張子は.OGGで、アーティスト情報などの不要な情報は追加しないでください。",
            ),
            BodyText(
                value="オンラインのOGGコンバーターを使う場合は、ウイルスなどが入ったファイルをダウンロードしないよう、信頼の出来るものを利用してください。"
            ),
            ft.Image(
                src=Path("images/help2.png"),
                border_radius=ft.border_radius.all(10),
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.3
            SmallExplainContainer(
                title="3. プロジェクトを作成する",
                body="プロジェクトとはリソースパック作成時の情報（名前、説明、アイコン、etc）を保存するための物です。一度作成したリソースパックに追加でBGMを設定したい時に、また0から設定し直す必要がなくなります。",
            ),
            BodyText(
                value="※ドキュメントにあるfletフォルダを削除するとプロジェクトの情報が消えます。"
            ),
            BodyText(
                value="※保存していたアイコンの画像ファイルとBGMのオーディオファイルを移動したり削除すると、保存していた情報は全て失われます。"
            ),
            ft.Image(
                src=Path("images/help3.png"),
                border_radius=ft.border_radius.all(10),
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.4
            SmallExplainContainer(
                title="4. プロジェクトを編集する",
                body="編集ボタンを押すと、作成するリソースパックの詳細設定が出来ます。",
            ),
            ft.Image(
                src=Path("images/help4.png"),
                border_radius=ft.border_radius.all(10),
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.5
            SmallExplainContainer(
                title="5. リソースパックの名前を入力する",
                body="保存する際にも変更はできますが、空欄だと作成できません。安全のため半角英数字にすることをお勧めします。",
            ),
            ft.Image(
                src=Path("images/help5.png"),
                border_radius=ft.border_radius.all(10),
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.6
            SmallExplainContainer(
                title="6. リソースパックの説明を入力する",
                body="空欄だと作成できません。安全のため半角英数字にすることをお勧めします。",
            ),
            ft.Image(
                src=Path("images/help6.png"),
                border_radius=ft.border_radius.all(10),
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.7
            SmallExplainContainer(
                title="7. リソースパックのアイコンを選択する",
                body="用意しておいたアイコンの画像を選択してください。拡張子は.PNGです。",
            ),
            ft.Image(
                src=Path("images/help7.png"),
                border_radius=ft.border_radius.all(10),
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.8
            SmallExplainContainer(
                title="8. BGMを選択する",
                body="用意しておいたオーディオを選択してください。拡張子は.OGGです。複数選択できます。",
            ),
            BodyText(
                value="複数選択した場合、BGMはランダムに再生されます。（Minecraftの仕様）"
            ),
            ft.Image(
                src=Path("images/help8.png"),
                border_radius=ft.border_radius.all(10),
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.9
            SmallExplainContainer(
                title="9. BGMの音量を設定する",
                body="100%で変更なしです。普通に聴いて音量が大きい場合は、音量を下げてください。あまり大きすぎると効果音がかき消されます。",
            ),
            ft.Image(
                src=Path("images/help9.png"),
                border_radius=ft.border_radius.all(10),
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.10
            SmallExplainContainer(
                title="10. バージョンを設定する",
                body="プレイするMinecraftのバージョンに合わせてください。違うバージョンで使おうとすると、警告が出る場合があります。",
            ),
            ft.Image(
                src=Path("images/help10.png"),
                border_radius=ft.border_radius.all(10),
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.11
            SmallExplainContainer(
                title="11. 保存する",
                body="プロジェクトの保存は、右上のアイコンを押すとできます。",
            ),
            ft.Image(
                src=Path("images/help11.png"),
                border_radius=ft.border_radius.all(10),
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.12
            SmallExplainContainer(
                title="12. 作成する",
                body="「作成する」のボタンを押すと、設定内容に不備がなければ保存先を選択するダイアログが出てきます。無事作成されると以下の画像のようになります。",
            ),
            ft.Image(
                src=Path("images/help12.png"),
                border_radius=ft.border_radius.all(10),
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.13
            SmallExplainContainer(
                title="13. エラーについて",
                body="設定内容に不備があれば発生しますが、不備がないのに発生たり、英語で書かれたエラーメッセージなど、不具合があった場合は、私に知らせてください。",
            ),
            ft.Image(
                src=Path("images/help13.png"),
                border_radius=ft.border_radius.all(10),
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
        ]
