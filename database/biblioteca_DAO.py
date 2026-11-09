from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass
    # TODO
    def get_biblioteche(self):
        # prendo una connessione (get_connection) dal pool in DBConnect
        cnx = DBConnect.get_connection()
        # se la connessione al db è fallita
        if cnx is None:
            return None
        else:
            # cursore che restituisce ogni riga come dizionario
            cursore_diz = cnx.cursor(dictionary=True)
            # query sql per selezionare tutte le biblioteche
            query = 'SELECT * FROM biblioteca'
            cursore_diz.execute(query)
            # lista vuota per raccogliere gli oggetti
            biblioteche = []
            for riga in cursore_diz:
                # 'shortcut' fatto a lezione (visto che i nomi sono uguali) per creare l'oggetto Biblioteca
                nuova_B = Biblioteca(**riga)
                biblioteche.append(nuova_B)
            cursore_diz.close()
            cnx.close()
            # restituisco la lista completa di oggetti bibliotecs
            return biblioteche





