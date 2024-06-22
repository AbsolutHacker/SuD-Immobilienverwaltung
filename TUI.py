from Model import Realty, Room, Rect
from Persistence import export, persist

from functools import partial
print = partial(print, flush=True)

def raum_einlesen() -> Room:
    raum = Room(input('Raum-Bezeichnung: '))
    while True:
        raum.add_partial(teilflaeche_einlesen())
        if input("Weitere Teilfläche hinzufügen? ").rstrip().lower() != 'j':
            print()
            break
    return raum


def teilflaeche_einlesen() -> Rect:
    laenge = input("Länge: ")
    laenge = float("0" + laenge)
    breite = input("Breite: ")
    breite = float("0" + breite)
    return Rect(breite, laenge)


def sanitize_currency_amount(instr):
    instr = instr.replace(" ", "")
    instr = instr.replace("\t", "")
    instr = instr.replace(".", "")
    instr = instr.replace("€", "")
    instr = instr.replace(",", ".")
    return float("0" + instr)


def objekt_einlesen() -> Realty:
    # Metadaten eingeben: Objekt, Name Makler
    site_name = input("Name des Objekts: ")
    site_owner = input(f"Besitzer des Objekts '{site_name}': ")
    site_price = sanitize_currency_amount(input("Verkaufspreis in €: "))
    site = Realty(site_name, site_owner, site_price)

    # Flächen einlesen
    weitere_flaeche_eingeben = "j"
    while weitere_flaeche_eingeben == "j":
        print()
        # Raummaße eingeben
        raum = raum_einlesen()
        # Raum-Aufmaß an Liste anhängen
        site.add_room(raum)
        weitere_flaeche_eingeben = input("Wollen Sie einen weiteren Raum hinzufügen? ")

    # Sortieren
    site.rooms.sort(key=lambda r: r.identifier)
    return site


def list_sites(sites):
    for index, site in enumerate(sites):
        print(f"({index}) {site.identifier}")


def clear_screen():
    print(chr(27) + "[2J")


def menu_edit(site: Realty) -> Realty:
    print(site)
    print("""
    (a) Raum hinzufügen
    (d) Raum löschen
    (r) Objekt umbenennen
    (c) Abbrechen
    """)
    match input("Kommando: ").strip().lower():
        case "a":
            site.add_room(raum_einlesen())
            return site
        case "d":
            raise NotImplemented
        case "r":
            site_name = input("Neuer Name des Objekts: ")
            site.identifier = site_name
            return site
        case "c":
            return site
        case _:
            print("Unbekanntes Kommando!")
            return menu_edit(site)

def run_menu(sites):
    print("""
    (n) Neues Objekt anlegen
    (l) Alle Objekte anzeigen
    (e) Objekt bearbeiten
    (d) Objekt löschen
    (x) Daten exportieren
    (q) Programm beenden
    """)
    selection = input("Kommando: ")
    clear_screen()
    match selection:
        case 'n':
            site = objekt_einlesen()
            sites.append(site)
            persist(sites)
        case 'l':
            for site in sites:
                print(site)
        case 'e':
            list_sites(sites)
            index = int(input("Immobilie auswählen, die bearbeitet werden soll: "))
            site = sites[index]
            site = menu_edit(site)
            sites.remove(sites[index])
            sites.append(site)
            persist(sites)
        case 'd':
            list_sites(sites)
            index = int(input("Immobilie auswählen, die gelöscht werden soll: "))
            site = sites[index]
            print(f"Entferne Immobilie #{index} '{site.identifier}'")
            sites.remove(site)
            persist(sites)
        case 'x':
            filename = input("Dateiname für den Export: ")
            export(filename, sites)
        case 'q':
            exit(0)


def run(sites):
    while True:
        run_menu(sites)