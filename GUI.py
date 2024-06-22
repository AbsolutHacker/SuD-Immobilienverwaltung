from Model import Realty
import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Immobilienverwaltung')
        self.resizable(True, False)

        selection_frame = tk.Frame(self)
        listbox = tk.Listbox(selection_frame, selectmode=tk.SINGLE)
        self.listbox = listbox

        button_frame = tk.Frame(selection_frame)
        insert_button = tk.Button(button_frame, text='  +  ', command=lambda: RealtyWindow().show())
        delete_button = tk.Button(button_frame, text='  --  ')
        insert_button.pack(side=tk.LEFT)
        delete_button.pack(side=tk.RIGHT)
        button_frame.pack(side=tk.TOP)

        listbox.pack(side=tk.BOTTOM)
        selection_frame.pack(side=tk.LEFT)

        info_frame = tk.Frame(self)

        label_identifier = tk.Label(info_frame, text='-')
        self.label_identifier = label_identifier
        label_identifier.pack(side=tk.TOP)

        frame_info_owner = tk.Frame(info_frame)
        label_owner_label = tk.Label(frame_info_owner, text='Eigentümer: ')
        label_owner = tk.Label(frame_info_owner, text='-')
        self.label_owner = label_owner
        label_owner_label.pack(side=tk.LEFT)
        label_owner.pack(side=tk.RIGHT)
        frame_info_owner.pack()

        frame_info_salesprice = tk.Frame(info_frame)
        label_salesprice_label = tk.Label(frame_info_salesprice, text='Verkaufspreis: ')
        label_salesprice = tk.Label(frame_info_salesprice, text='-')
        self.label_salesprice = label_salesprice
        label_salesprice_label.pack(side=tk.LEFT)
        label_salesprice.pack(side=tk.RIGHT)
        frame_info_salesprice.pack()

        frame_info_totalarea = tk.Frame(info_frame)
        label_totalarea_label = tk.Label(frame_info_totalarea, text='Gesamtfläche: ')
        label_totalarea = tk.Label(frame_info_totalarea, text='-')
        self.label_totalarea = label_totalarea
        label_totalarea_label.pack(side=tk.LEFT)
        label_totalarea.pack(side=tk.RIGHT)
        frame_info_totalarea.pack()

        frame_info_avgroomsize = tk.Frame(info_frame)
        label_avgroomsize_label = tk.Label(frame_info_avgroomsize, text='Durchschnittliche Raumgröße: ')
        label_avgroomsize = tk.Label(frame_info_avgroomsize, text='-')
        self.label_avgroomsize = label_avgroomsize
        label_avgroomsize_label.pack(side=tk.LEFT)
        label_avgroomsize.pack(side=tk.RIGHT)
        frame_info_avgroomsize.pack()

        info_frame.pack(side=tk.RIGHT)

    def on_select(self, handler):
        self.listbox.bind('<<ListboxSelect>>', lambda e: handler(self, self.listbox.curselection()))

    def update_labels(self, site: Realty):
        if site is not None:
            self.label_identifier['text'] = site.identifier
            self.label_owner['text'] = site.owner
            self.label_salesprice['text'] = f'{site.price} €'
            self.label_totalarea['text'] = f'{site.area():.2f} m²'
            self.label_avgroomsize['text'] = f'{site.avg_area():.2f} m²'


class RealtyWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Objekt bearbeiten')
        self.resizable(True, True)

        selection_frame = tk.Frame(self)
        listbox = tk.Listbox(selection_frame, selectmode=tk.SINGLE)
        self.listbox = listbox

        button_frame = tk.Frame(selection_frame)
        insert_button = tk.Button(button_frame, text='  +  ')
        delete_button = tk.Button(button_frame, text='  --  ')
        insert_button.pack(side=tk.LEFT)
        delete_button.pack(side=tk.RIGHT)
        button_frame.pack(side=tk.TOP)

        listbox.pack(side=tk.BOTTOM)
        selection_frame.pack(side=tk.LEFT)

    def show(self):
        self.mainloop()

def run(sites: list[Realty]):
    window = MainWindow()

    for site in sites:
        window.listbox.insert(tk.END, site.identifier)

    window.on_select(lambda win, sel_index_list: window.update_labels(sites[sel_index_list[0]] if len(sel_index_list) > 0 else None))

    window.mainloop()
