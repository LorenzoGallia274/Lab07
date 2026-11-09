from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        # TODO
        # chiedo al DAO la lista dei libri passando i due filtri
        risultato = self._libro_dao.get_libri_filtrati(biblioteca,genere)
        # restiuisco il risultato al controller
        return risultato

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        # TODO
        # chiedo al DAO la lista di tutti i generi distinti
        risultato = self._libro_dao.get_generi()
        # restituisco il risultato al controller
        return risultato

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # TODO
        # chiedo al DAO la lista di tutte le bibilioteche
        risultato = self._biblioteca_dao.get_biblioteche()
        # restituisco il risultato al controller
        return risultato
