import flet as ft
from wrapper import Wrapper


def firstget():
    data = Wrapper()
    data = data.getdata()
    return data


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

    # page.window.full_screen = True
    page.scroll = True
    page.title = "Simpsons Quotes"
    page.appbar = ft.AppBar(title=ft.Text(page.title))
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.REFRESH, on_click=lambda e: get()
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    data = firstget()
    quote = ft.Text(data["quote"])
    character = ft.Text(data["character"])
    img = ft.Image(src=data["image"])
    page.add(
        ft.SafeArea(
            ft.Column(
                controls=[ft.Column(controls=[quote, character]), img],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
    )


ft.app(main)
