import flet as ft
from incolume.py.ft_programadoraventureiro_8573.partials.button import MyButton
from incolume.py.ft_programadoraventureiro_8573.partials.navigation_drawer import MyNavigationDrawer

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.BLACK
        self.main()

    def main(self):
        def ok_clicked(e):
            print("OK clicked")
        
        def cancel_clicked(e):
            print("Cancel clicked")

        self.navigation_drawer = MyNavigationDrawer()
        self.content = MyButton(text="OK", on_click=ok_clicked)

        layout = ft.ResponsiveRow(
            columns=12,
            controls=[
                self.navigation_drawer,
                self.content,
            ],
            expand=True
        )

        self.page.add(layout)

if __name__ == '__main__':
    ft.app(target=App, assets_dir='assets')
