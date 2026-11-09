from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def get_generi(self):
        # prendo una connessione (get_connection) dal pool in DBConnect
        cnx = DBConnect.get_connection()
        # se la connessione al db è fallita
        if cnx is None:
            return None
        else:
            # cursore che restituisce ogni riga come dizionario
            cursore_diz = cnx.cursor(dictionary=True)
            # query sql che etrae i generi (senza duplicati)
            query = 'SELECT DISTINCT genere FROM libro'
            cursore_diz.execute(query)
            # lista vuota per raccogliere gli oggetti
            generi = []
            for riga in cursore_diz:
                # estraggo dal dizionario solo la stringa associata alla sua chiave (genere)
                nuovo_L = riga['genere']
                generi.append(nuovo_L)
            cursore_diz.close()
            cnx.close()
            return generi

    def get_libri_filtrati(self, id_biblioteca, genere):
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None
        else:
            cursore_diz = cnx.cursor(dictionary=True)
            # query sql con filtro Coalesce (se l'utente passa un valore, python sostitusce il %s con quel filtro
            # se l'utente non passa nulla, nessun filtro, python sostituisce %s con null)
            # filtro i libri per id e genere (comprese combinazioni)
            query = ('''SELECT * FROM libro
                        WHERE id_biblioteca = COALESCE(%s,id_biblioteca) AND genere = COALESCE(%s,genere)  ''')
            # al posto del %s passo la tupla (id_biblioteca,genere)
            cursore_diz.execute(query, (id_biblioteca,genere))
            libri_filtrati = []
            for riga in cursore_diz:
                nuovo_LF = Libro(**riga)
                libri_filtrati.append(nuovo_LF)
            cursore_diz.close()
            cnx.close()
            return libri_filtrati