import flet as ft
from partials.button import MyButton

class PedidoView:
    def __init__(self, page):
        self.page = page

    def handle_date_change(self, e):
        self.page.add(ft.Text(f"Date changed: {e.control.value.strftime('%Y-%m-%d')}"))

    def handle_date_dismissal(self, e):
        self.page.add(ft.Text("DatePicker dismissed"))

    def get_content(self):
        pg_dd_codigo_empresa = ft.Dropdown(
            col={"md": 2},
            label="Origem",
            hint_text="Empresa",
            focused_border_color=ft.colors.YELLOW,
            options=[
                ft.dropdown.Option(1, text="01 - MATRIZ"),
                ft.dropdown.Option(4, text="04 - FILIAL"),
                ft.dropdown.Option(12, text="12 - SV BM"),
                ft.dropdown.Option(59, text="59 - SV WS"),
            ],
            autofocus=True,
        )
        
        pg_codigo_chamada = ft.TextField(
            label="Código", 
            hint_text="FORNECEDOR",
            col={"md": 2},
            focused_border_color=ft.colors.YELLOW,
            input_filter=ft.NumbersOnlyInputFilter()
        )

        pg_nome_fornecedor = ft.TextField(
            label="Nome", 
            hint_text="FORNECEDOR",
            col={"md": 8},
            focused_border_color=ft.colors.YELLOW,
            input_filter=ft.NumbersOnlyInputFilter()
        )
        
        empresa_codigo_fornecedor = ft.ResponsiveRow(
            columns=12,
            controls=[pg_dd_codigo_empresa, pg_codigo_chamada, pg_nome_fornecedor],
        )

        date_picker = ft.DatePicker(
            cancel_text='Cancelar',
            confirm_text='Selecionar',
            error_format_text='Data inválida',
            field_label_text='Digite uma data',
            help_text='Selecione uma data no calendário',
            on_change=self.handle_date_change,
            on_dismiss=self.handle_date_dismissal
        )

        btn_pick_date_start = ft.TextField(
            label="Código", 
            hint_text="FORNECEDOR",
            col={"md": 2},
            focused_border_color=ft.colors.YELLOW,
            on_focus=lambda e: self.page.open(date_picker),
        )        

        btn_pick_date_end = ft.TextField(
            label="Código", 
            hint_text="FORNECEDOR",
            col={"md": 2},
            focused_border_color=ft.colors.YELLOW,
            on_focus=lambda e: self.page.open(date_picker),
        )  

        layout = ft.Column(
            controls=[empresa_codigo_fornecedor, btn_pick_date_start, btn_pick_date_end],
            alignment=ft.alignment.center,
            expand=True
        )

        return layout
