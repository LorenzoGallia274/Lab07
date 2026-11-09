import flet as ft
from flet import MainAxisAlignment

from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO
        # dropdown biblioteca e collega la selezione (on_select) a biblioteca_change (nel controller)
        self.dd_biblioteca = ft.Dropdown(label='Biblioteca', width = 500, on_select = self.controller.biblioteca_change)
        # dropdown genere e collega la selezione (on_select) a genere_change (nel controller)
        self.dd_genere = ft.Dropdown(label='Genere', width=250, on_select = self.controller.genere_change)
        # chiama il controlloer (popola dd) per riempire i dd con i dati del db
        self.controller.popola_dropdown()

        # Sezione 3: Libri
        # TODO
        # bottone per mostrare i libri e collega il click (on_click) a mostra_libri (nel controller)
        self.btn_mostra = ft.Button('Mostra libri', on_click = self.controller.mostra_libri)
        # crea la listview scorrevole con l'output dei libri trovati
        self.lista_libri = ft.ListView(expand = True, spacing = 10, padding = 20)


        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # TODO
            # row con i dd allineati al centro
            ft.Row(spacing = 50,
                   controls = [self.dd_biblioteca, self.dd_genere],
                   alignment = ft.MainAxisAlignment.CENTER ),
            ft.Divider(),

            # Sezione 3: Libri
            # TODO
            # row con il bottone per mostrare i libri allineato al centro
            ft.Row(spacing=50,
                   controls=[self.btn_mostra],
                   alignment=ft.MainAxisAlignment.CENTER),
            # listview che mostrerà i risultati in fondo
            self.lista_libri
        )
        # rendo la pagina scrollabile
        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
