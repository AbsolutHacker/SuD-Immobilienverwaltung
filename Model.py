class Realty:
    def __init__(self, ident, owner, price, realtor = None):
        self.identifier = ident
        self.owner = owner
        self.price = price
        self.responsible = realtor
        self.rooms = []
    def add_room(self, room):
        self.rooms.append(room)
    def area(self):
        from functools import reduce
        return reduce(lambda x, y: x + y.area(), self.rooms, 0)
    def avg_area(self):
        return self.area()/len(self.rooms)
    def __str__(self):
        ### Ausgabe
        # Metadaten ausgeben
        # Gesamt-Fläche berechnen
        result = f"\n\nImmobilie: {self.identifier}\n"
        result += f"Eigentümer: {self.owner}\n"
        result += f"Verkaufspreis: {self.price} €\n\n"
        for index, room in enumerate(self.rooms):
            result += f"\t({index + 1})\t{room.identifier}: {room.area():.2f}\n"
        result += f"\nGesamtfläche: {self.area():.2f}\nDurchschnittliche Fläche: {self.avg_area():.2f}"
        return result



class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Room:
    def __init__(self, ident):
        self.identifier = ident
        self.partials = []
        # partial: Rect

    def add_partial(self, partial):
        self.partials.append(partial)

    def area(self):
        from functools import reduce
        return reduce(lambda x, y: x + y.area(), self.partials, 0)

