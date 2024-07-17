import flet as ft

from incolume.py.ft_programadoraventureiro_8573.partials.app_bar import MyAppBar
from incolume.py.ft_programadoraventureiro_8573.partials.navigation_drawer import MyNavigationDrawer
from incolume.py.ft_programadoraventureiro_8573.views.home_view import HomeView
from incolume.py.ft_programadoraventureiro_8573.views.pedido_view import PedidoView
from incolume.py.ft_programadoraventureiro_8573.views.store_view import StoreView

# Telas e partes
# from partials.navigation_drawer import MyNavigationDrawer
# from partials.app_bar import MyAppBar
# from views.home_view import HomeView
# from views.store_view import StoreView
# from views.pedido_view import PedidoView

# ===========================================================================================================

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.BLACK
        self.page.title = "Sistema SV em Flet"
        self.page.theme_mode = "dark"
        self.page.window.center()

        self.page.theme = ft.Theme(page_transitions={
            'windows': ft.PageTransitionTheme.CUPERTINO
        })

        self.setup_navigation()
        self.page.update()

    def setup_navigation(self):
        def indicador_de_tela(e):
            menu_selecionado = e.control.selected_index
            match menu_selecionado:
                case 0:
                    self.page.go("/")
                case 1:
                    self.page.go("/store")
                case 2:
                    self.page.go("/pedido")                    
                case _:
                    self.page.go("/")

        self.page.drawer = MyNavigationDrawer(on_change=indicador_de_tela)

        def route_change(event):
            route = event.route
            print(f"Route changed to: {route}")
            self.page.views.clear()

            match route:
                case "/":
                    view = HomeView().get_content()
                    app_bar_title = "Pagina Principal"
                case "/store":
                    view = StoreView().get_content()
                    app_bar_title = "Store"
                case "/pedido":
                    view = PedidoView(self.page).get_content()
                    app_bar_title = "Pedido de Compra"                    
                case _:
                    view = HomeView().get_content()
                    app_bar_title = "Pagina Principal"

            self.page.views.append(ft.View(
                route,
                [
                    self.page.drawer,
                    MyAppBar(app_bar_title, ft.colors.RED_500),
                    view
                ]
            ))
            self.page.update()

        self.page.on_route_change = route_change
        self.page.go("/")  # Define the initial route

if __name__ == '__main__':
    ft.app(target=App, assets_dir='assets')
