#ESERCIZIO NUMERO 4
class Libro:#inizializzo qui una classe Libro con attributi titolo autore anno e quantita
    def __init__(self, titolo, autore, anno, quantita):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.quantita = quantita

    def __str__(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Anno: {self.anno}, Quantità: {self.quantita}"



class Libreria:#inizializzo una classe libreria solo per salvare i libri e richiamare poi le funzioni
    def __init__(self):
        self.libri = []#inizializzo una lista per aggiungere i libri

    
    def aggiungi_libro(self):
        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci l'autore del libro: ")
        anno = input("Inserisci l'anno di pubblicazione: ")
        quantita = int(input("Inserisci la quantità disponibile: "))
        libro = Libro(titolo, autore, anno, quantita)
        self.libri.append(libro)
        print(f"\nLibro '{titolo}' aggiunto alla libreria!\n")

    
    def visualizza_libri(self):
        if not self.libri: #se non c'è nulla nella libreria
            print("La libreria è vuota.")
        else:
            print("Lista dei libri:")
            for libro in self.libri:#faccio un for per stampare un libro per volta
                print(libro)

    
    def trova_libro(self):
        titolo = input("Inserisci il titolo del libro da cercare: ")
        for libro in self.libri:
            if libro.titolo.lower() == titolo.lower():#inserisco un controllo su maiusc minusc
                print(f"Ecco il tuo libro:\n{libro}\n")
                return libro
        print(f"Il libro '{titolo}' non è presente.\n")
        return None

    
    def gestione(self):
        libro = self.trova_libro()
        if libro:
            print("Cosa vuoi fare?")
            print("1. Modificare un libro")
            print("2. Aggiungere una copia")
            print("3. Rimuovere un libro")
            scelta = input("Seleziona un'opzione: ")

            if scelta == '1':
                libro.titolo = input(f"Inserisci il nuovo titolo (attuale: {libro.titolo}): ")
                libro.autore = input(f"Inserisci il nuovo autore (attuale: {libro.autore}): ")
                libro.anno = input(f"Inserisci il nuovo anno (attuale: {libro.anno}): ")
                libro.quantita = int(input(f"Inserisci la nuova quantità (attuale: {libro.quantita}): "))
                print(f"\nLibro aggiornato:\n{libro}\n")

            elif scelta == '2':
                libro.quantita += 1
                print(f"Hai aggiunto una copia. Ora le copie di '{libro.titolo}' sono: {libro.quantita}\n")

            elif scelta == '3':
                self.libri.remove(libro)
                print(f"\nLibro '{libro.titolo}' rimosso dalla libreria.\n")
            else:
                print("\nScelta non valida.\n")

def menu():
    libreria = Libreria()

    while True:
        print("\nCosa vuoi fare?")
        print("1. Aggiungere un nuovo libro")
        print("2. Visualizzare tutti i libri")
        print("3. Cercare un libro per titolo")
        print("4. Gestione libri")
        print("5. Esci")

        scelta = input("\nSeleziona un'opzione: ")

        if scelta == '1':
            libreria.aggiungi_libro()#richiamo la funzione
        elif scelta == '2':
            libreria.visualizza_libri()#richiamo la funzione
        elif scelta == '3':
            libreria.trova_libro()#richiamo la funzione
        elif scelta == '4':
            libreria.gestione()#richiamo la funzione
        elif scelta == '5':
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Riprova.\n")

menu()
