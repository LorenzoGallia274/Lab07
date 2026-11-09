import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO

    def popola_dropdown(self):
        # ottiene dal model la lista di oggetti Biblioteca
        biblioteche =self._model.get_biblioteche()
        # ottiene dal model la lista di generi
        generi = self._model.get_generi()
        # con options metto all'interno del dd delle biblioteche la lista delle scelte
        lista_dd_b = self._view.dd_biblioteca.options
        # così appendo subito l'opzione 'Nessun filtro'
        lista_dd_b.append(ft.dropdown.Option('Nessun filtro'))
        # scorro tutte le biblioteche lette nel db
        for b in biblioteche:
            # ci appendo l'opzione di filtraggio (id) ma come output mostrerà il text (nome)
            lista_dd_b.append(ft.dropdown.Option(key = b.id, text = b.nome))
        lista_dd_g = self._view.dd_genere.options
        lista_dd_g.append(ft.dropdown.Option('Nessun filtro'))
        for g in generi:
            lista_dd_g.append(ft.dropdown.Option(g))



    # CALLBACKS DROPDOWN
    # TODO
    def biblioteca_change(self,e):
        # controllo se l'utente abbia scelto di non filtrare per biblioteca
        if self._view.dd_biblioteca.value == 'Nessun filtro':
            # imposta None così Coalesce ignorerà il filtro biblioteca
            self.biblioteca_selezionata = None
        else:
            # sennò salva l'id (key) della biblioteca selezionata
            self.biblioteca_selezionata = self._view.dd_biblioteca.value

    def genere_change(self,e):
        # controllo se l'utente abbia scelto di non filtrare per genere
        if self._view.dd_genere.value == 'Nessun filtro':
            # imposta None così Coalesce ignorerà il filtro genere
            self.genere_selezionato = None
        else:
            # sennò salva il genere selezionato
            self.genere_selezionato = self._view.dd_genere.value

    # AZIONE: MOSTRA LIBRI
    # TODO
    def mostra_libri(self,e):
        # svuota la listview della ricerca precedente
        self._view.lista_libri.controls.clear()
        # chiede al model la lista dei libri passando i due filtri correnti (o None)
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata,self.genere_selezionato)
        # se non si connette
        if libri is None:
            self._view.show_alert('Errore di connessione al database')
        # se è vuota
        elif len(libri) == 0:
            self._view.show_alert('Errore: nessun libro presente')
        else:
            for libro in libri:
                # converte l'oggeto in stringa e lo inserisce come testo nella listview
                self._view.lista_libri.controls.append(ft.Text(f'{libro}'))
        self._view.update()

