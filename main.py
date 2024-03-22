import flet as ft
from wrapper import Wrapper


def firstget():
    data = Wrapper()
    data = data.getdata()
    return data


# firstget = firstget()


def main(page: ft.Page):
    def get():
        data = Wrapper()
        data = data.getdata()
        quote.value = data["quote"]
        quote.update()
        character.value = data["character"]
        character.update()
        img.src = data["image"]
        img.update()

    page.scroll = True
    page.title = "Simpsons Quotes"
    page.appbar = ft.AppBar(title=ft.Text(page.title))
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.REFRESH, on_click=lambda e: get()
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    quote = ft.Text("Please refresh")
    character = ft.Text("Please refresh")
    img = ft.Image(src="assets/icon.png")
    page.add(
        ft.SafeArea(ft.Column(controls=[ft.Column(controls=[quote, character]), img]))
    )


ft.app(main)
