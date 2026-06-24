import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Simulazione d'esame 10/06/2020"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT

        # controller
        self._controller = None

        # graphical elements
        self._title = None
        self._dd_genere = None
        self._dd_attore = None
        self._txt_giorni = None

        self._btn_crea_grafo = None
        self._btn_attori_simili = None
        self._btn_simulazione = None
        self.txt_result = None

    def load_interface(self):
        # Title
        self._title = ft.Text("Simulazione d'esame 10/06/2020", color="blue", size=24)
        self._page.controls.append(self._title)

        # Riga 1: Selezione Genere (g) e Bottone Crea Grafo
        self._dd_genere = ft.Dropdown(label="Genere (g)", hint_text="Seleziona un genere", width=300)
        self._btn_crea_grafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handleCreaGrafo,
                                                 width=200)
        self._controller.fillDDGeneri()

        row1 = ft.Row([self._dd_genere, self._btn_crea_grafo],
                      alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.END)
        self._page.controls.append(row1)

        # Riga 2: Selezione Attore (a) e Bottone Attori Simili
        self._dd_attore = ft.Dropdown(label="Attore (a)", hint_text="Seleziona un attore", width=300)
        self._btn_attori_simili = ft.ElevatedButton(text="Attori Simili", on_click=self._controller.handleAttoriSimili,
                                                    width=200)

        row2 = ft.Row([self._dd_attore, self._btn_attori_simili],
                      alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.END)
        self._page.controls.append(row2)

        # Riga 3: Inserimento Numero Giorni (n) e Bottone Simulazione
        self._txt_giorni = ft.TextField(label="# Giorni (n)", hint_text="Inserisci un valore intero", width=300)
        self._btn_simulazione = ft.ElevatedButton(text="Simulazione", on_click=self._controller.handleSimulazione,
                                                  width=200)

        row3 = ft.Row([self._txt_giorni, self._btn_simulazione],
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