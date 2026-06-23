import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Esame 29/06/2020 IMDB"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT

        # controller
        self._controller = None

        # graphical elements
        self._title = None
        self._dd_anno = None
        self._dd_regista = None
        self._txt_attori_condivisi = None

        self._btn_crea_grafo = None
        self._btn_registi_adiacenti = None
        self._btn_registi_affini = None
        self.txt_result = None

    def load_interface(self):
        # Title
        self._title = ft.Text("Esame 29/06/2020 IMDB", color="blue", size=24)
        self._page.controls.append(self._title)

        # Riga 1: Selezione Anno e Bottone Crea Grafo
        self._dd_anno = ft.Dropdown(
            label="Anno",
            hint_text="Seleziona l'anno",
            width=300,
            options=[
                ft.dropdown.Option("2004"),
                ft.dropdown.Option("2005"),
                ft.dropdown.Option("2006")
            ]
        )
        self._btn_crea_grafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handleCreaGrafo,
                                                 width=200)

        row1 = ft.Row([self._dd_anno, self._btn_crea_grafo],
                      alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.END)
        self._page.controls.append(row1)

        # Riga 2: Selezione Regista (d) e Bottone Registi Adiacenti
        self._dd_regista = ft.Dropdown(label="Director (d)", hint_text="Seleziona un regista", width=300)
        self._btn_registi_adiacenti = ft.ElevatedButton(text="Registi Adiacenti",
                                                        on_click=self._controller.handleRegistiAdiacenti, width=200)

        row2 = ft.Row([self._dd_regista, self._btn_registi_adiacenti],
                      alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.END)
        self._page.controls.append(row2)

        # Riga 3: Inserimento Numero Attori Condivisi (c) e Bottone Cerca Registi Affini
        self._txt_attori_condivisi = ft.TextField(label="# Attori Condivisi (c)",
                                                  hint_text="Inserisci un valore intero", width=300)
        self._btn_registi_affini = ft.ElevatedButton(text="Cerca Registi Affini",
                                                     on_click=self._controller.handleCercaRegistiAffini, width=200)

        row3 = ft.Row([self._txt_attori_condivisi, self._btn_registi_affini],
                      alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.END)
        self._page.controls.append(row3)

        # Area di testo per la stampa dei risultati (ListView)
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()