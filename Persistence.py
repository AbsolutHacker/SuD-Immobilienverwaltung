from Model import Realty, Room

def persist(obj):
    import pickle
    with open('makler.data', 'wb') as f:
        pickle.dump(obj, f)


def load():
    import pickle
    try:
        with open('makler.data', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []


def export(filename, sites: list[Realty]):
    import csv
    try:
        with open(filename, 'r'):
            raise FileExistsError()
    except FileNotFoundError:
        pass
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        for realty in sites:
            writer.writerow([realty.identifier, realty.owner, realty.price, realty.responsible])
            for room in realty.rooms:
                writer.writerow([room.identifier, room.area()])
