import flet as ft
from incolume.py.ft_programadoraventureiro_8573.partials.button import MyButton

class HomeView:
    def get_content(self):
        def ok_clicked(e):
            print("OK clicked")

        button = MyButton(text="OK", on_click=ok_clicked)
        text = ft.Text(value="Bem-vindo à Home!", color=ft.colors.WHITE)
        
        layout = ft.Column(
            controls=[
                text,
                button,
            ],
            alignment=ft.alignment.center,
            expand=True
        )
        return layout
